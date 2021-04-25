import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from PySide6.QtGui import QAction

from GUIMonkey import GUIMonkeyCore
from ui.views.GUIMonkeyMain import Ui_GUIMonkeyMain
from ui.support_widgets import CreateTimelineDialog


class GuiMonkeyUI(QMainWindow):
    def __init__(self):
        super(GuiMonkeyUI, self).__init__()
        self.core = GUIMonkeyCore()

        self.ui = Ui_GUIMonkeyMain()
        self.ui.setupUi(self)

        # Timeline list Context Menu
        self.ui.timelineList.setContextMenuPolicy(Qt.ActionsContextMenu)

        delete_action = QAction("Remove Timeline", self.ui.timelineList)
        self.ui.timelineList.addAction(delete_action)
        print("HERE")
        print(self.ui.timelineList.actions())

        # Hookup buttons
        self.ui.addTimelineButton.clicked.connect(self.add_timeline)
        delete_action.triggered.connect(self.delete_timeline)

    def update_timelines(self):
        self.ui.timelineList.clear()

        for timeline in self.core.timelines.values():
            self.ui.timelineList.addItem(QListWidgetItem(timeline.name))

        self.ui.timelineList.sortItems()

    def add_timeline(self):
        create_timeline_dialog = CreateTimelineDialog()
        result = create_timeline_dialog.exec_()
        if not result:
            print("Canceled")
        else:
            print(create_timeline_dialog.ui.timelineNameLine.text(),
            create_timeline_dialog.ui.timelineSourceLine.text())
        self.core.create_timeline(
            create_timeline_dialog.ui.timelineNameLine.text(),
            create_timeline_dialog.ui.timelineSourceLine.text()
        )
        print("CREATED NEW TIMELINE")
        self.update_timelines()

    def delete_timeline(self):
        selected_timeline = self.ui.timelineList.currentItem().text()
        print(f"Deleting {selected_timeline}")

        self.core.delete_timeline(selected_timeline)
        self.update_timelines()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = GuiMonkeyUI()
    window.show()

    sys.exit(app.exec_())
