from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import Ui_Moyu
class Moyu(QWidget,Ui_Moyu.Ui_Moyu2048):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setup()
    def setup(self):
        self.martix=[[],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
if __name__=="__main__":
    app=QApplication(sys.argv)
    window=Moyu()
    window.show()
    sys.exit(app.exec_())