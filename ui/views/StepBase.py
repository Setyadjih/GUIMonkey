# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StepBase.ui'
##
## Created by: Qt User Interface Compiler version 6.0.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_stepBaseWidget(object):
    def setupUi(self, stepBaseWidget):
        if not stepBaseWidget.objectName():
            stepBaseWidget.setObjectName(u"stepBaseWidget")
        stepBaseWidget.resize(200, 204)
        stepBaseWidget.setMinimumSize(QSize(200, 0))
        stepBaseWidget.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout = QVBoxLayout(stepBaseWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stepNameLine = QLineEdit(stepBaseWidget)
        self.stepNameLine.setObjectName(u"stepNameLine")
        font = QFont()
        font.setPointSize(16)
        self.stepNameLine.setFont(font)
        self.stepNameLine.setCursor(QCursor(Qt.IBeamCursor))
        self.stepNameLine.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.stepNameLine)

        self.line = QFrame(stepBaseWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.detailFrame = QFrame(stepBaseWidget)
        self.detailFrame.setObjectName(u"detailFrame")
        self.detailFrame.setFrameShape(QFrame.StyledPanel)
        self.detailFrame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.detailFrame)
        self.formLayout.setObjectName(u"formLayout")

        self.verticalLayout.addWidget(self.detailFrame)


        self.retranslateUi(stepBaseWidget)

        QMetaObject.connectSlotsByName(stepBaseWidget)
    # setupUi

    def retranslateUi(self, stepBaseWidget):
        stepBaseWidget.setWindowTitle(QCoreApplication.translate("stepBaseWidget", u"Form", None))
        self.stepNameLine.setText(QCoreApplication.translate("stepBaseWidget", u"Step Name", None))
    # retranslateUi

