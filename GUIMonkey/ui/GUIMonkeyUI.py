import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, \
    QMessageBox
from PySide6.QtCore import Qt

from GUIMonkey import Steps, GUIMonkeyCore
from GUIMonkey.Timelines import Timeline

from GUIMonkey.ui.views.GUIMonkeyMain import Ui_GUIMonkeyMain
from GUIMonkey.ui.support_widgets import CreateTimelineDialog
from GUIMonkey.ui.step_widgets import create_step_widget


class GuiMonkeyUI(QMainWindow):
    def __init__(self):
        super(GuiMonkeyUI, self).__init__()
        self.ui = Ui_GUIMonkeyMain()
        self.ui.setupUi(self)

        self.core = GUIMonkeyCore()
        self.current_timeline: Timeline = None

        # Timeline list Context Menu
        delete_action = self.ui.deleteTimelineAction
        self.ui.timelineList.addAction(delete_action)

        # Action connect
        delete_action.triggered.connect(self.delete_timeline)

        # Signal/Slots
        self.ui.timelineList.currentItemChanged.connect(self.update_selected_timeline)
        self.ui.addTimelineButton.clicked.connect(self.add_timeline)
        self.ui.executeButton.clicked.connect(self.execute_timeline)
        self.ui.addStepButton.clicked.connect(self.add_step_to_timeline)
        self.ui.removeStepButton.clicked.connect(self.remove_step_from_timeline)
        self.ui.testButton.clicked.connect(self.test_button)

    def add_step_to_timeline(self):
        """Add step to current selected timeline"""
        if not self.current_timeline:
            return
        self.current_timeline.add_step(Steps.WaitForImage)
        self.update_steps()

    def remove_step_from_timeline(self):
        if self.ui.scrollFrame.layout().count() == 0:
            return
        self.current_timeline.remove_step()
        self.update_steps()

    def update_selected_timeline(self):
        """Update UI to view current selected timeline details"""
        if not self.ui.timelineList.currentItem():
            return
        timeline_name = self.ui.timelineList.currentItem().text()
        self.current_timeline: Timeline = self.core.timelines[timeline_name]

        self.update_steps()

    def test_button(self):

        print("ScrollFrame Children: ", self.ui.scrollFrame.children())
        print(f"scrollframe ui count:", self.ui.scrollFrame.layout().count())

    def update_steps(self):
        """Clear and regenerate step scroll bar"""
        layout = self.ui.scrollFrame.layout()
        for widget_index in reversed(range(layout.count())):
            # Removed widgets need to be marked to destroy in main loop
            removed = layout.takeAt(widget_index)
            removed.widget().deleteLater()

        # Regenerate new steps
        for step in self.current_timeline.steps:
            step_widget = create_step_widget(step)
            layout.addWidget(step_widget)

        self.ui.timelineList.repaint()

    def update_timelines(self):
        self.ui.timelineList.clear()

        for timeline in self.core.timelines.values():
            self.ui.timelineList.addItem(QListWidgetItem(timeline.name))

        self.ui.timelineList.sortItems()

    def add_timeline(self):
        create_timeline_dialog = CreateTimelineDialog()
        result = create_timeline_dialog.exec_()

        if not result:
            print("Canceled Timeline Creation")
            return

        timeline_name = create_timeline_dialog.ui.timelineNameLine.text()

        self.core.create_timeline(
            timeline_name,
            create_timeline_dialog.ui.timelineSourceLine.text()
        )

        self.update_timelines()

        item = self.ui.timelineList.findItems(timeline_name, Qt.MatchExactly)[0]
        index = self.ui.timelineList.indexFromItem(item)
        self.ui.timelineList.setCurrentIndex(index)

    def delete_timeline(self):
        # Check for user confirmation
        confirm_dialog = QMessageBox()
        confirm_dialog.setIcon(QMessageBox.Warning)
        confirm_dialog.setWindowTitle("Confirm Delete")
        confirm_dialog.setText("Are you sure?")
        confirm_dialog.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        confirm_dialog.setDefaultButton(QMessageBox.Cancel)

        if confirm_dialog.exec_() == QMessageBox.Cancel:
            return

        selected_timeline = self.ui.timelineList.currentItem().text()

        self.core.delete_timeline(selected_timeline)
        self.update_timelines()

    def execute_timeline(self):
        self.current_timeline.run_timeline()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = GuiMonkeyUI()
    window.show()

    sys.exit(app.exec_())
