from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import Qt,QObject,pyqtSignal,QTimer
from Ui_NTD import *
from win32api import *
from win32con import *
from win32gui import *
from ctypes import *
from ctypes.wintypes import *
from system_hotkey import SystemHotkey
from threading import Thread
import sys,os,psutil,subprocess,b64,base64
class NoTopDomain(QMainWindow,Ui_NoTopDomain,QObject):
    sw=pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setup()
        self.show()
        QApplication.processEvents()
        with open("ntsd.exe","wb") as f:
            f.write(base64.b64decode(b64.ntsd))
        QApplication.processEvents()
        Thread(target=self.setState).start()
        QApplication.processEvents()
        s=subprocess.run("tasklist|find /i \"studentmain.exe\"",shell=True).returncode
        QApplication.processEvents()
        if s:
            self.TDState=0
            QApplication.processEvents()
            self.KillTD.setText("启动极域！！！")
            QApplication.processEvents()
        self.stateTimer=QTimer()
        QApplication.processEvents()
        self.stateTimer.setInterval(1000)
        QApplication.processEvents()
        self.stateTimer.timeout.connect(lambda:Thread(target=self.setState).start())
        QApplication.processEvents()
        self.stateTimer.start()
        QApplication.processEvents()
    def setState(self):
        QApplication.processEvents()
        s=subprocess.run("tasklist|find /i \"studentmain.exe\"",shell=True).returncode
        if s:
            self.StudentRunning.setText("极域：<span style=\"color:green\">未运行</span>")
            self.HangUpTD.setEnabled(False)
        else:
            self.StudentRunning.setText("极域：<span style=\"color:orange\">运行中</span>")
            self.HangUpTD.setEnabled(True)
        hWndList = [] 
        EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList) 
        for hwnd in hWndList:
            title = GetWindowText(hwnd)
            if title=="屏幕广播":
                g=GetWindowRect(hwnd)
                self.GBing.setText("广播：<span style=\"color:orange\">进行中</span>")
                self.GBWindowed.setEnabled(True)
                return
        self.GBing.setText("广播：<span style=\"color:green\">未进行</span>")
        self.GBWindowed.setEnabled(False)
    def startTSK(self):
        subprocess.run("start /B taskmgr")
        QApplication.processEvent()
        self.ttimer.setInterval(2000)
        self.ttimer.timeout.connect(self.TSK)
        self.ttimer.start()
    def TSK(self): #未完成，有bug
        self.ttimer.stop()
        hWndList = [] 
        EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList) 
        for hwnd in hWndList:
            title = GetWindowText(hwnd)
            if title=="任务管理器":
                g=GetWindowRect(hwnd)
                SetWindowPos(hwnd,HWND_TOPMOST, g[0], g[1], g[2]-g[0], g[3]-g[1], SWP_NOSIZE|SWP)
    def EnableFullScreen(self):
        hWndList = [] 
        EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList) 
        for hwnd in hWndList:
            title = GetWindowText(hwnd)
            if title=="屏幕广播":
                hWndList2=[]
                EnumChildWindows(hwnd,self.EnumChildWindowsProc)
                return
    def EnumChildWindowsProc(self,hwndChild,lParam):
        hmenu=GetMenu(hwndChild)
        if LOWORD(hmenu)==1004:
            if not IsWindowEnabled(hwndChild):
                EnableWindow(hwndChild, TRUE)
            return 0
        return 1
    def closeEvent(self, event):
        event.accept()
        os.remove("ntsd.exe")
        os._exit(0)
    def setup(self):
        self.TDState=1
        self.HangState=1
        self.ttimer=QTimer()
        self.setFixedSize(self.width(),self.height())
        self.icon=QPixmap()
        self.icon.loadFromData(base64.b64decode(b64.icon))
        self.setWindowIcon(QIcon(self.icon))
        self.hk=SystemHotkey()
        self.hk.register(("alt","m"),callback=lambda _:self.sw.emit())
        self.hk.register(("alt","t"),callback=lambda _:self.startTSK)
        self.sw.connect(self.showWindow)
        self.GBWindowed.clicked.connect(self.EnableFullScreen)
        self.action_1.triggered.connect(self.showAbout)
        self.action_3.triggered.connect(lambda:self.startTSK)
        self.runWindow=QDialog()
        self.action_4.triggered.connect(self.runWindow.show)
        self.runWindow.setWindowTitle("运行软件")
        self.runWindow.setFixedSize(300,50)
        self.runWindow.setWindowIcon(self.windowIcon())
        self.runStart=QPushButton("运行",self.runWindow)
        self.runStart.clicked.connect(self.runApp)
        self.runDir=QToolButton(self.runWindow)
        self.runDir.setText("...")
        self.runDir.clicked.connect(lambda:self.runExe.setText(QFileDialog.getOpenFileName(self.runWindow, "运行...",".", "Appliaction(*.exe)")[0]))
        self.runExe=QLineEdit(self.runWindow)
        self.runExe.setPlaceholderText("输入运行程序路径...")
        self.layout=QHBoxLayout(self.runWindow)
        self.layout.addWidget(self.runExe)
        self.layout.addWidget(self.runDir)
        self.layout.addWidget(self.runStart)
        self.runWindow.setLayout(self.layout)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.runWindow.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.KillTD.clicked.connect(self.killTopDomain)
        self.HangUpTD.clicked.connect(self.hangTD)
        self.tray=QSystemTrayIcon(self.windowIcon())
        self.tray.setToolTip("NoTopDomain")
        self.trayMenu=QMenu()
        self.a1=QAction("显示/隐藏主界面")
        self.a1.triggered.connect(self.showWindow)
        self.a2=QAction("退出")
        self.a2.triggered.connect(self.close)
        self.trayMenu.addActions([self.a1,self.a2])
        self.tray.setContextMenu(self.trayMenu)
        self.tray.show()
        self.tray.activated[QSystemTrayIcon.ActivationReason].connect(self.activate)
        SetWindowPos(self.winId(),HWND_TOPMOST,self.x(),self.y(),self.width(),self.height(),SWP_NOSIZE|SWP_NOZORDER)
        pids=psutil.process_iter()
        for p in pids:
            if(p.name().lower()=="studentmain.exe"):
                pid=psutil.Process(p.pid)
                break
        try:
            if pid.status()=="stopped":
                self.HangState=0
                self.HangUpTD.setText("恢复极域")
                self.KillTD.setEnabled(False)
        except:
            self.KillTD.setEnabled(True)
    def activate(self,reason):
        if reason == QSystemTrayIcon.DoubleClick:
            self.showWindow()
    def hangTD(self):
        if self.HangState:
            pids=psutil.process_iter()
            for p in pids:
                if(p.name().lower()=="studentmain.exe"):
                    pid=psutil.Process(p.pid)
                    break
            try:
                pid.suspend()
                self.statusbar.showMessage("挂起成功")
                self.HangState=0
                self.HangUpTD.setText("恢复极域")
                self.KillTD.setEnabled(False)
            except:
                self.statusbar.showMessage("挂起失败")
        else:
            pids=psutil.process_iter()
            for p in pids:
                if(p.name().lower()=="studentmain.exe"):
                    pid=psutil.Process(p.pid)
                    break
            try:
                pid.resume()
                self.statusbar.showMessage("恢复成功")
                self.HangState=1
                self.HangUpTD.setText("挂起极域")
                self.KillTD.setEnabled(True)
            except:
                self.statusbar.showMessage("恢复失败")
    def killTopDomain(self):
        if self.TDState:
            s=subprocess.run("tasklist|find /i \"studentmain.exe\"",shell=True).returncode
            if s:
                self.statusbar.showMessage("杀极域失败")
            else:
                WinExec("ntsd -c q -pn studentmain.exe", SW_HIDE)
                self.statusbar.showMessage("成功杀掉极域")
                self.TDState=0
                self.KillTD.setText("老师来了！！！")
        else:
            try:
                reg=RegOpenKeyEx(HKEY_LOCAL_MACHINE, 'SOFTWARE\\WOW6432Node\\TopDomain\\e-Learning Class Standard\\1.00',0,KEY_ALL_ACCESS)
                location=RegQueryValueEx(reg,"TargetDirectory")[0]
                os.startfile(location+"studentmain.exe")
                self.TDState=1
                self.KillTD.setText("杀掉极域！！！")
                self.statusbar.showMessage("成功启动极域")
                self.HangState=0
                self.HangUpTD.setText("挂起极域")
            except:
                self.statusbar.showMessage("获取地址失败（未安装？）")
    def runApp(self): #有BUG
        subprocess.run("start /B \""+self.runExe.text()+"\"",shell=True)
        self.runExe.setText("")
        self.runWindow.close()
    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.WindowStateChange:
            if self.windowState() & QtCore.Qt.WindowMinimized:
                event.ignore()
                self.hide()
                return
    def showAbout(self):
        QMessageBox.about(self,'关于',"""NoTopDomain By LYX<br>Version 0.01（咕咕咕ing...）<br>Powered By <a href="https://blog.csdn.net/weixin_42112038/article/details/127480471">极域机房工具箱1.1</a><br><a href="https://yisous.xyz">博客</a> <a href="https://luogu.com.cn/user/761305">Luogu</a> <a href="https://github.com/lyxofficial">Github</a><br>Tip：遇到了怪异且难以破解的密码？<br>mythware_super_password<br>往往可以帮助你解决问题。""")
    def showWindow(self):
        if self.isHidden():
            self.showNormal()
        elif not self.isActiveWindow():
            self.activateWindow()
        else:
            self.hide()
if __name__=="__main__":
    app=QApplication(sys.argv)
    window=NoTopDomain()
    sys.exit(app.exec_())
