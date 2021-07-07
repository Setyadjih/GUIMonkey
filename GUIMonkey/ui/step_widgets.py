from PySide6.QtWidgets import QWidget, QLabel, QSpinBox, QLineEdit, \
    QComboBox, QPushButton, QFileDialog, QFormLayout
from PySide6.QtGui import QPalette, QColor
from GUIMonkey import Steps
from GUIMonkey.ui.views.StepBase import Ui_stepBaseWidget


def create_step_widget(step):
    step_type = step.__class__.__name__
    step_dict = {
        "KeyPress": KeyPressWidget,
        "WaitForImage": WaitForImageWidget,
        "Delay": DelayWidget
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

    def update_step_name(self):
        self.step.name = self.ui.stepNameLine.text()

    def focusInEvent(self, event):
        self.step.timeline.selected_index = self.step.index
        print(f"focused on {self.step.name}")
        pal = self.palette()
        pal.setColor(QPalette.Window, QColor("grey"))
        self.setPalette(pal)

    def focusOutEvent(self, event) -> None:
        pal = self.palette()
        pal.setColor(QPalette.Window, QColor(""))


class KeyPressWidget(StepBaseWidget):
    def __init__(self, step: Steps.KeyPress):
        super(KeyPressWidget, self).__init__(step)

        detail_layout = self.ui.detailFrame.layout()

        # Key input
        self.key_label = QLabel("Key: ", self)
        self.key_line_edit = QLineEdit(self)
        self.key_line_edit.setMaxLength(1)
        self.key_line_edit.setText(self.step.key)
        self.key_line_edit.textChanged.connect(self.update_key)

        # Mod Input
        self.mod_label = QLabel("Mod: ", self)
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
        if not self.key_line_edit.text():
            self.key_line_edit.setText(" ")
        self.step.key = self.key_line_edit.text()

    def update_mod(self):
        if self.mod_combo.currentText() == "None":
            self.step.mod = None
        else:
            self.step.mod = self.mod_combo.currentText().lower()


class WaitForImageWidget(StepBaseWidget):
    def __init__(self, step: Steps.WaitForImage):
        super(WaitForImageWidget, self).__init__(step)

        detail_layout: QFormLayout = self.ui.detailFrame.layout()

        # Image selection
        self.image_label = QLabel()
        self.image_button = QPushButton("Select Image")

        # Timeout Input
        self.timeout_spin = QSpinBox()

        # Signal/Slots
        self.timeout_spin.valueChanged.connect(self.update_timeout)
        self.image_button.clicked.connect(self.update_image)

        # Widget insert
        detail_layout.addRow("Image: ", self.image_label)
        detail_layout.addRow("", self.image_button)
        detail_layout.addRow("Timeout: ", self.timeout_spin)

        # Init
        self.image_label.setText(self.step.image)
        self.timeout_spin.setValue(self.step.timeout)

        if not self.image_label.text():
            self.image_label.setText("No image selected")

    def update_image(self):
        file_name = QFileDialog.getOpenFileName(
            parent=None,
            caption="Choose Image to Find",
            dir=self.step.timeline.gm.resource_pool.as_posix(),
            filter="Images (*.png *.jpg)"
        )

        if not file_name:
            print("Canceled selection")
            return

        self.step.image = file_name[0]
        self.image_label.setText(self.step.image)

        if not self.image_label.text():
            self.image_label.setText("No image selected")

    def update_timeout(self):
        self.step.timeout = self.timeout_spin.value()


class DelayWidget(StepBaseWidget):
    def __init__(self, step: Steps.Delay):
        super(DelayWidget, self).__init__(step)

        detail_layout = self.ui.detailFrame.layout()
        self.delay_time = QSpinBox()
        detail_layout.addRow("Delay: ", self.delay_time)

        self.delay_time.valueChanged.connect(self.update_delay)

    def update_delay(self):
        self.step.delay = self.delay_time.value()
