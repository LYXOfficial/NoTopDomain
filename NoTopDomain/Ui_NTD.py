# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\NoTopDomain\NTD.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NoTopDomain(object):
    def setupUi(self, NoTopDomain):
        NoTopDomain.setObjectName("NoTopDomain")
        NoTopDomain.resize(471, 447)
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
        self.gridLayout_4.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.StudentRunning = QtWidgets.QLabel(self.tab)
        self.StudentRunning.setObjectName("StudentRunning")
        self.gridLayout_4.addWidget(self.StudentRunning, 0, 0, 1, 1)
        self.GBing = QtWidgets.QLabel(self.tab)
        self.GBing.setObjectName("GBing")
        self.gridLayout_4.addWidget(self.GBing, 0, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.KillCurrent = QtWidgets.QPushButton(self.groupBox)
        self.KillCurrent.setObjectName("KillCurrent")
        self.gridLayout_2.addWidget(self.KillCurrent, 0, 2, 1, 1)
        self.GBWindowed = QtWidgets.QPushButton(self.groupBox)
        self.GBWindowed.setObjectName("GBWindowed")
        self.gridLayout_2.addWidget(self.GBWindowed, 1, 0, 1, 1)
        self.NoPin = QtWidgets.QPushButton(self.groupBox)
        self.NoPin.setObjectName("NoPin")
        self.gridLayout_2.addWidget(self.NoPin, 1, 2, 1, 1)
        self.KillTD = QtWidgets.QPushButton(self.groupBox)
        self.KillTD.setObjectName("KillTD")
        self.gridLayout_2.addWidget(self.KillTD, 0, 7, 1, 6)
        self.HangUpTD = QtWidgets.QPushButton(self.groupBox)
        self.HangUpTD.setObjectName("HangUpTD")
        self.gridLayout_2.addWidget(self.HangUpTD, 0, 0, 1, 1)
        self.TDPwd = QtWidgets.QLineEdit(self.groupBox)
        self.TDPwd.setEnabled(True)
        self.TDPwd.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.TDPwd.setReadOnly(True)
        self.TDPwd.setObjectName("TDPwd")
        self.gridLayout_2.addWidget(self.TDPwd, 1, 7, 1, 6)
        self.gridLayout_4.addWidget(self.groupBox, 1, 0, 1, 2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ForYourSafety = QtWidgets.QCheckBox(self.groupBox_2)
        self.ForYourSafety.setObjectName("ForYourSafety")
        self.gridLayout_3.addWidget(self.ForYourSafety, 3, 0, 1, 1)
        self.TSKYes = QtWidgets.QPushButton(self.groupBox_2)
        self.TSKYes.setObjectName("TSKYes")
        self.gridLayout_3.addWidget(self.TSKYes, 4, 1, 1, 1)
        self.AppsYes = QtWidgets.QCheckBox(self.groupBox_2)
        self.AppsYes.setObjectName("AppsYes")
        self.gridLayout_3.addWidget(self.AppsYes, 2, 1, 1, 1)
        self.WebsiteYes = QtWidgets.QCheckBox(self.groupBox_2)
        self.WebsiteYes.setObjectName("WebsiteYes")
        self.gridLayout_3.addWidget(self.WebsiteYes, 2, 0, 1, 1)
        self.RegEditYes = QtWidgets.QPushButton(self.groupBox_2)
        self.RegEditYes.setObjectName("RegEditYes")
        self.gridLayout_3.addWidget(self.RegEditYes, 4, 0, 1, 1)
        self.CMDYes = QtWidgets.QPushButton(self.groupBox_2)
        self.CMDYes.setObjectName("CMDYes")
        self.gridLayout_3.addWidget(self.CMDYes, 3, 1, 1, 1)
        self.USBYes = QtWidgets.QCheckBox(self.groupBox_2)
        self.USBYes.setObjectName("USBYes")
        self.gridLayout_3.addWidget(self.USBYes, 0, 2, 1, 2)
        self.MouseYes = QtWidgets.QCheckBox(self.groupBox_2)
        self.MouseYes.setObjectName("MouseYes")
        self.gridLayout_3.addWidget(self.MouseYes, 0, 0, 1, 1)
        self.KeyboardYes = QtWidgets.QCheckBox(self.groupBox_2)
        self.KeyboardYes.setObjectName("KeyboardYes")
        self.gridLayout_3.addWidget(self.KeyboardYes, 0, 1, 1, 1)
        self.NoGBHP = QtWidgets.QCheckBox(self.groupBox_2)
        self.NoGBHP.setObjectName("NoGBHP")
        self.gridLayout_3.addWidget(self.NoGBHP, 2, 2, 1, 2)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_3.addWidget(self.pushButton_5, 3, 2, 1, 2)
        self.NoRes = QtWidgets.QPushButton(self.groupBox_2)
        self.NoRes.setObjectName("NoRes")
        self.gridLayout_3.addWidget(self.NoRes, 4, 2, 1, 2)
        self.gridLayout_4.addWidget(self.groupBox_2, 2, 0, 1, 2)
        self.WhereIsMyFile = QtWidgets.QPushButton(self.tab)
        self.WhereIsMyFile.setObjectName("WhereIsMyFile")
        self.gridLayout_4.addWidget(self.WhereIsMyFile, 3, 0, 1, 2)
        self.PigeonGames.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.PhigrosChapter9 = QtWidgets.QLabel(self.tab_2)
        self.PhigrosChapter9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PhigrosChapter9.setAlignment(QtCore.Qt.AlignCenter)
        self.PhigrosChapter9.setObjectName("PhigrosChapter9")
        self.gridLayout_5.addWidget(self.PhigrosChapter9, 0, 0, 1, 1)
        self.PigeonGames.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.PigeonGames, 0, 0, 1, 1)
        NoTopDomain.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NoTopDomain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 471, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
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
        self.menu.addAction(self.action_1)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_4)
        self.menu.addAction(self.action_5)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(NoTopDomain)
        self.PigeonGames.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(NoTopDomain)

    def retranslateUi(self, NoTopDomain):
        _translate = QtCore.QCoreApplication.translate
        NoTopDomain.setWindowTitle(_translate("NoTopDomain", "NoTopDomain v0.01 By LYX"))
        self.StudentRunning.setText(_translate("NoTopDomain", "极域：<span style=\"color:grey\">检测中</span>"))
        self.GBing.setText(_translate("NoTopDomain", "广播：<span style=\"color:grey\">检测中</span>"))
        self.groupBox.setTitle(_translate("NoTopDomain", "常用功能"))
        self.KillCurrent.setText(_translate("NoTopDomain", "强制杀掉选择程序"))
        self.GBWindowed.setText(_translate("NoTopDomain", "解冻全屏"))
        self.NoPin.setText(_translate("NoTopDomain", "取消选中焦点"))
        self.KillTD.setText(_translate("NoTopDomain", "杀掉极域！！！"))
        self.HangUpTD.setText(_translate("NoTopDomain", "挂起极域"))
        self.TDPwd.setInputMask(_translate("NoTopDomain", "尝试获取密码..."))
        self.TDPwd.setText(_translate("NoTopDomain", "尝试获取密码..."))
        self.groupBox_2.setTitle(_translate("NoTopDomain", "限制解除（部分需要在连接前解除，可以拔掉网线重启电脑）"))
        self.ForYourSafety.setText(_translate("NoTopDomain", "伪装教师端连接"))
        self.TSKYes.setText(_translate("NoTopDomain", "解禁任务管理器"))
        self.AppsYes.setText(_translate("NoTopDomain", "解除应用限制"))
        self.WebsiteYes.setText(_translate("NoTopDomain", "解除网站限制"))
        self.RegEditYes.setText(_translate("NoTopDomain", "解禁注册表编辑器"))
        self.CMDYes.setText(_translate("NoTopDomain", "解禁CMD"))
        self.USBYes.setText(_translate("NoTopDomain", "解除USB限制"))
        self.MouseYes.setText(_translate("NoTopDomain", "解除鼠标限制"))
        self.KeyboardYes.setText(_translate("NoTopDomain", "解除键盘限制"))
        self.NoGBHP.setText(_translate("NoTopDomain", "屏蔽广播/黑屏安静"))
        self.pushButton_5.setText(_translate("NoTopDomain", "解禁Ctrl+Alt+Del"))
        self.NoRes.setText(_translate("NoTopDomain", "尝试破解还原卡"))
        self.WhereIsMyFile.setText(_translate("NoTopDomain", "接收遗漏文件"))
        self.PigeonGames.setTabText(self.PigeonGames.indexOf(self.tab), _translate("NoTopDomain", "极域"))
        self.PhigrosChapter9.setText(_translate("NoTopDomain", "咕咕咕！（傲娇）"))
        self.PigeonGames.setTabText(self.PigeonGames.indexOf(self.tab_2), _translate("NoTopDomain", "学生机房管理助手"))
        self.menu.setTitle(_translate("NoTopDomain", "项目（也许有你需要的）"))
        self.action1.setText(_translate("NoTopDomain", "1"))
        self.action_1.setText(_translate("NoTopDomain", "关于"))
        self.action_2.setText(_translate("NoTopDomain", "设置"))
        self.action_3.setText(_translate("NoTopDomain", "启动TSK"))
        self.action_4.setText(_translate("NoTopDomain", "运行..."))
        self.action_5.setText(_translate("NoTopDomain", "映像劫持"))
