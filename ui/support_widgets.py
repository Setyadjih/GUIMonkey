from PySide6.QtWidgets import QDialog, QFileDialog
from ui.views.CreateTimelineDialog import Ui_createTimelineDialog


class CreateTimelineDialog(QDialog):
    def __init__(self):
        super(CreateTimelineDialog, self).__init__()
        self.ui = Ui_createTimelineDialog()
        self.ui.setupUi(self)

        self.ui.select_app_btn.clicked.connect(self.select_source)

    def select_source(self):
        source = QFileDialog.getOpenFileName(
            self,
            "Select Source",
            "C:/",
        )
        self.ui.timelineSourceLine.setText(source[0])
