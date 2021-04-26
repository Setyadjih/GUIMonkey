# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreateTimelineDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.0.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_createTimelineDialog(object):
    def setupUi(self, createTimelineDialog):
        if not createTimelineDialog.objectName():
            createTimelineDialog.setObjectName(u"createTimelineDialog")
        createTimelineDialog.resize(217, 95)
        self.verticalLayout = QVBoxLayout(createTimelineDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.nameLabel = QLabel(createTimelineDialog)
        self.nameLabel.setObjectName(u"nameLabel")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameLabel.sizePolicy().hasHeightForWidth())
        self.nameLabel.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.nameLabel)

        self.timelineNameLine = QLineEdit(createTimelineDialog)
        self.timelineNameLine.setObjectName(u"timelineNameLine")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.timelineNameLine)

        self.sourceLabel = QLabel(createTimelineDialog)
        self.sourceLabel.setObjectName(u"sourceLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sourceLabel.sizePolicy().hasHeightForWidth())
        self.sourceLabel.setSizePolicy(sizePolicy1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.sourceLabel)

        self.timelineSourceLine = QLineEdit(createTimelineDialog)
        self.timelineSourceLine.setObjectName(u"timelineSourceLine")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.timelineSourceLine)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonBox = QDialogButtonBox(createTimelineDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(createTimelineDialog)
        self.buttonBox.accepted.connect(createTimelineDialog.accept)
        self.buttonBox.rejected.connect(createTimelineDialog.reject)

        QMetaObject.connectSlotsByName(createTimelineDialog)
    # setupUi

    def retranslateUi(self, createTimelineDialog):
        createTimelineDialog.setWindowTitle(QCoreApplication.translate("createTimelineDialog", u"Create Timeline", None))
        self.nameLabel.setText(QCoreApplication.translate("createTimelineDialog", u"Name", None))
        self.sourceLabel.setText(QCoreApplication.translate("createTimelineDialog", u"Source", None))
        self.timelineSourceLine.setText("")
    # retranslateUi

