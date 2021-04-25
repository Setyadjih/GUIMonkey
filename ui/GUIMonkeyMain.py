# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUIMonkeyMain.ui'
##
## Created by: Qt User Interface Compiler version 6.0.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_GUIMonkeyMain(object):
    def setupUi(self, GUIMonkeyMain):
        if not GUIMonkeyMain.objectName():
            GUIMonkeyMain.setObjectName(u"GUIMonkeyMain")
        GUIMonkeyMain.resize(800, 600)
        self.actionNew_Timeline = QAction(GUIMonkeyMain)
        self.actionNew_Timeline.setObjectName(u"actionNew_Timeline")
        self.actionOpen = QAction(GUIMonkeyMain)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionRecents = QAction(GUIMonkeyMain)
        self.actionRecents.setObjectName(u"actionRecents")
        self.centralwidget = QWidget(GUIMonkeyMain)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.TimelineList = QListWidget(self.centralwidget)
        self.TimelineList.setObjectName(u"TimelineList")

        self.horizontalLayout.addWidget(self.TimelineList)

        self.ControlsFrame = QFrame(self.centralwidget)
        self.ControlsFrame.setObjectName(u"ControlsFrame")
        self.ControlsFrame.setMinimumSize(QSize(600, 0))
        self.ControlsFrame.setFrameShape(QFrame.StyledPanel)
        self.ControlsFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.ControlsFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.RemoveStepButton = QPushButton(self.ControlsFrame)
        self.RemoveStepButton.setObjectName(u"RemoveStepButton")

        self.gridLayout.addWidget(self.RemoveStepButton, 0, 1, 1, 1)

        self.AddStepButton = QPushButton(self.ControlsFrame)
        self.AddStepButton.setObjectName(u"AddStepButton")

        self.gridLayout.addWidget(self.AddStepButton, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.ControlsFrame)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)


        self.horizontalLayout.addWidget(self.ControlsFrame)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.TimelineScroll = QWidget()
        self.TimelineScroll.setObjectName(u"TimelineScroll")
        self.TimelineScroll.setGeometry(QRect(0, 0, 780, 264))
        self.scrollArea.setWidget(self.TimelineScroll)

        self.verticalLayout.addWidget(self.scrollArea)

        GUIMonkeyMain.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(GUIMonkeyMain)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        GUIMonkeyMain.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(GUIMonkeyMain)
        self.statusbar.setObjectName(u"statusbar")
        GUIMonkeyMain.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionNew_Timeline)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionRecents)

        self.retranslateUi(GUIMonkeyMain)

        QMetaObject.connectSlotsByName(GUIMonkeyMain)
    # setupUi

    def retranslateUi(self, GUIMonkeyMain):
        GUIMonkeyMain.setWindowTitle(QCoreApplication.translate("GUIMonkeyMain", u"GUI Monkey", None))
        self.actionNew_Timeline.setText(QCoreApplication.translate("GUIMonkeyMain", u"New Timeline", None))
        self.actionOpen.setText(QCoreApplication.translate("GUIMonkeyMain", u"Open..", None))
        self.actionRecents.setText(QCoreApplication.translate("GUIMonkeyMain", u"Recents", None))
        self.RemoveStepButton.setText(QCoreApplication.translate("GUIMonkeyMain", u"Remove Step", None))
        self.AddStepButton.setText(QCoreApplication.translate("GUIMonkeyMain", u"Add Step", None))
        self.pushButton.setText(QCoreApplication.translate("GUIMonkeyMain", u"Execute", None))
        self.menuFile.setTitle(QCoreApplication.translate("GUIMonkeyMain", u"File", None))
    # retranslateUi

