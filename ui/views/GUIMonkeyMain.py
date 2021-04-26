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
        self.openAction = QAction(GUIMonkeyMain)
        self.openAction.setObjectName(u"openAction")
        self.recentsAction = QAction(GUIMonkeyMain)
        self.recentsAction.setObjectName(u"recentsAction")
        self.deleteTimelineAction = QAction(GUIMonkeyMain)
        self.deleteTimelineAction.setObjectName(u"deleteTimelineAction")
        self.centralwidget = QWidget(GUIMonkeyMain)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.addTimelineButton = QPushButton(self.centralwidget)
        self.addTimelineButton.setObjectName(u"addTimelineButton")

        self.gridLayout_2.addWidget(self.addTimelineButton, 1, 0, 1, 1)

        self.timelineList = QListWidget(self.centralwidget)
        self.timelineList.setObjectName(u"timelineList")
        self.timelineList.setContextMenuPolicy(Qt.ActionsContextMenu)

        self.gridLayout_2.addWidget(self.timelineList, 2, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_2)

        self.ControlsFrame = QFrame(self.centralwidget)
        self.ControlsFrame.setObjectName(u"ControlsFrame")
        self.ControlsFrame.setMinimumSize(QSize(600, 0))
        self.ControlsFrame.setFrameShape(QFrame.StyledPanel)
        self.ControlsFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.ControlsFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.removeStepButton = QPushButton(self.ControlsFrame)
        self.removeStepButton.setObjectName(u"removeStepButton")

        self.gridLayout.addWidget(self.removeStepButton, 0, 1, 1, 1)

        self.addStepButton = QPushButton(self.ControlsFrame)
        self.addStepButton.setObjectName(u"addStepButton")

        self.gridLayout.addWidget(self.addStepButton, 0, 0, 1, 1)

        self.executeButton = QPushButton(self.ControlsFrame)
        self.executeButton.setObjectName(u"executeButton")

        self.gridLayout.addWidget(self.executeButton, 1, 1, 1, 1)


        self.horizontalLayout.addWidget(self.ControlsFrame)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.timelineScroll = QWidget()
        self.timelineScroll.setObjectName(u"timelineScroll")
        self.timelineScroll.setGeometry(QRect(0, 0, 780, 265))
        self.horizontalLayout_2 = QHBoxLayout(self.timelineScroll)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.scrollArea.setWidget(self.timelineScroll)

        self.verticalLayout.addWidget(self.scrollArea)

        GUIMonkeyMain.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(GUIMonkeyMain)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        GUIMonkeyMain.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(GUIMonkeyMain)
        self.statusbar.setObjectName(u"statusbar")
        GUIMonkeyMain.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.openAction)
        self.menuFile.addAction(self.recentsAction)

        self.retranslateUi(GUIMonkeyMain)

        QMetaObject.connectSlotsByName(GUIMonkeyMain)
    # setupUi

    def retranslateUi(self, GUIMonkeyMain):
        GUIMonkeyMain.setWindowTitle(QCoreApplication.translate("GUIMonkeyMain", u"GUI Monkey", None))
        self.openAction.setText(QCoreApplication.translate("GUIMonkeyMain", u"Open..", None))
        self.recentsAction.setText(QCoreApplication.translate("GUIMonkeyMain", u"Recents", None))
        self.deleteTimelineAction.setText(QCoreApplication.translate("GUIMonkeyMain", u"Delete Timeline", None))
#if QT_CONFIG(tooltip)
        self.deleteTimelineAction.setToolTip(QCoreApplication.translate("GUIMonkeyMain", u"Delete the selected Timeline", None))
#endif // QT_CONFIG(tooltip)
        self.addTimelineButton.setText(QCoreApplication.translate("GUIMonkeyMain", u"Add Timeline", None))
        self.removeStepButton.setText(QCoreApplication.translate("GUIMonkeyMain", u"Remove Step", None))
        self.addStepButton.setText(QCoreApplication.translate("GUIMonkeyMain", u"Add Step", None))
        self.executeButton.setText(QCoreApplication.translate("GUIMonkeyMain", u"Execute", None))
        self.menuFile.setTitle(QCoreApplication.translate("GUIMonkeyMain", u"File", None))
    # retranslateUi

