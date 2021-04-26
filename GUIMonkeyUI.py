import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, \
    QMessageBox

import Steps
from GUIMonkey import GUIMonkeyCore
from Timelines import Timeline

from ui.views.GUIMonkeyMain import Ui_GUIMonkeyMain
from ui.support_widgets import CreateTimelineDialog
from ui.step_widgets import create_step_widget


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

    def add_step_to_timeline(self):
        """Add step to current selected timeline"""
        if not self.current_timeline:
            return
        self.current_timeline.add_step(Steps.KeyPress())
        self.update_steps()

    def update_selected_timeline(self):
        """Update UI to view current selected timeline details"""
        timeline_name = self.ui.timelineList.currentItem().text()
        self.current_timeline: Timeline = self.core.timelines[timeline_name]

        self.update_steps()

    def update_steps(self):
        """Clear and regenerate step scroll bar"""
        # FIXME: there seems to be left overs when clearing the step
        #  widgets. Need to see if there's a better way to handle the
        #  refresh or clearing
        layout = self.ui.timelineScroll.layout()
        print(f"current steps: {layout.count()}")
        for step_widget in reversed(range(layout.count())):
            print(f"removing widget at {step_widget}")
            layout.takeAt(step_widget)

        for step in self.current_timeline.steps:
            step_widget = create_step_widget(step)
            self.ui.timelineScroll.layout().addWidget(step_widget)

        self.ui.timelineList.repaint()
        print(f"new steps: {layout.count()}")


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

        self.core.create_timeline(
            create_timeline_dialog.ui.timelineNameLine.text(),
            create_timeline_dialog.ui.timelineSourceLine.text()
        )

        self.update_timelines()

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
