from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ctypes import *
from win32gui import *
from win32con import *
from win32api import *
from . import Ui_Moyu
# import Ui_Moyu
import sys,random
mp={-4:"O3",-2:"O2",0:"",2:"WA",4:"TLE",8:"MLE",16:"RE",32:"CE",64:"PC",
    128:"UKE",256:"AC",512:"CSP",1024:"NOI",2048:"IOI",4096:"AK"}
color={-4:"#fd86bd",-2:"green",0:"#ffedc5",2:"#e74c3c",4:"#052242",8:"#1055a1",16:"#9d3dcf",
       32:"#ffe200",64:"rgb(242,128,17)",128:"#114885",256:"#52C41A",
       512:"#eed761",1024:"#8D2724",2048:"#66c8ff",4096:""}
nscore=0
for i in range(13,64):
    mp[2**i]=str(2**i)
    color[2**i]="black"
def add_two(mat):
    a = random.randint(0, len(mat)-1)
    b = random.randint(0, len(mat)-1)
    f=0
    while mat[a][b] and f<=10:
        f+=1
        a = random.randint(0, len(mat)-1)
        b = random.randint(0, len(mat)-1)
    gl=random.randint(1,128)
    if gl<=2:
        if not mat[a][b]: mat[a][b] = -4
    elif gl<=8:
        if not mat[a][b]: mat[a][b] = -2
    if not mat[a][b]: mat[a][b] = random.choice([2,2,2,4])
    return mat
 
 
 
def game_state(mat):
    # check for win cell
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 2048:
                return 'win'
    # check for any zero entries
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                return 'not over'
    # check for same cells that touch each other
    for i in range(len(mat)-1):
        # intentionally reduced to check the row on the right and below
        # more elegant to use exceptions but most likely this will be their solution
        for j in range(len(mat[0])-1):
            if mat[i][j] == mat[i+1][j] or mat[i][j+1] == mat[i][j]:
                return 'not over'
    for k in range(len(mat)-1):  # to check the left/right entries on the last row
        if mat[len(mat)-1][k] == mat[len(mat)-1][k+1]:
            return 'not over'
    for j in range(len(mat)-1):  # check up/down entries on last column
        if mat[j][len(mat)-1] == mat[j+1][len(mat)-1]:
            return 'not over'
    return 'lose'
 
 
 
def reverse(mat):
    new = []
    for i in range(len(mat)):
        new.append([])
        for j in range(len(mat[0])):
            new[i].append(mat[i][len(mat[0])-j-1])
    return new
 
 
 
def transpose(mat):
    new = []
    for i in range(len(mat[0])):
        new.append([])
        for j in range(len(mat)):
            new[i].append(mat[j][i])
    return new
 
 
 
def cover_up(mat):
    new = []
    for j in range(4):
        partial_new = []
        for i in range(4):
            partial_new.append(0)
        new.append(partial_new)
    done = False
    for i in range(4):
        count = 0
        for j in range(4):
            if mat[i][j] != 0:
                new[i][count] = mat[i][j]
                if j != count:
                    done = True
                count += 1
    return new, done
 
def merge(mat, done):
    global nscore
    for i in range(4):
        for j in range(4-1):
            if mat[i][j] == mat[i][j+1] and mat[i][j] > 0 and mat[i][j+1]>0:
                nscore+=mat[i][j]*2
                mat[i][j] *= 2
                mat[i][j+1] = 0
                done = True
            elif mat[i][j]<0 and mat[i][j+1]>0:
                nscore+=mat[i][j+1]*-mat[i][j]
                mat[i][j+1]*=-mat[i][j]
                mat[i][j]=0
                done=True
            elif mat[i][j+1]<0 and mat[i][j]>0:
                nscore+=mat[i][j]*-mat[i][j+1]
                mat[i][j]*=-mat[i][j+1]
                mat[i][j+1]=0
                done=True
    return mat, done
 
def up(game):
    game = transpose(game)
    # game, done = cover_up(game)
    game, done = merge(game, 1)
    game = cover_up(game)[0]
    game = transpose(game)
    return game
 
def down(game):
    # game = reverse(transpose(game))
    # game, done = cover_up(game)
    game, done = merge(game, 1)
    game = cover_up(game)[0]
    game = transpose(reverse(game))
    return game
 
def left(game):
    # return matrix after shifting left
    # game, done = cover_up(game)
    game, done = merge(game, 1)
    game = cover_up(game)[0]
    return game
 
def right(game):
    game = reverse(game)
    # game, done = cover_up(game)
    game, done = merge(game, 1)
    game = cover_up(game)[0]
    game = reverse(game)
    return game
class Moyu(QWidget,Ui_Moyu.Ui_Moyu2048):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setup()
    def setup(self):
        self.startButton.clicked.connect(self.switchGame)
        self.status=0
        nscore=0
        self.can=0
        try:
            self.hs=int(open("NTD2048HighScore","r+").read())
        except:
            self.hs=0
            try: 
                open("NTD2048HighScore","w+").close()
                SetFileAttributes("NTD2048HighScore",FILE_ATTRIBUTE_HIDDEN)
            except: pass
        self.lcdNumber.display(self.hs)
        self.tim=0
        if not self.checkBox_2.isChecked():
            windll.user32.SetWindowDisplayAffinity(int(self.winId()),0x11)
        self.setFocusPolicy(Qt.ClickFocus)
        self.matrix=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.update()
        self.startButton.setFocusPolicy(Qt.NoFocus)
        self.Reset.setFocusPolicy(Qt.NoFocus)
        self.checkBox.setFocusPolicy(Qt.NoFocus)
        self.flag=0
        self.timer=QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.tt)
        self.checkBox_2.clicked.connect(self.setjp)
        self.checkBox.clicked.connect(self.setzd)
        SetWindowPos(self.winId(),HWND_TOPMOST,0,0,0,0,SWP_NOMOVE|SWP_NOSIZE)
        self.Reset.setEnabled(0)
        self.Reset.clicked.connect(self.restart)
        self.init()
    def setjp(self):
        if not self.checkBox_2.isChecked():
            windll.user32.SetWindowDisplayAffinity(int(self.winId()),0x11)
        else:
            windll.user32.SetWindowDisplayAffinity(int(self.winId()),0)
    def setzd(self):
        if self.checkBox.isChecked():
            SetWindowPos(self.winId(),HWND_TOPMOST,0,0,0,0,SWP_NOMOVE|SWP_NOSIZE)
        else:
            SetWindowPos(self.winId(),HWND_NOTOPMOST,0,0,0,0,SWP_NOMOVE|SWP_NOSIZE)
    def tt(self):
        self.tim+=1
        self.time.setText("时间：{:02.0f}:{:02.0f}:{:02.0f}"
                          .format(self.tim//60//60,self.tim//60%60,self.tim%60))
    def keyPressEvent(self,event):
        if self.status:
            if   event.key()==Qt.Key_S or event.key()==Qt.Key_Down : 
                self.matrix=down(self.matrix)
                self.matrix=add_two(self.matrix)
                self.update()
            elif event.key()==Qt.Key_W or event.key()==Qt.Key_Up   : 
                self.matrix=up(self.matrix)
                self.matrix=add_two(self.matrix)
                self.update()
            elif event.key()==Qt.Key_A or event.key()==Qt.Key_Left : 
                self.matrix=left(self.matrix)
                self.matrix=add_two(self.matrix)
                self.update()
            elif event.key()==Qt.Key_D or event.key()==Qt.Key_Right: 
                self.matrix=right(self.matrix)
                self.matrix=add_two(self.matrix)
                self.update()
    def showE(self):
        if self.isMinimized():
            self.setWindowState(Qt.WindowNoState)
        if not self.checkBox_2.isChecked():
            windll.user32.SetWindowDisplayAffinity(int(self.winId()),0)
            windll.user32.SetWindowDisplayAffinity(int(self.winId()),0x11)
        self.setGeometry(self.x(),self.y(),100,100)
        self.show()
        self.setzd()
        self.setFixedSize(self.width(),self.height())
    def update(self):
        self.Score.display(nscore)
        self.lcdNumber.display(max(self.lcdNumber.value(),nscore))
        self.hs=max(self.hs,nscore)
        try: open("NTD2048HighScore","w").write(str(self.hs))
        except: pass
        for i in range(4):
            for j in range(4):
                eval("self.b%d_%d.setText(mp[self.matrix[%d][%d]])"%(i+1,j+1,i,j))
                eval("self.b%d_%d.setStyleSheet('color:white;background:%s;border:1px solid gray;border-radius:8px;font-size:24px;font-family:\"Microsoft YaHei\"')"%(i+1,j+1,color[self.matrix[i][j]]))
        akflag,fullflag=0,1
        for i in range(4):
            for j in range(4):
                if self.matrix[i][j]>=2048:
                    akflag=1
                if not self.matrix[i][j]:
                    fullflag=0
        if akflag and not self.can:
            QMessageBox.information(self,"提示","You AK IOI！RP：%d"%nscore)
            self.can=1
        if fullflag:
            fx,fy=[1,-1,0,0],[0,0,1,-1]
            for i in range(4):
                for j in range(4):
                    for k in range(4):
                        nx,ny=i+fx[k],j+fy[k]
                        if nx>3 or nx<0 or ny>3 or ny<0:
                            continue
                        if self.matrix[i][j]==self.matrix[nx][ny]:
                            return
                        elif self.matrix[i][j]<0 and self.matrix[nx][ny]>0:
                            return
                        elif self.matrix[nx][ny]<0 and self.matrix[i][j]>0:
                            return
            self.switchGame()
            self.flag=1
            QMessageBox.information(self,"提示","您AFO了！RP：%d"%nscore)
    def init(self):
        self.matrix=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.matrix=add_two(self.matrix)
        self.matrix=add_two(self.matrix)
        
        self.update()
    def restart(self):
        global nscore
        self.timer.stop()
        self.tim=0
        nscore=0
        self.timer.start()
        self.matrix=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.matrix=add_two(self.matrix)
        self.matrix=add_two(self.matrix)
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