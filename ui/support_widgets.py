from PySide6.QtWidgets import QDialog
from ui.views.CreateTimelineDialog import Ui_createTimelineDialog


class CreateTimelineDialog(QDialog):
    def __init__(self):
        super(CreateTimelineDialog, self).__init__()

        self.ui = Ui_createTimelineDialog()
        self.ui.setupUi(self)