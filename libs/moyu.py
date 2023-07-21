from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ctypes import *
from . import Ui_Moyu
import sys,random
mp={0:"",2:"WA",4:"TLE",8:"MLE",16:"RE",32:"CE",64:"PC",
    128:"UKE",256:"AC",512:"CSP",1024:"NOI",2048:"IOI"}
color={0:"#ffedc5",2:"#e74c3c",4:"#052242",8:"#1055a1",16:"#9d3dcf",
       32:"#ffe200",64:"rgb(242,128,17)",128:"#114885",256:"#52C41A",512:"",1024:"",2048:""}
class option():
    def __init__(self, input_field: list):
        self.field_number = input_field
        self.score = 0
    def tight(self, list_int: list) -> list:
        return sorted(list_int, key=lambda x: 1 if x == 0 else 0)
    # 将每一行进行平移
    def merge(self, list_int: list) -> list:
        tight_list_int = self.tight(list_int)
        for i in range(len(tight_list_int)-1):
            if list_int[i] == list_int[i+1]:
                list_int[i] = 0
                list_int[i+1] = list_int[i+1]*2
                self.score += list_int[i+1]
        return self.tight(list_int)

    def transpose(self, args):
        return [list(row) for row in zip(*args)]

    def invert(self, args):
        return [row[::-1] for row in args]
    def move_left(self):
        self.field_number = [self.merge(row) for row in self.field_number]

    def move_right(self):
        self.field_number = self.invert(
            [self.merge(row) for row in self.invert(self.field_number)])

    def move_up(self):
        self.field_number = self.transpose(
            [self.merge(row) for row in self.transpose(self.field_number)])

    def move_down(self):
        self.field_number = self.transpose(
            self.invert([self.merge(row) for row in self.transpose(self.field_number)]))

    def random_create(self,mode=0,dep=0):
        if dep<=3:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            if self.field_number[x][y] == 0:
                self.field_number[x][y] = random.choice([2] if mode else [2, 2, 2, 4])
            else: self.random_create(dep=dep+1)
        else: return
    def get_MaxScore(self):
        max_score = 0
        for numbers in self.field_number:
            for number in numbers:
                if number > max_score:
                    max_score = number
        return max_score
class Moyu(QWidget,Ui_Moyu.Ui_Moyu2048):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setup()
    def setup(self):
        self.startButton.clicked.connect(self.switchGame)
        self.status=0
        self.tim=0
        windll.user32.SetWindowDisplayAffinity(int(self.winId()),0x11)
        self.setFocusPolicy(Qt.ClickFocus)
        self.martix=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.op=option(self.martix)
        self.update()
        self.flag=0
        self.timer=QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.tt)
        self.Reset.setEnabled(0)
        self.Reset.clicked.connect(self.restart)
    def tt(self):
        self.tim+=1
        self.time.setText("时间：{:02.0f}:{:02.0f}:{:02.0f}"
                          .format(self.tim//60//60,self.tim//60%60,self.tim%60))
    def keyPressEvent(self,event):
        if self.status:
            if   event.key()==Qt.Key_S: self.op.move_down(),self.op.random_create(),self.update()
            elif event.key()==Qt.Key_W: self.op.move_up(),self.op.random_create(),self.update()
            elif event.key()==Qt.Key_A: self.op.move_left(),self.op.random_create(),self.update()
            elif event.key()==Qt.Key_D: self.op.move_right(),self.op.random_create(),self.update()
    def showE(self):
        windll.user32.SetWindowDisplayAffinity(int(self.winId()),0)
        windll.user32.SetWindowDisplayAffinity(int(self.winId()),0x11)
        self.setGeometry(self.x(),self.y(),100,100)
        self.show()
        self.init()
        self.setFixedSize(self.width(),self.height())
    def update(self):
        self.Score.display(self.op.score)
        for i in range(4):
            for j in range(4):
                eval("self.b%d_%d.setText(mp[self.op.field_number[%d][%d]])"%(i+1,j+1,i,j))
                eval("self.b%d_%d.setStyleSheet('color:white;background:%s;border:1px solid gray;border-radius:8px;font-size:24px;font-family:\"Microsoft YaHei\"')"%(i+1,j+1,color[self.op.field_number[i][j]]))
        flag=0
        for i in range(4):
            for j in range(4):
                if self.op.field_number[i][j]==2048:
                    flag=2
                if flag!=2 and not self.op.field_number[i][j]:
                    flag=1
            if flag: break
        if flag==2:
            self.switchGame()
            QMessageBox.information(self,"提示","恭喜您成为了一个成功的OIer！You AK IOI！RP：%d"%self.op.score)
        if not flag:
            fx,fy,flag2=[1,-1,0,0],[0,0,1,-1],1
            for i in range(4):
                for j in range(4):
                    for k in range(4):
                        nx,ny=i+fx[k],j+fy[k]
                        if nx>3 or nx<0 or ny>3 or ny<0:
                            continue
                        if self.op.field_number[i][j]==self.op.field_number[nx][ny]:
                            flag2=0
                            break
            if flag2:
                self.switchGame()
                self.flag=1
                QMessageBox.information(self,"提示","您AFO了！RP：%d"%self.op.score)
    def init(self):
        self.martix=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.op=option(self.martix)
        self.op.random_create(mode=1)
        self.op.random_create(mode=1)
        self.update()
    def restart(self):
        self.martix=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.op=option(self.martix)
        self.timer.stop()
        self.tim=0
        self.timer.start()
        self.op.random_create(mode=1)
        self.op.random_create(mode=1)
        self.update()
    def switchGame(self):
        if self.flag:
            self.restart()
            self.flag=0
        if not self.status:
            self.Reset.setEnabled(1)
            self.startButton.setText("暂停")
            self.status=1
            self.timer.start()
        else:
            self.Reset.setEnabled(0)
            self.timer.stop()
            self.startButton.setText("开始")
            self.status=0
if __name__=="__main__":
    app=QApplication(sys.argv)
    window=Moyu()
    window.showE()
    sys.exit(app.exec_())