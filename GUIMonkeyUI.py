import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.GUIMonkeyMain import Ui_GUIMonkeyMain


class GuiMonkeyUI(QMainWindow):
    def __init__(self):
        super(GuiMonkeyUI, self).__init__()
        self.ui = Ui_GUIMonkeyMain()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = GuiMonkeyUI()
    window.show()

    sys.exit(app.exec_())
