# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\Phigros\NoTopDomain\libs\NTD.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NoTopDomain(object):
    def setupUi(self, NoTopDomain):
        NoTopDomain.setObjectName("NoTopDomain")
        NoTopDomain.resize(345, 413)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(9)
        NoTopDomain.setFont(font)
        self.centralwidget = QtWidgets.QWidget(NoTopDomain)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.PigeonGames = QtWidgets.QTabWidget(self.centralwidget)
        self.PigeonGames.setObjectName("PigeonGames")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setVerticalSpacing(7)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.GBWindowed = QtWidgets.QPushButton(self.groupBox)
        self.GBWindowed.setEnabled(False)
        self.GBWindowed.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.GBWindowed.setAutoDefault(False)
        self.GBWindowed.setFlat(False)
        self.GBWindowed.setObjectName("GBWindowed")
        self.gridLayout_2.addWidget(self.GBWindowed, 1, 1, 1, 1)
        self.CopyLink = QtWidgets.QPushButton(self.groupBox)
        self.CopyLink.setObjectName("CopyLink")
        self.gridLayout_2.addWidget(self.CopyLink, 1, 0, 1, 1)
        self.KillTD = QtWidgets.QPushButton(self.groupBox)
        self.KillTD.setMinimumSize(QtCore.QSize(100, 0))
        self.KillTD.setObjectName("KillTD")
        self.gridLayout_2.addWidget(self.KillTD, 0, 0, 1, 1)
        self.HangUpTD = QtWidgets.QPushButton(self.groupBox)
        self.HangUpTD.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HangUpTD.sizePolicy().hasHeightForWidth())
        self.HangUpTD.setSizePolicy(sizePolicy)
        self.HangUpTD.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.HangUpTD.setObjectName("HangUpTD")
        self.gridLayout_2.addWidget(self.HangUpTD, 0, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_2.addWidget(self.pushButton_6, 0, 2, 1, 2)
        self.KillSome = QtWidgets.QLineEdit(self.groupBox)
        self.KillSome.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.KillSome.sizePolicy().hasHeightForWidth())
        self.KillSome.setSizePolicy(sizePolicy)
        self.KillSome.setMinimumSize(QtCore.QSize(0, 0))
        self.KillSome.setMaximumSize(QtCore.QSize(120, 16777215))
        self.KillSome.setObjectName("KillSome")
        self.gridLayout_2.addWidget(self.KillSome, 1, 2, 1, 2)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(2, 1)
        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 1, 0, 1, 4)
        self.UninstallTopDomain = QtWidgets.QPushButton(self.tab)
        self.UninstallTopDomain.setEnabled(False)
        self.UninstallTopDomain.setObjectName("UninstallTopDomain")
        self.gridLayout_4.addWidget(self.UninstallTopDomain, 3, 2, 1, 1)
        self.StudentRunning = QtWidgets.QLabel(self.tab)
        self.StudentRunning.setMinimumSize(QtCore.QSize(150, 0))
        self.StudentRunning.setObjectName("StudentRunning")
        self.gridLayout_4.addWidget(self.StudentRunning, 0, 1, 1, 1)
        self.TDPasswd = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TDPasswd.sizePolicy().hasHeightForWidth())
        self.TDPasswd.setSizePolicy(sizePolicy)
        self.TDPasswd.setReadOnly(True)
        self.TDPasswd.setObjectName("TDPasswd")
        self.gridLayout_4.addWidget(self.TDPasswd, 3, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setSpacing(3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.NoImg = QtWidgets.QPushButton(self.groupBox_2)
        self.NoImg.setObjectName("NoImg")
        self.gridLayout_3.addWidget(self.NoImg, 4, 3, 1, 1)
        self.ToolsYes = QtWidgets.QPushButton(self.groupBox_2)
        self.ToolsYes.setObjectName("ToolsYes")
        self.gridLayout_3.addWidget(self.ToolsYes, 4, 1, 1, 1)
        self.WebsiteYes = QtWidgets.QCheckBox(self.groupBox_2)
        self.WebsiteYes.setObjectName("WebsiteYes")
        self.gridLayout_3.addWidget(self.WebsiteYes, 1, 3, 1, 1)
        self.NoBlackScreen = QtWidgets.QCheckBox(self.groupBox_2)
        self.NoBlackScreen.setObjectName("NoBlackScreen")
        self.gridLayout_3.addWidget(self.NoBlackScreen, 2, 1, 1, 1)
        self.NoKill = QtWidgets.QCheckBox(self.groupBox_2)
        self.NoKill.setObjectName("NoKill")
        self.gridLayout_3.addWidget(self.NoKill, 3, 3, 1, 1)
        self.NoShutdown = QtWidgets.QCheckBox(self.groupBox_2)
        self.NoShutdown.setObjectName("NoShutdown")
        self.gridLayout_3.addWidget(self.NoShutdown, 2, 3, 1, 1)
        self.IamTop = QtWidgets.QCheckBox(self.groupBox_2)
        self.IamTop.setObjectName("IamTop")
        self.gridLayout_3.addWidget(self.IamTop, 0, 1, 1, 1)
        self.MouseYes = QtWidgets.QCheckBox(self.groupBox_2)
        self.MouseYes.setObjectName("MouseYes")
        self.gridLayout_3.addWidget(self.MouseYes, 0, 5, 1, 1)
        self.KeyboardYes = QtWidgets.QCheckBox(self.groupBox_2)
        self.KeyboardYes.setObjectName("KeyboardYes")
        self.gridLayout_3.addWidget(self.KeyboardYes, 0, 3, 1, 1)
        self.USBYes = QtWidgets.QCheckBox(self.groupBox_2)
        self.USBYes.setObjectName("USBYes")
        self.gridLayout_3.addWidget(self.USBYes, 1, 1, 1, 1)
        self.UnlockTDHook = QtWidgets.QCheckBox(self.groupBox_2)
        self.UnlockTDHook.setObjectName("UnlockTDHook")
        self.gridLayout_3.addWidget(self.UnlockTDHook, 1, 5, 1, 1)
        self.NoRemoteRun = QtWidgets.QCheckBox(self.groupBox_2)
        self.NoRemoteRun.setObjectName("NoRemoteRun")
        self.gridLayout_3.addWidget(self.NoRemoteRun, 3, 1, 1, 1)
        self.RestartExplorer = QtWidgets.QPushButton(self.groupBox_2)
        self.RestartExplorer.setObjectName("RestartExplorer")
        self.gridLayout_3.addWidget(self.RestartExplorer, 4, 5, 1, 1)
        self.NoMontior = QtWidgets.QCheckBox(self.groupBox_2)
        self.NoMontior.setObjectName("NoMontior")
        self.gridLayout_3.addWidget(self.NoMontior, 3, 5, 1, 1)
        self.NoControl = QtWidgets.QCheckBox(self.groupBox_2)
        self.NoControl.setObjectName("NoControl")
        self.gridLayout_3.addWidget(self.NoControl, 2, 5, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 2, 0, 1, 4)
        self.GBing = QtWidgets.QLabel(self.tab)
        self.GBing.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.GBing.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.GBing.setObjectName("GBing")
        self.gridLayout_4.addWidget(self.GBing, 0, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 3, 1, 1)
        self.PigeonGames.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_6.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_4.setFlat(False)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSpacing(4)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.showWindowHotKey = QtWidgets.QLineEdit(self.groupBox_4)
        self.showWindowHotKey.setObjectName("showWindowHotKey")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.showWindowHotKey)
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.killFocusHotKey = QtWidgets.QLineEdit(self.groupBox_4)
        self.killFocusHotKey.setObjectName("killFocusHotKey")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.killFocusHotKey)
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.GBWindowSwitchHotKey = QtWidgets.QLineEdit(self.groupBox_4)
        self.GBWindowSwitchHotKey.setObjectName("GBWindowSwitchHotKey")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.GBWindowSwitchHotKey)
        self.horizontalLayout.addLayout(self.formLayout)
        self.line = QtWidgets.QFrame(self.groupBox_4)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setSpacing(4)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.TSKHotKey = QtWidgets.QLineEdit(self.groupBox_4)
        self.TSKHotKey.setObjectName("TSKHotKey")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.TSKHotKey)
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.topFocusHotKey = QtWidgets.QLineEdit(self.groupBox_4)
        self.topFocusHotKey.setObjectName("topFocusHotKey")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.topFocusHotKey)
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.ForceFullHotKey = QtWidgets.QLineEdit(self.groupBox_4)
        self.ForceFullHotKey.setObjectName("ForceFullHotKey")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ForceFullHotKey)
        self.horizontalLayout.addLayout(self.formLayout_2)
        self.gridLayout_6.addWidget(self.groupBox_4, 3, 0, 1, 2)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_6.addWidget(self.pushButton_2, 8, 0, 1, 1)
        self.reStart = QtWidgets.QPushButton(self.tab_3)
        self.reStart.setObjectName("reStart")
        self.gridLayout_6.addWidget(self.reStart, 8, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem, 4, 0, 1, 2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setHorizontalSpacing(0)
        self.gridLayout_5.setVerticalSpacing(2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_5.addWidget(self.checkBox, 1, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_5.addWidget(self.radioButton)
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_3.setEnabled(True)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_5.addWidget(self.radioButton_3)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_5.addWidget(self.radioButton_2)
        self.gridLayout_5.addLayout(self.horizontalLayout_5, 9, 0, 1, 3)
        self.label_17 = QtWidgets.QLabel(self.groupBox_3)
        self.label_17.setObjectName("label_17")
        self.gridLayout_5.addWidget(self.label_17, 8, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_5.addWidget(self.checkBox_2, 2, 0, 1, 2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_5.addWidget(self.checkBox_3, 1, 1, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_4.setChecked(False)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_5.addWidget(self.checkBox_4, 1, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setObjectName("label_16")
        self.gridLayout_5.addWidget(self.label_16, 7, 0, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout_5.addWidget(self.checkBox_5, 2, 2, 1, 1)
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox_3)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout_5.addWidget(self.horizontalSlider, 7, 1, 1, 2)
        self.gridLayout_6.addWidget(self.groupBox_3, 0, 0, 1, 2)
        self.PigeonGames.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.progressBar = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_7.addWidget(self.progressBar, 7, 0, 1, 3)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_7.addWidget(self.plainTextEdit, 3, 0, 1, 3)
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout_7.addWidget(self.label_13, 5, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.tab_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_7.addWidget(self.line_2, 1, 0, 1, 3)
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_7.addWidget(self.label_10, 0, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_7.addWidget(self.label_9, 0, 0, 1, 2)
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setOpenExternalLinks(True)
        self.label_14.setObjectName("label_14")
        self.gridLayout_7.addWidget(self.label_14, 4, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.tab_2)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_2.addWidget(self.label_15)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.gridLayout_7.addWidget(self.widget, 8, 0, 1, 3)
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_7.addWidget(self.label_12, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setEnabled(False)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_7.addWidget(self.pushButton, 6, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setEnabled(False)
        self.label_11.setObjectName("label_11")
        self.gridLayout_7.addWidget(self.label_11, 6, 0, 1, 1)
        self.PigeonGames.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_5)
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.PigeonGames.addTab(self.tab_5, "")
        self.gridLayout.addWidget(self.PigeonGames, 0, 0, 1, 2)
        NoTopDomain.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NoTopDomain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 345, 23))
        self.menubar.setObjectName("menubar")
        NoTopDomain.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NoTopDomain)
        self.statusbar.setObjectName("statusbar")
        NoTopDomain.setStatusBar(self.statusbar)
        self.action1 = QtWidgets.QAction(NoTopDomain)
        self.action1.setObjectName("action1")
        self.action_1 = QtWidgets.QAction(NoTopDomain)
        self.action_1.setObjectName("action_1")
        self.action_2 = QtWidgets.QAction(NoTopDomain)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(NoTopDomain)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(NoTopDomain)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(NoTopDomain)
        self.action_5.setObjectName("action_5")

        self.retranslateUi(NoTopDomain)
        self.PigeonGames.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(NoTopDomain)

    def retranslateUi(self, NoTopDomain):
        _translate = QtCore.QCoreApplication.translate
        NoTopDomain.setWindowTitle(_translate("NoTopDomain", "NoTopDomain"))
        self.groupBox.setTitle(_translate("NoTopDomain", "常用功能"))
        self.GBWindowed.setText(_translate("NoTopDomain", "解冻全屏"))
        self.CopyLink.setText(_translate("NoTopDomain", "复制极域链接"))
        self.KillTD.setText(_translate("NoTopDomain", "杀掉极域！！"))
        self.HangUpTD.setText(_translate("NoTopDomain", "挂起极域"))
        self.pushButton_6.setText(_translate("NoTopDomain", "监视图片替换"))
        self.KillSome.setPlaceholderText(_translate("NoTopDomain", "杀掉输入进程"))
        self.UninstallTopDomain.setText(_translate("NoTopDomain", "卸载极域"))
        self.StudentRunning.setText(_translate("NoTopDomain", "极域：<span style=\"color:grey\">检测中</span>"))
        self.TDPasswd.setPlaceholderText(_translate("NoTopDomain", "尝试获取密码..."))
        self.groupBox_2.setTitle(_translate("NoTopDomain", "限制解除"))
        self.NoImg.setText(_translate("NoTopDomain", "解除映像劫持"))
        self.ToolsYes.setText(_translate("NoTopDomain", "解工具/限制"))
        self.WebsiteYes.setText(_translate("NoTopDomain", "解除网站限制"))
        self.NoBlackScreen.setText(_translate("NoTopDomain", "屏蔽黑屏安静"))
        self.NoKill.setText(_translate("NoTopDomain", "拦截杀掉进程"))
        self.NoShutdown.setText(_translate("NoTopDomain", "脱离远程关机"))
        self.IamTop.setText(_translate("NoTopDomain", "置顶窗口"))
        self.MouseYes.setText(_translate("NoTopDomain", "解除鼠标限制"))
        self.KeyboardYes.setText(_translate("NoTopDomain", "解除键盘限制"))
        self.USBYes.setText(_translate("NoTopDomain", "U盘/软件限制"))
        self.UnlockTDHook.setText(_translate("NoTopDomain", "解除极域防杀"))
        self.NoRemoteRun.setText(_translate("NoTopDomain", "拦截远程运行"))
        self.RestartExplorer.setText(_translate("NoTopDomain", "重启资源管理器"))
        self.NoMontior.setText(_translate("NoTopDomain", "拦截教师监控"))
        self.NoControl.setText(_translate("NoTopDomain", "拦截传入连接"))
        self.GBing.setText(_translate("NoTopDomain", "广播：<span style=\"color:grey\">检测中</span>"))
        self.PigeonGames.setTabText(self.PigeonGames.indexOf(self.tab), _translate("NoTopDomain", "极域"))
        self.groupBox_4.setTitle(_translate("NoTopDomain", "快捷键配置"))
        self.label.setText(_translate("NoTopDomain", "唤起窗口"))
        self.label_4.setText(_translate("NoTopDomain", "杀掉当前窗口"))
        self.label_7.setText(_translate("NoTopDomain", "窗口化切换"))
        self.label_2.setText(_translate("NoTopDomain", "隐藏当前窗口"))
        self.label_3.setText(_translate("NoTopDomain", "置顶当前窗口"))
        self.label_8.setText(_translate("NoTopDomain", "恢复广播全屏"))
        self.pushButton_2.setText(_translate("NoTopDomain", "保存"))
        self.reStart.setText(_translate("NoTopDomain", "重启程序以应用设置"))
        self.groupBox_3.setTitle(_translate("NoTopDomain", "基础设置"))
        self.checkBox.setText(_translate("NoTopDomain", "隐藏托盘"))
        self.radioButton.setText(_translate("NoTopDomain", "TermProc"))
        self.radioButton_3.setText(_translate("NoTopDomain", "TermThr"))
        self.radioButton_2.setText(_translate("NoTopDomain", "ntsd.exe"))
        self.label_17.setText(_translate("NoTopDomain", "杀进程方案:"))
        self.checkBox_2.setText(_translate("NoTopDomain", "修改窗口化时自缩放"))
        self.checkBox_3.setText(_translate("NoTopDomain", "禁用QSS"))
        self.checkBox_4.setText(_translate("NoTopDomain", "允许教师截屏"))
        self.label_16.setText(_translate("NoTopDomain", "窗口透明度"))
        self.checkBox_5.setText(_translate("NoTopDomain", "禁用随机窗口名"))
        self.PigeonGames.setTabText(self.PigeonGames.indexOf(self.tab_3), _translate("NoTopDomain", "设置"))
        self.plainTextEdit.setPlainText(_translate("NoTopDomain", "获取中..."))
        self.label_13.setText(_translate("NoTopDomain", "更新包信息："))
        self.label_10.setText(_translate("NoTopDomain", "当前版本："))
        self.label_9.setText(_translate("NoTopDomain", "最新版本：获取中..."))
        self.label_14.setText(_translate("NoTopDomain", "<a href=\"https://github.com/lyxofficial/NoTopDomain/releases\">查看历史版本</a>"))
        self.label_15.setText(_translate("NoTopDomain", "新版下载完毕"))
        self.pushButton_3.setText(_translate("NoTopDomain", "重启并应用更新"))
        self.pushButton_4.setText(_translate("NoTopDomain", "打开下载位置"))
        self.label_12.setText(_translate("NoTopDomain", "更新日志："))
        self.pushButton.setText(_translate("NoTopDomain", "下载更新包"))
        self.label_11.setText(_translate("NoTopDomain", "大小：获取中..."))
        self.PigeonGames.setTabText(self.PigeonGames.indexOf(self.tab_2), _translate("NoTopDomain", "更新"))
        self.PigeonGames.setTabText(self.PigeonGames.indexOf(self.tab_5), _translate("NoTopDomain", "帮助"))
        self.action1.setText(_translate("NoTopDomain", "1"))
        self.action_1.setText(_translate("NoTopDomain", "关于"))
        self.action_2.setText(_translate("NoTopDomain", "设置"))
        self.action_3.setText(_translate("NoTopDomain", "启动TSK"))
        self.action_4.setText(_translate("NoTopDomain", "运行..."))
        self.action_5.setText(_translate("NoTopDomain", "映像劫持"))
