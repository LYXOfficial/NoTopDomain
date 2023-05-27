from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from threading import *
import sys,base64
import datetime
from . import mail,b64,Ui_feedback
class Feedbacker(QWidget,Ui_feedback.Ui_feedbacker):
    ok=pyqtSignal()
    fail=pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setup()
    def Ok(self):
        QMessageBox.information(self,"提示","发送成功啦！")
        self.close()
    def Fail(self):
        QMessageBox.warning(self,"QwQ","发送失败了...要不去交Issue吧（")
        self.pushButton_2.setText("发送反馈")
        self.pushButton_2.setEnabled(1)
        self.lineEdit.setEnabled(1)
        self.lineEdit_2.setEnabled(1)
        self.textEdit.setEnabled(1)
    def setup(self):
        self.ok.connect(self.Ok)
        self.fail.connect(self.Fail)
        self.icon=QPixmap()
        self.icon.loadFromData(base64.b64decode(b64.icon))
        self.setWindowIcon(QIcon(self.icon))
        self.pushButton_2.clicked.connect(lambda:Thread(target=self.send).start())
        self.textEdit.textChanged.connect(self.sete)
    def sete(self):
        if self.textEdit.toPlainText().replace(" ","")=="" and self.lineEdit.text().replace(" ","")=="":
            self.pushButton_2.setDisabled(True)
        else:
            self.pushButton_2.setEnabled(True)
    def send(self):
        self.pushButton_2.setText("发送中...")
        self.pushButton_2.setEnabled(0)
        self.lineEdit.setEnabled(0)
        self.lineEdit_2.setEnabled(0)
        self.textEdit.setEnabled(0)
        try:
            mail.mail(c=self.textEdit.toPlainText(),t=self.lineEdit.text(),f=self.lineEdit_2.text())
            self.ok.emit()
        except:
            self.fail.emit()
def start(message):
    global window
    window=Feedbacker()
    window.textEdit.setText("我在使用NoTopDomain时，遇到了如下这个bug：\n"+message+"\n希望修复！！！")
    window.show()
if __name__=="__main__":
    app = QApplication(sys.argv)
    window=Feedbacker()
    window.show()
    sys.exit(app.exec_())