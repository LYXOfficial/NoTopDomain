# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\Phigros\NoTopDomain\libs\UDPAttack.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UDPAttacker(object):
    def setupUi(self, UDPAttacker):
        UDPAttacker.setObjectName("UDPAttacker")
        UDPAttacker.resize(776, 600)
        UDPAttacker.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        UDPAttacker.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(UDPAttacker)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(7)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox333555 = QtWidgets.QGroupBox(UDPAttacker)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox333555.sizePolicy().hasHeightForWidth())
        self.groupBox333555.setSizePolicy(sizePolicy)
        self.groupBox333555.setTitle("")
        self.groupBox333555.setObjectName("groupBox333555")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox333555)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox333555)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox333555, 0, 0, 1, 2)
        self.groupBox_2344 = QtWidgets.QGroupBox(UDPAttacker)
        self.groupBox_2344.setTitle("")
        self.groupBox_2344.setObjectName("groupBox_2344")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2344)
        self.gridLayout_4.setContentsMargins(22, 22, 22, 22)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2344)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_4.addWidget(self.pushButton, 4, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2344)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_4.addWidget(self.pushButton_4, 4, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_2344)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textBrowser.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_4.addWidget(self.textBrowser, 3, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.groupBox_2344)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 2)
        self.gridLayout.addWidget(self.groupBox_2344, 1, 0, 3, 1)
        self.groupBox_33 = QtWidgets.QGroupBox(UDPAttacker)
        self.groupBox_33.setTitle("")
        self.groupBox_33.setObjectName("groupBox_33")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_33)
        self.gridLayout_3.setContentsMargins(22, 22, 22, 22)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_7 = QtWidgets.QLabel(self.groupBox_33)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 4, 0, 1, 1)
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox_33)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy)
        self.textEdit_2.setMaximumSize(QtCore.QSize(16777215, 1677215))
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout_3.addWidget(self.textEdit_2, 5, 0, 1, 2)
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox_33)
        self.spinBox_2.setMinimum(40)
        self.spinBox_2.setMaximum(65535)
        self.spinBox_2.setProperty("value", 4705)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout_3.addWidget(self.spinBox_2, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_33)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_33)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(1145141919)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.label_8 = QtWidgets.QLabel(self.groupBox_33)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.gridLayout_3.addLayout(self.horizontalLayout, 4, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_33)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 2, 0, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox_33)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setMaximumSize(QtCore.QSize(16777215, 1677215))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_3.addWidget(self.plainTextEdit, 6, 0, 1, 2)
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_33)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 16777214))
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_3.addWidget(self.textEdit, 0, 0, 2, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_33)
        self.pushButton_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.spinBox_3 = QtWidgets.QSpinBox(self.groupBox_33)
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(114)
        self.spinBox_3.setObjectName("spinBox_3")
        self.gridLayout_3.addWidget(self.spinBox_3, 3, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_33)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_33, 1, 1, 3, 1)

        self.retranslateUi(UDPAttacker)
        QtCore.QMetaObject.connectSlotsByName(UDPAttacker)

    def retranslateUi(self, UDPAttacker):
        _translate = QtCore.QCoreApplication.translate
        UDPAttacker.setWindowTitle(_translate("UDPAttacker", "极域UDP重放攻击 by ht0Ruial&&modify in NTD"))
        self.label_5.setText(_translate("UDPAttacker", "极域UDP重放攻击 by NoTopDomain"))
        self.pushButton.setText(_translate("UDPAttacker", "发送（&S）"))
        self.pushButton_4.setText(_translate("UDPAttacker", "扫描IP"))
        self.textBrowser.setMarkdown(_translate("UDPAttacker", "日志\n"
"\n"
""))
        self.label.setText(_translate("UDPAttacker", "<html><head/><body><p>警告:此工具利用极域漏洞进行攻击，如使用此工具导致的任何问题作者不承担任何责任！（PS：极域有10秒左右的消息CD，这期间发送消息无效）<br/>注意：为防误触，请按 Alt+S 发送而不是回车<br/><span style=\" color:#808080;\">by ht0Ruial&amp;&amp;modify in NTD</span></p></body></html>"))
        self.label_7.setText(_translate("UDPAttacker", "等待时间"))
        self.textEdit_2.setPlaceholderText(_translate("UDPAttacker", "运行命令（CMD），留空则不发送"))
        self.label_6.setText(_translate("UDPAttacker", "循环次数"))
        self.label_8.setText(_translate("UDPAttacker", "秒"))
        self.label_9.setText(_translate("UDPAttacker", "对方端口（默认4705，不用改）"))
        self.plainTextEdit.setPlaceholderText(_translate("UDPAttacker", "发送消息内容，留空则不发送"))
        self.textEdit.setPlaceholderText(_translate("UDPAttacker", "对方IP（可以使用英文分号隔开）"))
        self.pushButton_2.setText(_translate("UDPAttacker", "对方关机"))
        self.pushButton_3.setText(_translate("UDPAttacker", "对方重启"))
