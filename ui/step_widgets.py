from PySide6.QtWidgets import QWidget, QLabel, QSpinBox, QLineEdit, QComboBox

import Steps
from ui.views.StepBase import Ui_stepBaseWidget


def create_step_widget(step):
    step_type = step.__class__.__name__
    step_dict = {
        "KeyPress": KeyPressWidget,
        # "WaitForImage": WaitForImageWidget,
        # "Delay": DelayWidget
    }
    step_widget = step_dict[step_type](step)
    return step_widget


class StepBaseWidget(QWidget):
    def __init__(self, step):
        super(StepBaseWidget, self).__init__()
        self.ui = Ui_stepBaseWidget()
        self.ui.setupUi(self)

        # Step name hookup
        self.step = step
        self.ui.stepNameLine.setText(step.name)
        self.ui.stepNameLine.textChanged.connect(self.update_step_name)

        # Load specific step type details
        self.load_details()

    def update_step_name(self):
        self.step.name = self.ui.stepNameLine.text()

    def load_details(self):
        """virtual function to be overloaded"""
        pass


class KeyPressWidget(StepBaseWidget):
    def __init__(self, step: Steps.KeyPress):
        super(KeyPressWidget, self).__init__(step)

    def load_details(self):
        detail_layout = self.ui.detailFrame.layout()

        # Key input
        self.key_label = QLabel("Key", self)
        self.key_line_edit = QLineEdit(self)
        self.key_line_edit.setMaxLength(1)
        self.key_line_edit.setText(self.step.key)
        self.key_line_edit.textChanged.connect(self.update_key)

        # Mod Input
        self.mod_label = QLabel("Mod", self)
        self.mod_combo = QComboBox(self)
        mod_list = ["None", "Ctrl", "Shift", "Alt", "Super"]
        self.mod_combo.addItems(mod_list)

        if self.step.mod:
            current_mod_index = mod_list.index(self.step.mod.capitalize())
            self.mod_combo.setCurrentIndex(current_mod_index)

        self.mod_combo.currentIndexChanged.connect(self.update_mod)

        # Add to layout
        detail_layout.addWidget(self.key_label)
        detail_layout.addWidget(self.key_line_edit)
        detail_layout.addWidget(self.mod_label)
        detail_layout.addWidget(self.mod_combo)

    def update_key(self):
        if self.key_line_edit.text() == None:
            self.key_line_edit.setText(" ")
        self.step.key = self.key_line_edit.text()

    def update_mod(self):
        if self.mod_combo.currentText() == "None":
            self.step.mod = None
        else:
            self.step.mod = self.mod_combo.currentText().lower()
