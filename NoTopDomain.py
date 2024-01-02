# -*- coding: utf-8 -*-

'''
QwQ (。・ω・。)

NoTopDomain v3.0

很多屎山的awa 新的大改版之后更多了

可以找到"shellsMaybeYouUse"来跑打包（（（

!!
接下来是

某蒟蒻的垃圾代码
!!

没有注释！！！

/* ! ! ! ! ! ! ! ! */

(　o=^•ェ•)o　┏━┓
'''

import os,sys,difflib,urllib.request,math
import subprocess as su
import qtawesome as qta
from json import *
from base64 import *
from random import *
from psutil import *
from hashlib import *
from traceback import *
from threading import *
from subprocess import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from win32api import *
from win32con import *
from win32gui import *
from win32print import *
from win32process import *
from win32gui_struct import *
from ctypes import *
from ctypes.wintypes import *
from libs.b64 import *
from libs.Ui_NTD import *
from libs.feedback import *
from libs.UDPAttack import *
from libs.system_hotkey import *
from libs.moyu import *
from libs.windowEffecter import *
from platform import *
from pynput import *



VERSION="v3.0"
DEBUG=FALSE
class NoTopDomain(QMainWindow,Ui_NoTopDomain,QObject):
    sw=pyqtSignal()
    st=pyqtSignal()
    top=pyqtSignal()
    kf=pyqtSignal()
    ef=pyqtSignal()
    ff=pyqtSignal()
    ts=pyqtSignal()
    gud=pyqtSignal()
    sc=pyqtSignal()
    vv=pyqtSignal(int)
    sm=pyqtSignal(int,int)
    cm=pyqtSignal(int,int)
    def __init__(self):
        super().__init__()
        self.isok=0
        self.logque=[]
        self.setupUi(self)
        self.retranslateUi(self)
        self.loadConfig()
        self.setup()
        self.show()
        self.setFixedSize(self.width(),self.height())
        self.isok=1
        self.loque()
        self.setHelpButton()
        self.addEffect()
        for i in range(8):
            self.PigeonGames.setCurrentIndex(i%7) 
        QApplication.processEvents()
        Thread(target=self.getUpdate).start()
        QApplication.processEvents()
    def addEffect(self):
        self.shadowEffect=[]
        # for it in self.findChildren(QGroupBox):
        #     self.shadowEffect.append(QGraphicsDropShadowEffect(self))
        #     self.shadowEffect[-1].setOffset(0,0)
        #     self.shadowEffect[-1].setBlurRadius(3)
        #     self.shadowEffect[-1].setColor(Qt.gray)
        #     print(Qt.gray)
        #     it.setGraphicsEffect(self.shadowEffect[-1])
        self.shadowEffect.append(QGraphicsDropShadowEffect(self))
        self.shadowEffect[-1].setOffset(0,0)
        self.shadowEffect[-1].setBlurRadius(20)
        self.shadowEffect[-1].setColor(Qt.gray)
        self.helpButton.setGraphicsEffect(self.shadowEffect[-1])
        self.shadowEffect.append(QGraphicsDropShadowEffect(self))
        self.shadowEffect[-1].setOffset(0,0)
        self.shadowEffect[-1].setBlurRadius(10)
        self.shadowEffect[-1].setColor(Qt.gray)
        self.textBrowser.setGraphicsEffect(self.shadowEffect[-1])
    def setHelpButton(self):
        self.helpButton=QPushButton("?",self)
        self.helpButton.setObjectName("helpButton")
        self.helpButton.setGeometry(self.width()-100,self.height()-100,60,60)
        self.helpButton.show()
        self.textBrowser=QTextBrowser(self)
        self.textBrowser.setObjectName("helpMd")
        self.textBrowser.setGeometry(self.width()-420,80,370,self.height()-190)
        self.textBrowser.stackUnder(self.helpButton)
        self.helpButton.clicked.connect(lambda:(self.textBrowser.hide(),self.helpButton.setText("?")) if self.textBrowser.isVisible() else (self.textBrowser.show(),self.helpButton.setText("×")))
        self.showHelp()
    def shownormal(self):
        if not self.checkBox_4.isChecked():
            windll.user32.SetWindowDisplayAffinity(int(self.winId()),0)
            windll.user32.SetWindowDisplayAffinity(int(self.winId()),0x00000011)
        self.showNormal()
    def drawLogBar(self):
        self.logtim+=1
        if self.logtim<=4000:
            self.logpro.setValue(10000*self.easeOutElastic((4000-self.logtim)/4000))
        else:self.logpro.hide()
        if self.logtim>=5000:
            self.logTimer.stop()
            self.logpro.hide()
            self.logLabel.hide()
    def easeOutElastic(self,x):
        return x*(x**2)
    def setup(self):
        self.logLabel=QLabel(self)
        self.logLabel.setObjectName("logLabel")
        self.logpro=QSlider(self)
        self.logpro.setObjectName("logpro")
        self.logpro.setMaximum(10000)
        self.logpro.setEnabled(0)
        self.logpro.setOrientation(Qt.Horizontal)
        self.logLabel.setWordWrap(1)
        self.logLabel.hide()
        self.logtim=0
        self.logTimer=QTimer()
        self.logTimer.setInterval(1)
        self.logTimer.timeout.connect(self.drawLogBar)
        self.ver.setText(VERSION)
        pids=process_iter()
        self.label_39.setPixmap(QIcon(qta.icon("ri.radar-line",color="gray")).pixmap(32,32))
        self.label_44.setPixmap(QIcon(qta.icon("ei.magic",color="gray")).pixmap(32,32))
        self.logger=open(os.getenv("temp")+"\\NoTopDomain.log","ab+",buffering=0)
        self.logger.write(("[%s] %s %s 启动 DEBUG: %d\n"%(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),__file__,VERSION,DEBUG)).encode())
        self.setWindowTitle("NoTopDomain %s"%VERSION)
        self.st.connect(self.hideWindow)
        self.kf.connect(self.killFocus)
        self.sc.connect(self.stopCap)
        self.horizontalSlider.setMinimum(30)
        self.horizontalSlider.setValue(100)
        self.capWindow.clicked.connect(self.getWindow)
        self.horizontalSlider.valueChanged.connect(lambda:
            (self.setWindowOpacity(self.horizontalSlider.value()/100),
             self.moyu.setWindowOpacity(self.horizontalSlider.value()/100),
            self.gjW.setWindowOpacity(self.horizontalSlider.value()/100)))
        self.top.connect(self.setTop)
        self.sm.connect(lambda x,y:(self.gbMenu.exec(QPoint(x,y)),SetWindowPos(self.gbMenu.winId(),HWND_TOPMOST,0,0,0,0,SWP_NOMOVE|SWP_NOSIZE)))
        self.cm.connect(self.closeMenu)
        try:
            reg=RegOpenKeyEx(HKEY_LOCAL_MACHINE,'SOFTWARE\\WOW6432Node\\TopDomain\\e-Learning Class Standard\\1.00',0,KEY_ALL_ACCESS)
            self.location=RegQueryValueEx(reg,"TargetDirectory")[0]
            self.lineEdit_2.setText(self.location)
            self.lineEdit_2.setCursorPosition(0)
        except:
            try:
                reg=RegOpenKeyEx(HKEY_LOCAL_MACHINE,'SOFTWARE\\TopDomain\\e-Learning Class Standard\\1.00',0,KEY_ALL_ACCESS)
                self.location=RegQueryValueEx(reg,"TargetDirectory")[0]
                self.lineEdit_2.setText(self.location)
                self.lineEdit_2.setCursorPosition(0)
            except:
                self.location=""
                self.CopyLink.setDisabled(1)
                self.UninstallTopDomain.setDisabled(True)
        if self.location:
            try:
                if not os.path.exists(self.location+"\\MinHook.x86.dll"):
                    with open(self.location+"\\MinHook.x86.dll","wb+") as f:
                        f.write(b64decode(mhookdll))
            except: pass
        try:
            if "Shutdown_back.exe" in os.listdir(self.location):
                self.NoShutdown.setChecked(0)
        except: pass
        EnumWindows(self.NoRunningAgain,0)
        try:
            reg=RegOpenKeyEx(HKEY_CURRENT_USER,r'SOFTWARE\Policies\Microsoft\Windows\System',0,KEY_ALL_ACCESS)
            RegSetValueEx(reg,"DisableCMD",0,REG_DWORD,0)
            reg.Close()
        except:
            pass
        self.pushButton_2.clicked.connect(self.saveConfig)
        self.setGeometry(100,100,300,300)
        self.TDState=1
        self.HangState=1
        self.gud.connect(self.gudone)
        self.CopyLink.clicked.connect(self.copyLink)
        self.ttimer=QTimer()
        self.setFocusPolicy(Qt.StrongFocus)
        self.icon=QPixmap()
        self.icon.loadFromData(b64decode(icon))
        self.reStart.clicked.connect(self.restart)
        self.setWindowIcon(QIcon(self.icon))
        self.zb=QTimer()
        self.zb.setInterval(randint(200,3000))
        self.zb.timeout.connect(self.ZB)
        self.zb.start()
        self.vv.connect(self.verifyUnis)
        self.widget.hide()
        self.ExitProcess.setIcon(qta.icon("fa.power-off",color="white"))
        self.tb1.setIcon(qta.icon("ei.magic",color="white"))
        self.tb2.setIcon(qta.icon("ri.settings-3-line",color="white"))
        self.tb3.setIcon(qta.icon("ri.window-line",color="white"))
        self.tb4.setIcon(qta.icon("fa.gamepad",color="white"))
        self.tb5.setIcon(qta.icon("mdi.wall",color="white"))
        self.tb6.setIcon(qta.icon("mdi.information-outline",color="white"))
        self.stTSK.setIcon(qta.icon("fa.tasks"))
        self.CopyLink.setIcon(qta.icon("ri.file-copy-2-line"))
        self.deleteIcon.setIcon(qta.icon("ri.delete-bin-6-line"))
        self.changeIcon.setIcon(qta.icon("fa5s.exchange-alt"))
        self.refresh.setIcon(qta.icon("fa.refresh"))
        self.pushButton_2.setIcon(qta.icon("fa5.save"))
        self.reStart.setIcon(qta.icon("mdi.restart"))
        self.CopyLink.setIconSize(QSize(20,20))
        self.CopyLink.setFixedSize(self.lineEdit_2.height(),self.lineEdit_2.height())
        self.label_5.setPixmap(qta.icon("mdi.file-link").pixmap(24,24))
        self.label_6.setPixmap(qta.icon("fa5s.key").pixmap(24,24))
        self.label_10.setPixmap(qta.icon("mdi6.progress-close").pixmap(28,28))
        self.label_13.setPixmap(qta.icon("ph.terminal-window-bold").pixmap(28,28))
        self.UninstallTopDomain.setIcon(qta.icon("ri.delete-bin-6-line"))
        self.label_18.setPixmap(self.icon.scaled(100,100,Qt.IgnoreAspectRatio,Qt.SmoothTransformation))
        self.floatwin=QLabel()
        self.floatwin.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowTransparentForInput|Qt.WindowStaysOnTopHint)
        self.floatwin.setWindowOpacity(0.8)
        self.floatwin.setAttribute(Qt.WA_ShowWithoutActivating,1)
        self.floatwin.setStyleSheet("border:1px solid black;font-family:\"Microsoft Yahei\";")
        self.fb=Feedbacker(self)
        windll.user32.SetWindowDisplayAffinity(int(self.fb.winId()),0x11)
        self.checkBox_5.clicked.connect(self.switchTitle)
        SetWindowPos(self.fb.winId(),HWND_TOPMOST,0,0,0,0,SWP_NOSIZE|SWP_NOMOVE)
        self.UnlockTDHook.clicked.connect(self.unHook)
        if not self.config.get("QssDisabled"):
            if DEBUG:
                self.setStyleSheet(open(bl+"/libs/NTD.qss",encoding="utf-8").read())
            else:
                self.setStyleSheet(base64.b64decode(qss).decode())
        self.WebsiteYes.clicked.connect(self.websiteYes)
        self.hk=SystemHotkey()
        try:
            self.hk.register(['control' if i=='ctrl' else i for i in self.config.get("AcWindow").split("+")],callback=lambda _:self.sw.emit())
            self.hk.register(['control' if i=='ctrl' else i for i in self.config.get("KillWindow").split("+")],callback=lambda _:self.kf.emit())
            self.hk.register(['control' if i=='ctrl' else i for i in self.config.get("HideWindow").split("+")],callback=lambda _:self.st.emit())
            self.hk.register(['control' if i=='ctrl' else i for i in self.config.get("TopWindow").split("+")],callback=lambda _:self.top.emit())
            self.hk.register(['control' if i=='ctrl' else i for i in self.config.get("Switch").split("+")],callback=lambda _:self.ef.emit())
            self.hk.register(['control' if i=='ctrl' else i for i in self.config.get("ForceFull").split("+")],callback=lambda _:self.ff.emit())
        except:
            try:
                self.hk.register(("alt","m"),callback=lambda _:self.sw.emit())
                self.hk.register(("alt","k"),callback=lambda _:self.kf.emit())
                self.hk.register(("alt","h"),callback=lambda _:self.st.emit())
                self.hk.register(("alt","y"),callback=lambda _:self.top.emit())
                self.hk.register(("alt","q"),callback=lambda _:self.ef.emit())
                self.hk.register(("alt","f"),callback=lambda _:self.ff.emit())
            except:
                self.log("热键注册失败，请尝试更改配置")
        else:
            if DEBUG:
                self.log("已启动调试模式")
            else:
                global ff
                if ff==1:
                    self.log("加载工具DLL失败，部分功能受影响")
                elif ff==2:
                    self.log("等待操作...(检测到已开启UAC，建议查看帮助)")
                else:
                    self.log("等待操作...(建议查看帮助)")
        self.ff.connect(self.forceFull)
        self.sw.connect(self.showWindow)
        self.trfl=0
        self.gjW=UDPAttack()
        self.gjW.setWindowIcon(self.windowIcon())
        self.horizontalLayout_22.addWidget(self.gjW)
        self.label_23.setPixmap(self.icon.scaled(40,40,Qt.IgnoreAspectRatio,Qt.SmoothTransformation))
        self.moyu=Moyu()
        # self.moyu.setWindowIcon(self.windowIcon())
        # self.moyu.setStyleSheet(self.styleSheet())
        self.horizontalLayout_5.addWidget(self.moyu)
        self.moyu.widget.setFixedSize(self.moyu.widget.width()-40,self.moyu.widget.width()-40)
        self.moyu.buttonbox.setFixedSize(self.moyu.widget.width(),self.moyu.buttonbox.height())
        for i in range(1,5):
            for j in range(1,5):
                exec(f"self.moyu.b{i}_{j}.setFixedSize(self.moyu.widget.width()//4-18,self.moyu.widget.width()//4-18)")
        # windll.user32.SetWindowDisplayAffinity(int(self.gjW.winId()),0x11)
        if not self.moyu.checkBox_2.isChecked():
            windll.user32.SetWindowDisplayAffinity(int(self.moyu.winId()),0x11)
        self.GBWindowed.clicked.connect(self.EnableFullScreen)
        self.checkBox_4.clicked.connect(self.switchWindowVisiable)
        self.ef.connect(lambda:self.EnableFullScreen() if self.GBWindowed.isEnabled() else self.log("切换窗口化仅在检查到广播后可用"))
        self.action_1=QAction("关于")
        self.action_4=QAction("日志")
        self.feedback=QAction("反馈")
        self.action_3=QAction("TSK")
        self.action_6=QAction("摸鱼")
        self.action_7=QAction("攻击")
        self.action_5=QAction("退出")
        self.pushButton_7.clicked.connect(self.showAbout)
        self.action_7.triggered.connect(self.gjW.showE)
        self.action_6.triggered.connect(self.moyu.showE)
        self.action_5.triggered.connect(lambda:os._exit(0) if self.question("提示","退出程序吗？")==16384 else 0)
        self.topLabel=QLabel("")
        self.topLabel.setWindowFlag(Qt.SplashScreen)
        self.topLabel.setStyleSheet("font-family:\"Microsoft YaHei\";padding:5px;background:white;border:1px solid;border-radius:3px")
        self.topLabel2=QLabel("")
        self.topLabel2.setWindowFlag(Qt.SplashScreen)
        self.topLabel2.setStyleSheet("font-family:\"Microsoft YaHei\";padding:5px;background:white;border:1px solid;border-radius:3px")
        self.tltimer=QTimer()
        self.tltimer.setInterval(2000)
        self.tltimer.timeout.connect(self.hidelb)
        self.tl2timer=QTimer()
        self.tl2timer.setInterval(3000)
        self.tl2timer.timeout.connect(self.hidelb2)
        self.checkBox.clicked.connect(self.reTrayState)
        self.pushButton_4.clicked.connect(lambda:Popen(f"""explorer /select, "{os.getenv("systemdrive")}\\NoTopDomain {self.updver}.exe" """,shell=True))
        self.closeWin.clicked.connect(self.close)
        self.minWin.clicked.connect(self.sw.emit)
        self.stTSK.clicked.connect(self.startTSK)
        self.HangUpTD.setFixedSize(70,70)
        self.GBWindowed.setFixedSize(70,70)
        self.CloseGB.setFixedSize(70,70)
        self.KillTD.setFixedSize(70,70)
        self.ExitProcess.clicked.connect(lambda:os._exit(0) if self.question("提示","退出程序吗？")==16384 else 0)
        # self.menubar.addActions([self.action_1,self.action_4,self.feedback,self.action_3,self.action_6,self.action_7,self.action_5])
        self.action_1.triggered.connect(self.showAbout)
        self.action_2.triggered.connect(self.showHelp)
        self.action_3.triggered.connect(self.startTSK)
        self.action_4.triggered.connect(lambda:Popen("notepad \""+os.getenv("temp")+"\\NoTopDomain.log"+"\"",shell=True))
        self.pushButton_6.clicked.connect(lambda:Popen("notepad \""+os.getenv("temp")+"\\NoTopDomain.log"+"\"",shell=True))
        self.RestartExplorer.clicked.connect(self.restartExplorer)
        self.setWindowFlags(self.windowFlags()|Qt.FramelessWindowHint)
        self.effect=window_effect.WindowEffect()
        self.effect.setShadowEffect(self.winId())
        self.KillTD.clicked.connect(self.killTopDomain)
        self.HangUpTD.clicked.connect(self.hangTD)
        self.pushButton.clicked.connect(lambda:Thread(target=self.downloadUpdate).start())
        self.tray=QSystemTrayIcon(self.windowIcon())
        self.tray.setToolTip("NoTopDomain")
        self.trayMenu=QMenu(self)
        self.openFolderIcon.clicked.connect(self.openIconFile)
        if not self.config.get("QssDisabled"):
            self.trayMenu.setStyleSheet(menuqss)
        self.topThisWindow.clicked.connect(lambda:self.setTop(mode=1))
        self.hideThisWindow.clicked.connect(lambda:self.hideWindow(mode=1))
        self.killThisWindow.clicked.connect(lambda:self.killFocus(mode=1))
        self.changeThisWindowTitle.clicked.connect(lambda: (SetWindowText(self.nowhwnd,self.newWindowTitle.text()),self.log("修改窗口标题成功："+self.newWindowTitle.text())) if IsWindow(self.nowhwnd) else self.log("窗口句柄无效"))
        self.a0=QAction("NoTopDomain %s"%VERSION)
        self.a0.setEnabled(False)
        self.a1=QAction("显示/隐藏主界面")
        self.a1.triggered.connect(self.showWindow)
        self.a2=QAction("退出")
        self.a2.triggered.connect(lambda:os._exit(0) if self.question("提示","退出程序吗？")==16384 else 0)
        self.a3=QAction("配置")
        self.a3.triggered.connect(self.toSetting)
        self.setWindowFlag
        self.trayMenu.addActions([self.a0,self.a1,self.a3,self.a2])
        self.tray.setContextMenu(self.trayMenu)
        self.gbMenu=QMenu(self)
        SetWindowPos(self.gbMenu.winId(),HWND_TOPMOST,0,0,0,0,SWP_NOMOVE|SWP_NOSIZE)
        if not self.config.get("QssDisabled"):
            self.gbMenu.setStyleSheet(menuqss)
        self.NoRemoteRun.clicked.connect(self.noremoterun)
        self.tb1.clicked.connect(lambda:self.PigeonGames.setCurrentIndex(0))
        self.tb2.clicked.connect(lambda:self.PigeonGames.setCurrentIndex(1))
        self.tb3.clicked.connect(lambda:self.PigeonGames.setCurrentIndex(2))
        self.tb4.clicked.connect(lambda:self.PigeonGames.setCurrentIndex(3))
        self.tb5.clicked.connect(lambda:self.PigeonGames.setCurrentIndex(4))
        self.tb6.clicked.connect(lambda:self.PigeonGames.setCurrentIndex(5))
        self.g0=QAction("NoTopDomain Menu")
        self.g0.setEnabled(0)
        self.g1=QAction("查看帮助")
        self.g1.triggered.connect(self.toHelp)
        self.g2=QAction("解冻/恢复全屏")
        self.g2.triggered.connect(self.EnableFullScreen)
        self.g3=QAction("强制全屏")
        self.g3.triggered.connect(self.forceFull)
        self.g4=QAction("关闭广播窗口")
        self.g4.triggered.connect(self.closeGB)
        self.CloseGB.clicked.connect(self.closeGB)
        self.g5=QAction("杀掉极域")
        self.g5.triggered.connect(lambda:self.killTopDomain() if self.question("警告","真的要杀掉极域吗？",x=GetWindowRect(tdgbhwnd)[0]+50,y=GetWindowRect(tdgbhwnd)[1]+100)==16384 else 0)
        self.g6=QAction("恢复软件窗口")
        self.g6.triggered.connect(self.shownormal)
        self.gbMenu.addActions([self.g0,self.g6,self.g1,self.g2,self.g3,self.g4,self.g5])
        if not self.checkBox.isChecked():
            self.tray.show()
        self.pushButton_5.clicked.connect(self.Feedback)
        self.UninstallTopDomain.clicked.connect(lambda:Thread(target=self.uninstallTopDomain).start())
        self.KeyboardYes.clicked.connect(self.enableKeyboard)
        self.MouseYes.clicked.connect(self.enableMouse)
        self.ToolsYes.clicked.connect(self.enableTools)
        self.KeyboardYes.setChecked(1)
        self.ttt=QTimer()
        self.ttt.setInterval(200)
        self.ttt.timeout.connect(self.showProgress)
        self.ts.connect(self.ttt.start)
        self.IamTop.setChecked(1)
        self.IamTop.clicked.connect(self.toTop)
        self.NoShutdown.clicked.connect(self.noShutDown)
        self.resetTitle.clicked.connect(lambda:self.newWindowTitle.setText(self.oldname))
        self.NoControl.clicked.connect(self.unRemoteControl)
        self.NoImg.clicked.connect(self.noImg)
        self.NoBlackScreen.clicked.connect(self.nbs)
        self.changeNormalIcon.clicked.connect(lambda:(
            SendMessage(self.nowhwnd,WM_SETICON,ICON_SMALL,LoadIcon(NULL,IDI_APPLICATION)),
            SendMessage(self.nowhwnd,WM_SETICON,ICON_BIG,LoadIcon(NULL,IDI_APPLICATION)),
            self.log("设置默认图标成功")) if IsWindow(self.nowhwnd) else self.log("窗口句柄无效"))
        self.resetIcon.clicked.connect(lambda:(
            SendMessage(self.nowhwnd,WM_SETICON,ICON_SMALL,self.oldiconsmall),
            SendMessage(self.nowhwnd,WM_SETICON,ICON_BIG,self.oldiconbig),
            self.log("恢复图标成功")) if IsWindow(self.nowhwnd) else self.log("窗口句柄无效"))
        self.USBYes.clicked.connect(self.usbYes)
        self.tray.activated.connect(self.activate)
        SetWindowPos(self.winId(),HWND_TOPMOST,self.x(),self.y(),self.width(),self.height(),SWP_NOSIZE|SWP_NOZORDER)
        pids=process_iter()
        for p in pids:
            if(p.name().lower()=="studentmain.exe"):
                pid=Process(p.pid)
                break
        try:
            if pid.status()=="stopped":
                self.HangState=0
                self.HangUpTD.setText("恢复\n极域")
                self.HangUpTD.setEnabled(True)
                self.KillTD.setEnabled(False)
        except:
            self.KillTD.setEnabled(True)
        if self.config.get("UseNTSD"):
            if os.path.exists(os.getenv("temp")+"\\ntsd.exe"):
                self.ntsd=os.getenv("temp")+"\\ntsd.exe"
            else:
                with open(os.getenv("temp")+"\\ntsd.exe","wb") as f:
                    f.write(b64decode(ntsd))
                self.ntsd=os.getenv("temp")+"\\ntsd.exe"
        self.startupinfo = su.STARTUPINFO()
        self.startupinfo.wShowWindow = su.SW_HIDE
        self.startupinfo.dwFlags = su.STARTF_USESHOWWINDOW
        
    # def getRealResolution(self):
    #     hDC=GetDC(0)
    #     wide=GetDeviceCaps(hDC,DESKTOPHORZRES)
    #     high=GetDeviceCaps(hDC,DESKTOPVERTRES)
    #     return {"wide":wide,"high":high}
    # def getScreenSize(self):
    #     wide=GetSystemMetrics(0)
    #     high=GetSystemMetrics(1)
    #     return {"wide":wide,"high":high}
    # def getScaling(self):
    #     realResolution=self.getRealResolution()
    #     screenSize=self.getScreenSize()
    #     proportion=round(realResolution['wide']/screenSize['wide'],2)
    #     return proportion
    # 可能有用
    def mousePressEvent(self, event):
        if event.pos().y()>self.widget_2.height():
            return

        ReleaseCapture()
        SendMessage(self.window().winId(), win32con.WM_SYSCOMMAND,
                    win32con.SC_MOVE + win32con.HTCAPTION, 0)
        event.ignore()
    def NoRunningAgain(self,hwnd,lParam):
        if hwnd and "Qt5" in GetClassName(hwnd) and hwnd!=int(self.winId()) and difflib.SequenceMatcher(None,self.windowTitle(),GetWindowText(hwnd)).ratio()>0.6:
            SetForegroundWindow(hwnd)
            if not IsWindowVisible(hwnd):
                try:
                    sg=self.config.get("AcWindow").split('+')
                    for i in sg:
                        keybd_event(key[i],0,0,0)
                    sg.reverse()
                    for i in sg:
                        keybd_event(key[i],0,KEYEVENTF_KEYUP,0)
                except:
                    keybd_event(18,0,0,0)
                    keybd_event(77,0,0,0)
                    keybd_event(77,0,KEYEVENTF_KEYUP,0)
                    keybd_event(18,0,KEYEVENTF_KEYUP,0)
            os._exit(0)
    def noremoterun(self):
        try:
            if self.NoRemoteRun.isChecked():
                if self.question("提示","此功能尚不稳定，\
开启后会自动在极域运行远程命令和杀掉进程时弹框确认，可能出现各种失败如极域崩溃，继续吗？\n\
如果因此被掉线导致您当场寄掉，这个蒟蒻可是不负责任的呢awa\n\
可以实现的拦截包括但不限于：\n\
1.禁止黑屏广播反复切换焦点\n2.拦截极域远程运行/关机\n3.拦截极域杀掉进程\n4.拦截极域关闭窗口\n5.禁止极域广播置顶")\
                ==16384:
                    if not self.TDState:
                        self.log("未启动极域")
                        self.NoRemoteRun.setChecked(0)
                        return
                    it=process_iter()
                    for i in it:
                        if i.name().lower()=="studentmain.exe":
                            if not su.run(os.getenv("temp")+"\\NTDHookRunner.exe --pid="+str(i.pid),stdout=su.PIPE).returncode:
                                self.log("设置极域系统函数钩子成功")
                                self.NoRemoteRun.setEnabled(0)
                                self.label_30.setEnabled(0)
                            else: 
                                self.log("设置极域系统函数钩子失败")
                                self.NoRemoteRun.setChecked(0)
                else:
                    self.NoRemoteRun.setChecked(0)
        except: 
            self.log("设置极域系统函数钩子失败")
            self.NoRemoteRun.setChecked(0)
    def switchTitle(self):
        global flag6
        if self.checkBox_5.isChecked():
            self.tmptmr=QTimer()
            self.tmptmr.setInterval(1000)
            self.tmptmr.timeout.connect(self.stoptmp)
            self.tmptmr.start()
        flag6=not self.checkBox_5.isChecked()
    def stoptmp(self):
        self.tmptmr.stop()
        self.tmptmr.deleteLater()
        self.setWindowTitle(f"NoTopDomain {VERSION}")
    def closeMenu(self,x,y):
        x1,y1,x2,y2=GetWindowRect(self.gbMenu.winId())
        if x<=x1 or x>=x2 or y<=y1 or y>=y2:
            self.gbMenu.close()
    def downloadUpdate(self):
        try:
            self.log("开始下载更新")
            self.pushButton.setDisabled(1)
            self.pro=0
            self.ts.emit()
            t=time.time()
            self.sp=0
            url=f"https://npm.elemecdn.com/ntdupdapi@latest/NoTopDomain%20{self.updver}.exe"
            with open(os.getenv("systemdrive")+"\\NoTopDomain %s.exe"%self.updver,"wb+",buffering=0) as f:
                for i in range(0,self.cl,int(self.cl//50)):
                    if i+self.cl//50<=self.cl:
                        r=urllib.request.Request(url=url,headers={"Range":"bytes=%s-%s"%(i,i+self.cl//50-1)})
                    else:
                        r=urllib.request.Request(url=url,headers={"Range":"bytes=%s-"%(i)})
                    req=urllib.request.urlopen(r)
                    f.write(req.read())
                    self.sp=round((self.cl/1024/1024)/(time.time()-t),2)
                    self.pro+=2
            self.pushButton.setText("下载完成")
            self.log("下载完成")
        except:
            self.log("下载失败")
    def hideWindow(self,mode=0):
        if mode:
            hwnd=self.nowhwnd
        else: hwnd=GetForegroundWindow()
        try:
            if hwnd==int(self.winId()) or hwnd==int(self.topLabel2.winId()) or hwnd==int(self.gjW.winId()) or hwnd==int(self.moyu.winId()):
                self.log("触发进程保护...")
                return
            ptr=pointer(c_int(0))
            if windll.user32.GetWindowDisplayAffinity(hwnd,ptr):
                pid=GetWindowThreadProcessId(hwnd)[1]
                if ptr.contents.value:
                    if GetNativeSystemInfo()[0]==9 and not IsWow64Process(OpenProcess(PROCESS_ALL_ACCESS,0,pid)):
                        Tools.InjectDLL(pid,bytes(os.getenv("temp")+"\\NTDShower.dll","utf-8"))
                    else:
                        run(os.getenv("temp")+"\\NTDHide32Runner.exe --pid=%d --type=%d"%(pid,0),stdout=su.PIPE)
                    Sleep(100)
                    ptr2=pointer(c_int(0))
                    windll.user32.GetWindowDisplayAffinity(hwnd,ptr2)
                    if ptr2.contents.value!=ptr.contents.value:
                        self.topLabel2.setText("显示窗口成功")
                        self.log("显示窗口成功")
                    else: 
                        self.topLabel2.setText("显示窗口失败")
                        self.log("显示窗口失败")
                    self.topLabel2.show()
                    x,y,_,__=GetWindowRect(hwnd)
                    SetWindowPos(self.topLabel2.winId(),HWND_TOPMOST,x+10,y+10,0,0,SWP_NOSIZE)
                    SetForegroundWindow(hwnd)
                    if self.checkBox_4.isChecked():
                        windll.user32.SetWindowDisplayAffinity(int(self.topLabel2.winId()),0)
                    else:
                        windll.user32.SetWindowDisplayAffinity(int(self.topLabel2.winId()),0x11)
                    self.tl2timer.start()
                else:
                    if GetNativeSystemInfo()[0]==9 and not IsWow64Process(OpenProcess(PROCESS_ALL_ACCESS,0,pid)):
                        Tools.InjectDLL(pid,bytes(os.getenv("temp")+"\\NTDHider.dll","utf-8"))
                    else:
                        run(os.getenv("temp")+"\\NTDHide32Runner.exe --pid=%d --type=%d"%(pid,1),stdout=PIPE)
                    Sleep(100)
                    ptr2=pointer(c_int(0))
                    windll.user32.GetWindowDisplayAffinity(hwnd,ptr2)
                    if ptr2.contents.value!=ptr.contents.value:
                        self.topLabel2.setText("隐藏窗口成功")
                        self.log("隐藏窗口成功")
                    else:
                        self.topLabel2.setText("隐藏窗口失败")
                        self.log("隐藏窗口失败")
                    self.topLabel2.show()
                    x,y,_,__=GetWindowRect(hwnd)
                    SetWindowPos(self.topLabel2.winId(),HWND_TOPMOST,x+10,y+10,0,0,SWP_NOSIZE)
                    if self.checkBox_4.isChecked():
                        windll.user32.SetWindowDisplayAffinity(int(self.topLabel2.winId()),0)
                    else:
                        windll.user32.SetWindowDisplayAffinity(int(self.topLabel2.winId()),0x11)
                    self.tl2timer.start()
            if mode:
                if self.hideThisWindow.text()=="隐藏此窗口" and ptr2.contents.value!=ptr.contents.value:
                    self.hideThisWindow.setText("显示此窗口")
                elif self.hideThisWindow.text()=="显示此窗口" and ptr2.contents.value!=ptr.contents.value:
                    self.hideThisWindow.setText("隐藏此窗口")
        except: self.log("窗口句柄错误")
    def getWindow(self):
        self.capWindow.setEnabled(0)
        self.topThisWindow.setEnabled(0)
        self.hideThisWindow.setEnabled(0)
        self.killThisWindow.setEnabled(0)
        self.changeThisWindowTitle.setEnabled(0)
        self.newWindowTitle.setEnabled(0)
        self.resetTitle.setEnabled(0)
        self.changeNormalIcon.setEnabled(0)
        self.openFolderIcon.setEnabled(0)
        self.resetIcon.setEnabled(0)
        self.captimer=QTimer()
        self.captimer.setInterval(100)
        self.captimer.timeout.connect(self.showCapture)
        self.captimer.start()
        self.log("开始捕获窗口")
        self.floatwin.show()
        self.hk.register(("control","alt","p"),callback=lambda _:self.sc.emit(),overwrite=1)
    def showCapture(self):
        try:
            hwnd=GetForegroundWindow()
            pid=GetWindowThreadProcessId(hwnd)[1]
            pids=process_iter()
            procname=""
            for p in pids:
                if(p.pid==pid):
                    procname=p.name()
                    break
            self.floatwin.setText(f"窗口标题：{GetWindowText(hwnd)}\n窗口类名：{GetClassName(hwnd)}\n窗口位置：{str(GetWindowRect(hwnd))}\n窗口句柄：{int(hwnd)}\n窗口进程：{procname}")
            self.floatwin.adjustSize()
            self.floatwin.setGeometry(GetWindowRect(hwnd)[0]+50,GetWindowRect(hwnd)[1]+50,self.floatwin.width(),self.floatwin.height())
            self.textBrowser_2.setPlainText(f"窗口标题：{GetWindowText(hwnd)}\n窗口类名：{GetClassName(hwnd)}\n窗口位置：{str(GetWindowRect(hwnd))}\n窗口句柄：{int(hwnd)}\n窗口进程：{procname}")
        except: pass
    def openIconFile(self):
        if(not IsWindow(self.nowhwnd)):
            print("窗口句柄无效")
            return
        dir=QFileDialog.getOpenFileName(self,"选择图标文件","","图标(*.ico)")
        if(dir[0]):
            li=LoadImage(0,dir[0],IMAGE_ICON,GetSystemMetrics(win32con.SM_CXSMICON),GetSystemMetrics(win32con.SM_CYSMICON),LR_LOADFROMFILE)
            SendMessage(self.nowhwnd,WM_SETICON,ICON_SMALL,li)
            SendMessage(self.nowhwnd,WM_SETICON,ICON_BIG,li)
            self.log("设置图标成功")
        else:
            self.log("已取消选择")
    def stopCap(self):
        try:
            self.captimer.stop()
            self.captimer.deleteLater()
            self.floatwin.close()
            self.log("捕获窗口完毕")
            self.hk.unregister(("control","alt","p"))
            self.capWindow.setEnabled(1)
            self.hideThisWindow.setEnabled(1)
            self.topThisWindow.setEnabled(1)
            self.killThisWindow.setEnabled(1)
            self.changeThisWindowTitle.setEnabled(1)
            self.newWindowTitle.setEnabled(1)
            self.resetTitle.setEnabled(1)
            self.changeNormalIcon.setEnabled(1)
            self.openFolderIcon.setEnabled(1)
            self.resetIcon.setEnabled(1)
            hwnd=GetForegroundWindow()
            self.nowhwnd=hwnd
            self.oldname=GetWindowText(hwnd)
            self.oldiconbig=SendMessage(hwnd,WM_GETICON,ICON_BIG,0)
            self.oldiconsmall=SendMessage(hwnd,WM_GETICON,ICON_SMALL,0)
            pid=GetWindowThreadProcessId(hwnd)[1]
            pids=process_iter()
            procname=""
            for p in pids:
                if(p.pid==pid):
                    procname=p.name()
                    break
            self.textBrowser_2.setPlainText(f"窗口标题：{GetWindowText(hwnd)}\n窗口类名：{GetClassName(hwnd)}\n窗口位置：{str(GetWindowRect(hwnd))}\n窗口句柄：{int(hwnd)}\n窗口进程：{procname}")
            if not GetWindowLong(hwnd,GWL_EXSTYLE) & WS_EX_TOPMOST:
                self.topThisWindow.setText("置顶此窗口")
            else: self.topThisWindow.setText("取消置顶此窗口")
        except: pass
    def switchWindowVisiable(self):
        if self.checkBox_4.isChecked():
            windll.user32.SetWindowDisplayAffinity(int(self.winId()),0)
        else:
            windll.user32.SetWindowDisplayAffinity(int(self.winId()),0x00000011)
    def showProgress(self):
        if self.pro==100:
            self.ttt.stop()
            self.progressBar.hide()
            self.widget.show()
            self.pushButton.setText("下载完毕")
        self.progressBar.setValue(int(self.pro))
        if self.sp<1: self.progressBar.setFormat(f"%p% {int(self.sp*1024)}KB/s")
        else: self.progressBar.setFormat(f"%p% {round(self.sp,2)}MB/s ")
        # elif self.pro<80:
        #     self.pro+=random()*randint(1,3)
        #     self.progressBar.setValue(int(self.pro))
        # elif self.pro<95:
        #     self.pro+=randint(1,10)/100
        #     self.progressBar.setValue(int(self.pro))
        # elif self.pro<99:
        #     QApplication.processEvents()
        #     self.ttt.stop()
        #     t=time.time()
        #     while(time.time()-t<=1):
        #         QApplication.processEvents()
        #     self.pro=99
        #     self.progressBar.setValue(int(self.pro))
        #     t=time.time()
        #     while(time.time()-t<=1):
        #         QApplication.processEvents()
        #     self.ttt.start()
        # elif self.pro==99:
        #     self.progressBar.setValue(int(selrandomf.pro))
        #     self.pushButton.setText("校验文件中...")
        #     self.progressBar.setMaximum(0)
        #     self.progressBar.setTextVisible(0)
    def forceFull(self):
        try:
            hwnd=FindWindow(0,"屏幕广播")
            if hwnd and "Afx:" in GetClassName(hwnd):
                if GetWindowRect(hwnd)!=GetWindowRect(GetDesktopWindow()):
                    EnumChildWindows(hwnd,self.EnumChildWindowsProc4,LPARAM)
                    self.log("强制全屏成功")
                    return
                else: self.log("强制全屏仅在广播非全屏时有效")
            else: EnumWindows(self.cb5,0)
        except:
            self.log("强制全屏失败")
    def getUpdate(self):
        try:
            self.updver=urllib.request.urlopen("http://ntdupdapi.yisous.xyz/latest").read().decode()
            self.label_9.setText("最新版本："+self.updver)
            self.updlog=urllib.request.urlopen("http://ntdupdapi.yisous.xyz/updlog").read().decode()
            self.cl=int(urllib.request.urlopen(f"https://npm.elemecdn.com/ntdupdapi@latest/NoTopDomain%20{self.updver}.exe").info()["Content-Length"])
            self.gud.emit()
        except: pass
    def hidelb(self):
        self.topLabel.hide()
        self.tltimer.stop()
        try:
            SetForegroundWindow(self.hh)
        except: pass
    def hidelb2(self):
        try:
            self.topLabel2.hide()
            self.tl2timer.stop()
        except: pass
    def unRemoteControl(self):
        if windll.shell32.IsUserAnAdmin():
            
            QApplication.processEvents()
            if self.NoControl.isChecked():
                self.warning("注意","开启了可能会掉线（在老师面前当场寄掉）\n一定要适度使用，如果发现问题可以马上关掉！qwq")
                try:
                    QApplication.processEvents()
                    run('sc config MpsSvc start= auto',shell=True)
                    QApplication.processEvents()
                    run('net start MpsSvc',shell=True)
                    QApplication.processEvents()
                    run('netsh advfirewall set allprofiles state on',shell=True)
                    QApplication.processEvents()
                    run('netsh advfirewall firewall set rule name="StudentMain.exe" new action=block',shell=True)
                    self.log("拦截成功")
                except:
                    self.log("拦截失败")
                    self.NoControl.setChecked(0)
            else:
                try:
                    QApplication.processEvents()
                    run('netsh advfirewall set allprofiles state off',shell=True)
                    QApplication.processEvents()
                    run('netsh advfirewall firewall set rule name="StudentMain.exe" new action=allow',shell=True)
                    self.log("恢复成功")
                except:
                    self.log("恢复失败")
                    self.NoControl.setChecked(0)
        else:
            self.log("请以管理员权限重启后运行该命令")
            self.NoControl.setChecked(0)
    def loque(self):
        for i in self.logque:
            self.log(i)
    def log(self,ls):
        if self.isok:
            self.logLabel.setText("ℹ "+ls)
            self.logLabel.setMaximumWidth(600)
            self.logLabel.setWordWrap(0)
            self.logLabel.adjustSize()
            self.logLabel.setAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
            self.logLabel.setGeometry(self.width()/2-self.logLabel.width()/2,self.height()-150,self.logLabel.width(),self.logLabel.height())
            self.logpro.setGeometry(self.logLabel.x()+18,self.logLabel.y()+self.logLabel.height()-2,self.logLabel.width()-36,2)
            self.logLabel.show()
            self.logpro.show()
            self.logtim=0
            self.logTimer.start()
        else:
            self.logque.append(ls)
        if DEBUG:
            try: print(ls)
            except: pass
        self.logger.write(("[%s] %s\n"%(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),ls)).encode())
    def question(self,title,text,yes="确定(&Y)",no="取消(&N)",x=-1,y=-1):
        box=QMessageBox(self)
        if x!=-1 and y!=-1:
            box.setGeometry(x,y,box.width(),box.height())
        box.setText(text)
        box.setWindowTitle(title)
        box.setIcon(QMessageBox.Question)
        box.setWindowOpacity(self.windowOpacity())
        y=self.tr(yes)
        box.addButton(y, QMessageBox.YesRole)
        box.addButton(self.tr(no), QMessageBox.NoRole)
        if self.checkBox_4.isChecked():
            windll.user32.SetWindowDisplayAffinity(int(box.winId()),0)
        else:
            windll.user32.SetWindowDisplayAffinity(int(box.winId()),0x11)
        r=box.exec()
        if r==0: return 16384
        else: return 0
    def information(self,title,text,button="好的"):
        box=QMessageBox(self)
        box.setText(text)
        box.setWindowTitle(title)
        box.setIcon(QMessageBox.Information)
        box.addButton(self.tr(button),QMessageBox.YesRole)
        box.setWindowOpacity(self.windowOpacity())
        box.show()
        if self.checkBox_4.isChecked():
            windll.user32.SetWindowDisplayAffinity(int(box.winId()),0)
        else:
            windll.user32.SetWindowDisplayAffinity(int(box.winId()),0x11)
    def warning(self,title,text,button="我已知悉"):
        box=QMessageBox(self)
        box.setText(text)
        box.setWindowTitle(title)
        box.setIcon(QMessageBox.Warning)
        box.addButton(self.tr(button),QMessageBox.YesRole)
        box.setWindowOpacity(self.windowOpacity())
        box.show()
        if self.checkBox_4.isChecked():
            windll.user32.SetWindowDisplayAffinity(int(box.winId()),0)
        else:
            windll.user32.SetWindowDisplayAffinity(int(box.winId()),0x11)
    def unHook(self):
        if self.UnlockTDHook.isChecked():
            if self.question("警告","本程序可能因此炸掉，而且貌似没多大用（？）要用的话也不是不行？")==16384:
                try:
                    if self.config.get("UseNTSD"):
                        Popen(self.ntsd+" -c q -pn prochelper64.exe ",shell=True,stdout=PIPE,stderr=PIPE)
                        Popen(self.ntsd+" -c q -pn prochelper32.exe ",shell=True,stdout=PIPE,stderr=PIPE)
                        self.log("解Hook成功")
                        return
                    elif self.config.get("UseThr"):
                        pids=process_iter()
                        for p in pids:
                            if p.name().lower()=="prochelper64.exe" or p.name().lower()=="prochelper32.exe":
                                if Tools.KillProcessByThread(p.pid)!=1:
                                    raise Exception
                    else:
                        pids=process_iter()
                        for p in pids:
                            if p.name().lower()=="prochelper64.exe" or p.name().lower()=="prochelper32.exe":
                                handle=OpenProcess(PROCESS_TERMINATE,0,p.pid)
                                TerminateProcess(handle,0)
                                self.log("解Hook成功")
                                return
                    try:
                        hook=GetModuleHandle("LibTDProcHook64.dll")
                        FreeLibrary(hook)
                        self.log("解Hook成功")
                    except:
                        hook=GetModuleHandle("LibTDProcHook32.dll")
                        FreeLibrary(hook)
                        self.log("解Hook成功")
                except:
                    self.log("并未开启防杀或解除失败")
                    self.UnlockTDHook.setChecked(0)
            else:
                self.UnlockTDHook.setChecked(0)
                self.log("放弃解防杀")
        else:
            try:
                os.startfile(self.location+"prochelper64.exe")
                self.log("恢复成功")
            except:
                try:
                    os.startfile(self.location+"prochelper32.exe")
                    self.log("恢复成功")
                except:
                    self.log("恢复失败")
    def uninstallTopDomain(self):
        try:
            self.log("调用自动卸载...")
            os.startfile(self.location+"unins000.exe")
            Sleep(1000)
            keybd_event(0xff0d,0,0,0)
            Sleep(100)
            keybd_event(0xff0d,0,KEYEVENTF_KEYUP,0)
            hwnd=FindWindow(0,"输入卸载密码")
            EnumChildWindows(hwnd,self.cb3,LPARAM)
            self.vv.emit(hwnd)
        except:
            self.log("调用卸载程序失败")
    def verifyUnis(self,hwnd):
        if self.question("提示","确定卸载极域吗？请注意您的生命安全！")==16384:
            try:
                SetForegroundWindow(hwnd)
                EnumChildWindows(hwnd,self.cb4,LPARAM)
                self.log("卸载成功")
            except:
                self.log("卸载失败")
        else:
            SendMessage(hwnd,WM_CLOSE,0,0)
            self.log("放弃卸载")
    def cb3(self,hwnd,lp):
        if GetClassName(hwnd)=="Edit":
            SendMessage(hwnd,WM_SETTEXT,0,self.TDPasswd.text()[:-1])
    def cb4(self,hwnd,lp):
        if GetWindowText(hwnd)=="确定":
            SendMessage(hwnd,WM_LBUTTONDOWN,MK_LBUTTON,0)
            SendMessage(hwnd,WM_LBUTTONUP,MK_LBUTTON,0)
    def closeGB(self):
        if self.question("警告","确定关闭广播窗口吗？此操作不可逆！\n（其实你可以重启极域的...）",x=GetWindowRect(GetForegroundWindow())[0]+50,y=GetWindowRect(GetForegroundWindow())[1]+100)==16384:
            PostMessage(tdgbhwnd, WM_SYSCOMMAND, SC_CLOSE, 0)
            self.log("关闭广播窗口成功")
            self.tray.showMessage("NoTopDomain","关闭广播窗口成功",QSystemTrayIcon.NoIcon,msecs=1000)
    def reTrayState(self):
        if self.checkBox.isChecked():
            self.tray.hide()
        else:
            self.tray.show()
    def toHelp(self):
        self.shownormal()
        self.setFocus()
        self.PigeonGames.setCurrentIndex(3)
    def toSetting(self):
        self.shownormal()
        self.setFocus()
        self.PigeonGames.setCurrentIndex(1)
    def restart(self):
        os.chdir(bl)
        if ff==2 or DEBUG:
            Popen(" ".join(Process(os.getpid()).cmdline()),shell=True,stdout=PIPE,stderr=PIPE)
        else:
            os.startfile(os.getenv("temp")+"\\NTDUIALoader.exe")
        os._exit(0)
    def EnumChildWindowsProc3(self,hwndChild,lParam):
        EnableWindow(hwndChild)
    def EnumChildWindowsProc2(self,hwndChild,lParam):
        hmenu=GetMenu(hwndChild)
        if LOWORD(hmenu)==1004:
            if IsWindowEnabled(hwndChild):
                self.GBWindowed.setText("禁用\n全屏")
            else:
                self.GBWindowed.setText("解冻\n全屏")
                if not window.IamTop.isChecked():
                    window.IamTop.click()
    def startTSK(self):
        os.startfile("taskmgr")
        QApplication.processEvents()
        self.cnt=0
        self.ttimer.setInterval(200)
        self.ttimer.timeout.connect(self.TSK)
        self.ttimer.start()
    def TSK(self):
        if(self.cnt>20):
            self.log("置顶尝试超时")
            self.ttimer.stop()
            return
        hwnd=FindWindow("TaskManagerWindow","任务管理器")
        if(hwnd):
            self.ttimer.stop()
        try:
            hm=GetMenu(hwnd)
            mii,_=EmptyMENUITEMINFO()
            GetMenuItemInfo(hm,0x7704,False,mii)
            if(list(UnpackMENUITEMINFO(mii))[1]==0):
                PostMessage(hwnd,WM_COMMAND,0x7704,0)
            self.log("启动并勾选置顶任务管理器，完毕")
        except:
            try:
                SetWindowPos(hwnd,HWND_TOPMOST,0,0,0,0,SWP_NOSIZE|SWP_NOMOVE)
                self.log("启动并外挂置顶任务管理器，完毕（优先级较低）")
            except:
                self.log("似乎任务管理器不可以置顶（Win1122H2?）")
    def EnableFullScreen(self):
        try:
            hwnd=FindWindow(0,"屏幕广播")
            self.h=hwnd
            if hwnd and "Afx:" in GetClassName(hwnd):
                EnumChildWindows(hwnd,self.EnumChildWindowsProc,LPARAM)
                self.log("解禁按钮成功")
                return
            else:
                EnumWindows(self.cb2,0)
        except:
            self.log("解禁失败")
    def copyLink(self):
        run("echo "+self.location+" | clip",shell=True)
        self.log("复制链接成功")
    def cb2(self,hwnd,lParam):
        if "正在共享屏幕" in GetWindowText(hwnd) and "Afx:" in GetClassName(hwnd):
            self.h=hwnd
            EnumChildWindows(hwnd,self.EnumChildWindowsProc,LPARAM)
            self.log("解禁按钮成功")
        return 1
    def cb5(self,hwnd,lParam):
        if "正在共享屏幕" in GetWindowText(hwnd) and "Afx:" in GetClassName(hwnd):
            self.h=hwnd
            if GetWindowRect(hwnd)!=GetWindowRect(GetDesktopWindow()):
                EnumChildWindows(hwnd,self.EnumChildWindowsProc4,LPARAM)
            self.log("恢复全屏成功")
        return 1
    def EnumChildWindowsProc4(self,hwndChild,lParam):
        hmenu=GetMenu(hwndChild)
        if LOWORD(hmenu)==1004:
            t=IsWindowEnabled(hwndChild)
            EnableWindow(hwndChild,TRUE)
            SendMessage(hwndChild,WM_LBUTTONDOWN,MK_LBUTTON,0)
            SendMessage(hwndChild,WM_LBUTTONUP,MK_LBUTTON,0)
            EnableWindow(hwndChild,t)
            return 0
        return 1
    def EnumChildWindowsProc(self,hwndChild,lParam):
        hmenu=GetMenu(hwndChild)
        if LOWORD(hmenu)==1004:
            if not IsWindowEnabled(hwndChild):
                EnableWindow(hwndChild,TRUE)
                if self.config.get("AutoCommand"):
                    if GetWindowRect(self.h)==GetWindowRect(GetDesktopWindow()):
                        # PostMessage(hwndChild,WM_COMMAND,WPARAM((BM_CLICK<<16)|1004),NULL)
                        # x,y=GetCursorPos()
                        # g=GetWindowRect(hwndChild)
                        # SetCursorPos((g[0]+10,g[1]+10))
                        # Sleep(250)
                        # g=GetWindowRect(hwndChild)
                        # SetCursorPos((g[0]+10,g[1]+10))
                        # mouse_event(MOUSEEVENTF_LEFTDOWN|MOUSEEVENTF_ABSOLUTE,0,0)
                        # Sleep(50)
                        # mouse_event(MOUSEEVENTF_LEFTUP|MOUSEEVENTF_ABSOLUTE,0,0)
                        # SetCursorPos((x,y))
                        # 睿智
                        SendMessage(hwndChild,WM_LBUTTONDOWN,MK_LBUTTON,0)
                        SendMessage(hwndChild,WM_LBUTTONUP,MK_LBUTTON,0)
                        # YYDS
                self.GBWindowed.setText("禁用\n全屏")
                self.log("解禁按钮成功")
                return 0
            else:
                if self.config.get("AutoCommand"):
                    if GetWindowRect(self.h)!=GetWindowRect(GetDesktopWindow()):
                        # PostMessage(hwndChild,WM_COMMAND,WPARAM((BM_CLICK<<16)|1004),NULL)
                        # x,y=GetCursorPos()
                        # g=GetWindowRect(hwndChild)
                        # SetCursorPos((g[0]+10,g[1]+10))
                        # g=GetWindowRect(hwndChild)
                        # SetCursorPos((g[0]+10,g[1]+10))
                        # Sleep(250)
                        # mouse_event(MOUSEEVENTF_LEFTDOWN|MOUSEEVENTF_ABSOLUTE,0,0)
                        # Sleep(150)
                        # mouse_event(MOUSEEVENTF_LEFTUP|MOUSEEVENTF_ABSOLUTE,0,0)
                        # SetCursorPos((x,y))
                        # 睿智
                        SendMessage(hwndChild,WM_LBUTTONDOWN,MK_LBUTTON,0)
                        SendMessage(hwndChild,WM_LBUTTONUP,MK_LBUTTON,0)
                        # YYDS
                EnableWindow(hwndChild,FALSE)
                self.GBWindowed.setText("解冻\n全屏")
                self.log("禁用按钮成功")
                return 0
        return 1
    def gudone(self):
        try:
            self.plainTextEdit.setPlainText(self.updlog)
            if self.updver==VERSION:
                self.label_11.setText("已是最新版本")
            else:
                self.label_11.setEnabled(1)
                self.pushButton.setEnabled(1)
                self.progressBar.setEnabled(1)
                self.label_11.setText(f"大小：{str(round(self.cl/1024/1024,2))}MB")
        except: pass
    def loadConfig(self):
        self.PigeonGames.setCurrentIndex(1)
        try:
            try:
                with open(os.getenv("temp")+"\\NTDConfig.json","r+") as f:
                    f.seek(0)
                    self.config=load(f)
            except:
                with open(os.getenv("temp")+"\\NTDConfig.json","w+") as f:
                    self.config={"HideTrayIcon":False,"AutoCommand":False,
                         "NoRandomTitle":False,"QssDisabled":False,
                         "UseNTSD":False,"WindowVisible":False,"UseThr":False,
                         "AcWindow":"alt+m","HideWindow":"alt+h",
                         "TopWindow":"alt+y","KillWindow":"alt+k",
                         "Switch":"alt+q","ForceFull":"alt+f"}
                    f.seek(0)
                    dump(self.config,f)
            try:
                with open(os.getenv("temp")+"\\NTDHooksConfig","r") as f:
                    if f.read().split()[0]=="1":
                        self.checkBox_6.setChecked(1)
                    f.seek(0)
                    if f.read().split()[1]=="1":
                        self.checkBox_7.setChecked(1)
            except:
                try:
                    with open(os.getenv("temp")+"\\NTDHooksConfig","w+") as f:
                        f.write("0 0")
                except: pass
            if self.config.get("HideTrayIcon"):
                self.checkBox.setChecked(1)
            if self.config.get("AutoCommand"):
                self.checkBox_2.setChecked(1)
            # if self.config.get("QssDisabled"):
            #     self.QSSDis.setChecked(1)
            if self.config.get("WindowVisible"):
                self.checkBox_4.setChecked(1)
            else:
                self.switchWindowVisiable()
            if self.config.get("NoRandomTitle"):
                self.checkBox_5.setChecked(1)
                global flag6
                flag6=0
            if self.config.get("UseNTSD"):
                self.radioButton_2.setChecked(1)
            elif self.config.get("UseThr"):
                self.radioButton_3.setChecked(1)
            else:
                self.radioButton.setChecked(1)
            self.showWindowHotKey.setText(self.config.get("AcWindow").upper())
            self.TSKHotKey.setText(self.config.get("HideWindow").upper())
            self.topFocusHotKey.setText(self.config.get("TopWindow").upper())
            self.killFocusHotKey.setText(self.config.get("KillWindow").upper())
            self.GBWindowSwitchHotKey.setText(self.config.get("Switch").upper())
            self.ForceFullHotKey.setText(self.config.get("ForceFull").upper())
        except:
            self.config={"HideTrayIcon":False,"AutoCommand":False,
                         "NoRandomTitle":False,"QssDisabled":False,
                         "UseNTSD":False,"WindowVisible":False,"UseThr":False,
                         "AcWindow":"alt+m","HideWindow":"alt+h",
                         "TopWindow":"alt+y","KillWindow":"alt+k",
                         "Switch":"alt+q","ForceFull":"alt+f"}
            self.switchWindowVisiable()
        self.PigeonGames.setCurrentIndex(0)
    def saveConfig(self):
        keys=("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w",
              "x","y","z","0","1","2","3","4","5","6","7","8","9","ctrl","alt","control","shift","esc",
              "f1","f2","f3","f4","f5","f6","f7","f8","f9","f10","f11","f12")
        for k in self.showWindowHotKey.text().lower().split("+"):
            if not (k in keys):
                self.log("唤起窗口快捷键设置不合法")
                return
        for k in self.TSKHotKey.text().lower().split("+"):
            if not (k in keys):
                self.log("任务管理器快捷键设置不合法")
                return
        for k in self.topFocusHotKey.text().lower().split("+"):
            if not (k in keys):
                self.log("置顶窗口快捷键设置不合法")
                return
        for k in self.killFocusHotKey.text().lower().split("+"):
            if not (k in keys):
                self.log("杀掉焦点快捷键设置不合法")
                return
        for k in self.GBWindowSwitchHotKey.text().lower().split("+"):
            if not (k in keys):
                self.log("窗口化切换快捷键设置不合法")
                return
        for k in self.ForceFullHotKey.text().lower().split("+"):
            if not (k in keys):
                self.log("强制广播全屏快捷键设置不合法")
                return
        try:
            self.config["HideTrayIcon"]=self.checkBox.isChecked()
            self.config["AutoCommand"]=self.checkBox_2.isChecked()
            # self.config["QssDisabled"]=self.QSSDis.isChecked()
            self.config["WindowVisible"]=self.checkBox_4.isChecked()
            self.config["NoRandomTitle"]=self.checkBox_5.isChecked()
            self.config["UseNTSD"]=self.radioButton_2.isChecked()
            self.config["UseThr"]=self.radioButton_3.isChecked()
            self.config["AcWindow"]=self.showWindowHotKey.text().lower()
            self.config["HideWindow"]=self.TSKHotKey.text().lower()
            self.config["TopWindow"]=self.topFocusHotKey.text().lower()
            self.config["KillWindow"]=self.killFocusHotKey.text().lower()
            self.config["Switch"]=self.GBWindowSwitchHotKey.text().lower()
            self.config["ForceFull"]=self.ForceFullHotKey.text().lower()
            with open(os.getenv("temp")+"\\NTDConfig.json","w+") as f:
                dump(self.config,f)
            with open(os.getenv("temp")+"\\NTDHooksConfig","w+") as f:
                if self.checkBox_6.isChecked():
                    f.write("1 ")
                else: f.write("0 ")
                if self.checkBox_7.isChecked():
                    f.write("1 ")
                else: f.write("0 ")
            self.log("保存成功（重启生效）")
        except:
            self.log("保存失败")
    def closeEvent(self,event):
        # self.moyu.close()
        # self.gjW.close()
        if DEBUG:
            event.accept()
            try:
                self.tray.hide()
                self.logger.close()
            except:
                pass
            os._exit(0)
        else:
            event.ignore()
            if not self.trfl:
                self.tray.showMessage("NoTopDomain","窗口已隐藏到托盘，请右键或双击唤起",0,msecs=1000)
                self.trfl=1    
            self.hide()
    def keyPressEvent(self,event):
        event.accept()
        if event.key()==16777220 and self.KillSome.hasFocus():
            self.killCurrent()
        if event.key()==16777220 and self.Run.hasFocus() and self.Run.text():
            self.runCurrent()
    def runCurrent(self):
        try: 
            os.startfile(self.Run.text())
            self.log(f"运行 {self.Run.text()} 成功")
        except Exception as e: self.log(f"运行失败 {e}")
    def killFocus(self,mode=0):
        try:
            if(mode):
                hwnd=self.nowhwnd
            else: hwnd=GetForegroundWindow()
            pid=GetWindowThreadProcessId(hwnd)[1]
            if(pid==os.getpid()):
                self.log("触发进程保护...")
                return
            x,y,_,__=GetWindowRect(hwnd)
            if self.question("提示","确定要杀掉焦点进程吗？\n%s PID："%Process(pid).name()+str(pid),x=x+20,y=y+70)==16384:
                if self.config.get("UseNTSD"):
                    Popen(self.ntsd+" -c q -p %d"%pid,shell=True,stdout=PIPE,stderr=PIPE)
                elif self.config.get("UseThr"):
                    if not Tools.KillProcessByThread(pid):
                        raise Exception
                else:
                    handle=OpenProcess(PROCESS_TERMINATE,0,pid)
                    TerminateProcess(handle,0)
                self.log("已经杀掉焦点窗口，PID："+str(pid))
                self.tray.showMessage("NoTopDomain","已经杀掉焦点窗口，PID："+str(pid),QSystemTrayIcon.NoIcon,msecs=1000)
            if self.isHidden():
                self.shownormal()
                self.hide()
        except:
            self.log("杀窗口失败")
            self.tray.showMessage("NoTopDomain","杀掉焦点窗口失败",QSystemTrayIcon.NoIcon,msecs=1000)
    def enableTools(self):
        self.information("提示","以下工具/功能将被解禁：\n1.修改密码\n2.注册表编辑器\n3.切换用户\n4.任务管理器\n5.Autorun\n6.注销/开始菜单选项\n7.运行")
        try:
            flag=0
            fails=[]
            reg=RegOpenKeyEx(HKEY_CURRENT_USER,r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System',0,KEY_ALL_ACCESS)
            dises=["DisableChangePassword","DisableRegistryTools","DisableSwitchUserOption","DisableTaskMgr"]
            for i in dises:
                try:
                    RegSetValueEx(reg,i,0,REG_DWORD,0)
                except:
                    flag=1
                    fails.append(i)
            reg.Close()
            reg=RegOpenKeyEx(HKEY_CURRENT_USER,r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer',0,KEY_ALL_ACCESS)
            dises=["NoDriveTypeAutoRun","NoLogOff","NoRun","StartMenuLogOff"]
            for i in dises:
                try:
                    RegSetValueEx(reg,i,0,REG_DWORD,0)
                except:
                    flag=1
                    fails.append(i)
            reg.Close()
            if(flag):
                self.log("部分项目解禁失败："+" ".join(fails))
            else:
                self.log("解禁成功")
        except:
            self.log("解禁失败，请尝试以管理员权限启动")
    def restartExplorer(self):
        pids=process_iter()
        for p in pids:
            if(p.name().lower()=="explorer.exe"):
                handle=OpenProcess(PROCESS_TERMINATE,0,p.pid)
                TerminateProcess(handle,0)
        self.log("重启成功")
    def noImg(self):
        s=self.question("警告","重置映像劫持不可逆，是否继续？")
        if(s==16384):
            try:
                reg=RegOpenKeyEx(HKEY_LOCAL_MACHINE,r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options',0,KEY_ALL_ACCESS)
                for item in RegEnumKeyEx(reg):
                    try:
                        r=RegOpenKeyEx(HKEY_LOCAL_MACHINE,r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\\'+item[0],0,KEY_ALL_ACCESS)
                        RegQueryValueEx(r,"debugger")
                    except:
                        pass
                    else:
                        RegDeleteKey(RegOpenKeyEx(HKEY_LOCAL_MACHINE,r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options',0,KEY_ALL_ACCESS),item[0])
                        r.Close()
                self.log("解除成功")
            except:
                self.log("解除失败，尝试以System权限重启？")
        else:
            self.log("放弃解除")
    def ZB(self):
        self.zb.stop()
        try:
            self.UninstallTopDomain.setEnabled(1)
            try:
                reg=RegOpenKeyEx(HKEY_LOCAL_MACHINE,r'SOFTWARE\WOW6432Node\TopDomain\e-Learning Class Standard\1.00')
                r=RegQueryValueEx(reg,"UninstallPasswd")
                if r[1] and r[0]!='Passwd[123456]':
                    self.TDPasswd.setText(r[0][7:-1])
                    self.TDPasswd.setCursorPosition(0)
                    return
            except:
                try:
                    reg=RegOpenKeyEx(HKEY_LOCAL_MACHINE,r'SOFTWARE\TopDomain\e-Learning Class Standard\1.00')
                    r=RegQueryValueEx(reg,"UninstallPasswd")
                    if r[1] and r[0]!='Passwd[123456]':
                        self.TDPasswd.setText(r[0][7:-1])
                        self.TDPasswd.setCursorPosition(0)
                        return
                except: pass
            Tools.GetMythwarePasswordFromRegedit()
            with open(os.getenv("temp")+"\\NTDPwd.key",encoding="utf-8") as f:
                t=f.read()
                if t[0]=='n': t=t[1:]
                self.TDPasswd.setText(t)
                self.TDPasswd.setCursorPosition(0)
        except:
            if self.location:
                self.TDPasswd.setText("mythware_super_password")
                self.TDPasswd.setCursorPosition(0)
            else:
                self.TDPasswd.setText("未找到极域")
                self.TDPasswd.setCursorPosition(0)
    def showHelp(self):
        try:
            self.textBrowser.setMarkdown(base64.b64decode(helpMD).decode().format(VERSION,self.config.get("AcWindow").upper(),self.config.get("KillWindow").upper(),self.config.get("HideWindow").upper(),self.config.get("TopWindow").upper(),self.config.get("ForceFull").upper(),self.config.get("Switch").upper()))
        except:
            self.textBrowser.setMarkdown(base64.b64decode(helpMD).decode().format(VERSION,"ALT+M","ALT+K","ALT+H","ALT+Y","ALT+F","ALT+Q"))
    def killCurrent(self):
        if self.KillSome.text():
            if self.question("提示","确定杀掉输入进程吗？ %s"%self.KillSome.text())==16384:
                try:
                    if self.KillSome.text().isdigit():
                        if self.config.get("UseNTSD"):
                            Popen(self.ntsd+" -c q -p %s"%self.KillSome.text(),shell=True,stdout=PIPE,stderr=PIPE)
                            self.log("执行成功")
                            return
                        elif self.config.get("UseThr"):
                            if not Tools.KillProcessByThread(int(self.KillSome.text())):
                                raise Exception
                            else:
                                self.log("执行成功")
                                return
                        else:
                            handle=OpenProcess(PROCESS_TERMINATE,0,int(self.KillSome.text()))
                            TerminateProcess(handle,0)
                            return
                    else:
                        if self.config.get("UseNTSD"):
                            Popen(self.ntsd+" -c q -pn %s "%(self.KillSome.text() if ".exe" in self.KillSome.text() else self.KillSome.text()+".exe"),shell=True,stdout=PIPE,stderr=PIPE)
                            self.log("执行成功")
                            return
                        elif self.config.get("UseThr"):
                            pids=process_iter()
                            for p in pids:
                                if p.name().lower()==self.KillSome.text() or p.name().lower()==self.KillSome.text()+".exe":
                                    if Tools.KillProcessByThread(p.pid,0):
                                        self.log("执行成功")
                                    else:
                                        raise Exception
                        else:
                            flag=0
                            pids=process_iter()
                            for p in pids:
                                if p.name().lower()==self.KillSome.text() or p.name().lower()==self.KillSome.text()+".exe":
                                    handle=OpenProcess(PROCESS_TERMINATE,0,p.pid)
                                    TerminateProcess(handle,0)
                                    self.log("执行成功")
                                    flag=1
                            if flag:
                                return
                except:
                    self.log("杀进程失败，检查进程名？")
    def noShutDown(self):
        if self.NoShutdown.isChecked():
            try:
                with open(self.location+"shutdown.exe","rb+") as f:
                    with open(self.location+"Shutdown_back.exe","wb+") as f2:
                        f2.write(f.read())
                    f.seek(0)
                    f.write(b64decode(emptyexe))
                self.log("关机程序补丁注入成功")
            except:
                self.log("注入失败，未找到极域")
        else:
            try:
                with open(self.location+"Shutdown_back.exe","rb+") as f:
                    with open(self.location+"Shutdown.exe","wb+") as f2:
                        f2.write(f.read())
                os.remove(self.location+"shutdown_back.exe")
                self.log("关机程序恢复成功")
            except:
                self.log("恢复失败，未找到极域")
    def websiteYes(self):
        if self.WebsiteYes.isChecked():
            try:
                if self.config.get("UseNTSD"):
                    Popen(self.ntsd+" -c q -pn gatesrv.exe",shell=True,stdout=PIPE,stderr=PIPE)
                    Popen(self.ntsd+" -c q -pn masterhelper.exe",shell=True,stdout=PIPE,stderr=PIPE)
                elif self.config.get("UseThr"):
                    pids=process_iter()
                    for p in pids:
                        if p.name().lower()=="gatesrv.exe" or p.name().lower()=="masterhelper.exe":
                            if not Tools.KillProcessByThread(p.pid):
                                raise Exception
                else:
                    pids=process_iter()
                    for p in pids:
                        if p.name().lower()=="gatesrv.exe" or p.name().lower()=="masterhelper.exe":
                            handle=OpenProcess(PROCESS_TERMINATE,0,p.pid)
                            TerminateProcess(handle,0)
                run("sc stop TDNetFilter",shell=True,stdout=PIPE)
                try:
                    run("sc stop TDNetworkFilter",shell=True,stdout=PIPE)
                except: pass
                self.log("解禁网站成功")
            except Exception as e:
                print(e)
                self.log("解禁网站失败")
        else:
            try:
                os.startfile(self.location+"gatesrv.exe")
                os.startfile(self.location+"masterhelper.exe")
                run("sc start TDNetFilter",shell=True,stdout=PIPE)
                self.log("恢复禁网成功")
            except:
                self.log("恢复禁网失败")
    def Feedback(self):
        self.fb.show()
    def setTop(self,mode=0):
        if not mode:
            hwnd=GetForegroundWindow()
        else: hwnd=self.nowhwnd
        if int(self.winId())==hwnd or self.topLabel.isActiveWindow() or self.moyu.isActiveWindow():
            self.log("触发进程保护...")
            return
        try:
            if not IsWindow(hwnd): raise Exception
            if not GetWindowLong(hwnd,GWL_EXSTYLE) & WS_EX_TOPMOST:
                self.hh=hwnd
                self.topLabel.setText("置顶窗口")
                self.topLabel.show()
                if self.checkBox_4.isChecked():
                    windll.user32.SetWindowDisplayAffinity(int(self.topLabel.winId()),0)
                else:
                    windll.user32.SetWindowDisplayAffinity(int(self.topLabel.winId()),0x11)
                SetWindowPos(hwnd,HWND_TOPMOST,0,0,0,0,SWP_NOMOVE|SWP_NOSIZE)
                x,y,_,__=GetWindowRect(hwnd)
                SetWindowPos(self.topLabel.winId(),HWND_TOPMOST,x+10,y+10,0,0,SWP_NOSIZE)
                self.tltimer.start()
                self.log("置顶选中窗口成功，hwnd:%d"%hwnd)
            else:
                self.hh=hwnd
                self.topLabel.setText("取消置顶")
                self.topLabel.show()
                SetWindowPos(hwnd,HWND_NOTOPMOST,0,0,0,0,SWP_NOMOVE|SWP_NOSIZE)
                x,y,_,__=GetWindowRect(hwnd)
                SetWindowPos(self.topLabel.winId(),HWND_TOPMOST,x+10,y+10,0,0,SWP_NOSIZE)
                if self.checkBox_4.isChecked():
                    windll.user32.SetWindowDisplayAffinity(int(self.topLabel2.winId()),0)
                else:
                    windll.user32.SetWindowDisplayAffinity(int(self.topLabel2.winId()),0x11)
                self.tltimer.start()
                self.log("取消置顶选中窗口，hwnd:%d"%hwnd)
            if mode:
                if self.topThisWindow.text()=="置顶此窗口":
                    self.topThisWindow.setText("取消置顶")
                elif self.topThisWindow.text()=="取消置顶":
                    self.topThisWindow.setText("置顶此窗口")
        except:
            self.log("置顶窗口失败")
    def nbs(self):
        global flag3
        if flag3:
            self.log("恢复黑屏成功")
        else:
            self.log("启动黑屏屏蔽")
        flag3=not flag3
    def usbYes(self):
        if windll.shell32.IsUserAnAdmin():
            if self.USBYes.isChecked():
                run("sc stop TDFileFilter",shell=True,stdout=PIPE)
                self.log("解禁USB成功")
            else:
                run("sc start TDFileFilter",shell=True,stdout=PIPE)
                self.log("恢复USB成功")
        else:
            self.USBYes.setChecked(0)
            self.log("请使用管理员权限运行程序")
    def toTop(self):
        global flag
        if not self.IamTop.isChecked():
            flag=0
            self.log("取消置顶")
        else:
            flag=1
            self.log("置顶完毕") 
    def activate(self,reason):
        if reason == QSystemTrayIcon.DoubleClick:
            self.showWindow()
    def enableMouse(self):
        global flag4
        if self.MouseYes.isChecked():
            flag4=1
            self.log("解鼠标锁成功，注意可能会卡顿")
        else:
            flag4=0
            self.log("恢复鼠标锁成功，注意可能会卡顿")
    def enableKeyboard(self):
        global flag2
        if self.KeyboardYes.isChecked():
            flag2=0
            self.log("解键盘锁成功")
        else:
            flag2=1
            self.log("恢复键盘锁成功")
    def hangTD(self):
        if self.HangState:
            pids=process_iter()
            for p in pids:
                if(p.name().lower()=="studentmain.exe"):
                    pid=Process(p.pid)
                    break
            try:
                pid.suspend()
                self.log("挂起成功")
                self.HangState=0
                self.HangUpTD.setText("恢复\n极域")
                self.KillTD.setEnabled(False)
            except:
                self.log("挂起失败")
        else:
            pids=process_iter()
            for p in pids:
                if(p.name().lower()=="studentmain.exe"):
                    pid=Process(p.pid)
                    break
            try:
                pid.resume()
                self.log("恢复成功")
                self.HangState=1
                self.HangUpTD.setText("挂起\n极域")
                self.KillTD.setEnabled(True)
            except:
                self.log("恢复失败")
    def killTopDomain(self):
        if self.TDState:
            try:
                if self.config.get("UseNTSD"):
                    Popen(self.ntsd+" -c q -pn studentmain.exe",shell=True,stdout=PIPE,stderr=PIPE)
                elif self.config.get("UseThr"):
                    pids=process_iter()
                    for p in pids:
                        if p.name().lower()=="studentmain.exe":
                            pid=p.pid
                    if Tools.KillProcessByThread(pid)!=1:
                        raise Exception
                else:
                    pids=process_iter()
                    for p in pids:
                        if p.name().lower()=="studentmain.exe":
                            pid=p.pid
                    handle=OpenProcess(PROCESS_TERMINATE,0,pid)
                    TerminateProcess(handle,0)
                self.log("成功杀掉极域")
                self.TDState=0
                self.KillTD.setText("启动\n极域")
            except:
                self.log("杀极域失败，可能开启了防杀")
        else:
            if ff==2:
                try:
                    if self.location:
                        Popen(f"""{self.location}studentmain.exe """,stdout=PIPE,shell=True)
                        self.TDState=1
                        self.KillTD.setText("杀掉\n极域")
                        self.log("成功启动极域")
                        self.HangState=1
                        self.HangUpTD.setText("挂起\n极域")
                    else:
                        raise Exception
                except:
                    self.log("启动极域失败（地址原因？）")
            else:
                try:
                    if not self.location:
                        raise Exception
                    res=Tools.StartMythware(self.location+"studentmain.exe")
                    if not res:
                        self.TDState=1
                        self.KillTD.setText("杀掉\n极域")
                        self.log("成功启动极域")
                        self.HangState=1
                        self.HangUpTD.setText("挂起\n极域")
                    elif res==1:
                        self.log("启动极域失败（权限原因？）")
                    else:
                        self.log("启动极域失败，请检查您的资源管理器启动情况")
                except:
                    self.log("启动极域失败（地址原因？）")
    def changeEvent(self,event):
        if event.type() == QEvent.WindowStateChange:
            if self.windowState() & Qt.WindowMinimized:
                event.ignore()
                self.hide()
                return
    def showAbout(self):
        QMessageBox.about(self,'关于',"""NoTopDomain<br>%s<br>Powered By <a href="https://blog.csdn.net/weixin_42112038/article/details/127480471">极域机房工具箱1.1</a> <a href="https://github.com/imengyu/JiYuTrainer">JiYuTrainer</a> <br><a href="https://yisous.xyz">博客</a> <a href="https://luogu.com.cn/user/761305">Luogu</a> <a href="https://github.com/lyxofficial">Github</a>"""%VERSION)
    def showWindow(self):
        if self.isHidden():
            self.shownormal()
        elif not (self.isActiveWindow()) and not self.IamTop.isChecked():
            self.activateWindow()
        else:
            self.hide()
            # self.moyu.close()
            # self.gjW.close()
class UnlockKeyboard(Thread):
    def __init__(self):
        super().__init__()
    def run(self):
        while(1):
            if(flag2):
                Tools.UnlockKeyboard()
            else:
                Sleep(100)
class UnlockMouse(Thread):
    def __init__(self):
        super().__init__()
    def run(self):
        while(1):
            if(flag4):
                Tools.UnlockMouse()
            Sleep(50)
class SetWindowPref(Thread):
    def __init__(self,hwnd):
        super().__init__()
        self.hwnd=hwnd
    def run(self):
        while(1):
            if(flag):
                Tools.SetWindowPref(self.hwnd)
            else:
                Tools.SetWindowNoPref(self.hwnd)
class setState(Thread):
    def __init__(self):
        super().__init__()
    def run(self):
        global flag3,flag5,tdgbhwnd,flag6
        wt=window.windowTitle()
        pids=process_iter()
        for p in pids:
            if(p.name().lower()=="studentmain.exe"):
                window.TDState=0
                window.KillTD.setText("启动\n极域")
        while(1):
            d=GetLastError()
            if d:
                f=FormatMessage(FORMAT_MESSAGE_ALLOCATE_BUFFER | FORMAT_MESSAGE_IGNORE_INSERTS| FORMAT_MESSAGE_FROM_SYSTEM | FORMAT_MESSAGE_MAX_WIDTH_MASK,0,d, MAKELANGID(LANG_NEUTRAL, SUBLANG_DEFAULT),"")
                window.logger.write(("[%s] GetLastError: Code %d %s\n"%(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),d,f)).encode())
            if flag6:
                c=randint(1,5)
                ti=list(wt)
                for _ in range(c):
                    ti[randint(1,len(ti))-1]=choice(list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-=_+~`[]\\|{}/?><,.;': "))
                SetWindowText(window.winId(),"".join(ti))
            if not window.HangState:
                pid,s=0,1
                pids=process_iter()
                for p in pids:
                    if(p.name().lower()=="studentmain.exe"):
                        s,pid=0,p.pid
                        break
                if not s:
                    window.StudentRunning.setText("<span style=\"color:red\">挂起中</span> <span style=\"color:gray\">PID:%s</span>"%pid)
                    window.label_44.setPixmap(QIcon(qta.icon("ei.magic",color="red")).pixmap(32,32))
            else:
                pid,s=0,1
                pids=process_iter()
                for p in pids:
                    if(p.name().lower()=="studentmain.exe"):
                        s,pid=0,p.pid
                        break
                if s:
                    window.StudentRunning.setText("<span style=\"color:green\">未运行</span>")
                    window.label_44.setPixmap(QIcon(qta.icon("ei.magic",color="green")).pixmap(32,32))
                    window.HangUpTD.setEnabled(False)
                    # window.EnableTDBar.setEnabled(False)
                    window.TDState=0
                    window.KillTD.setText("启动\n极域")
                else:
                    window.StudentRunning.setText("<span style=\"color:orange\">运行中</span> <span style=\"color:gray\">PID:%s</span>"%pid)
                    window.label_44.setPixmap(QIcon(qta.icon("ei.magic",color="orange")).pixmap(32,32))
                    window.HangUpTD.setEnabled(True)
                    # window.EnableTDBar.setEnabled(True)
                    window.TDState=1
                    window.KillTD.setText("杀掉\n极域")
                    window.HangState=1
                    window.HangUpTD.setText("挂起\n极域")
            self.flag=1
            hwnd=0
            hwnd=FindWindow(0,"BlackScreen Window")
            if hwnd:
                self.flag=0
                window.GBWindowed.setText("解冻\n全屏")
                window.GBWindowed.setEnabled(False)
                window.CloseGB.setEnabled(False)
                if not flag3:
                    window.GBing.setText("<span style=\"color:purple\">黑屏安静中</span>")
                else:
                    window.GBing.setText("<span style=\"color:blue\">黑屏安静已屏蔽</span>")
            hwnd=0
            hwnd=FindWindow(0,"屏幕广播")
            if hwnd and "Afx:" in GetClassName(hwnd):
                window.GBing.setText("广播：<span style=\"color:orange\">进行中</span>")
                window.GBWindowed.setEnabled(True)
                window.CloseGB.setEnabled(True)
                flag5,tdgbhwnd=1,hwnd
                try:
                    EnumChildWindows(hwnd,window.EnumChildWindowsProc2,LPARAM)
                except:
                    pass
                self.flag=0
            else:
                EnumWindows(self.cb1,0)
            if self.flag:
                flag5=0
                window.GBing.setText("<span style=\"color:green\">未进行</span>")
                window.label_39.setPixmap(QIcon(qta.icon("ri.radar-line",color="green")).pixmap(32,32))
                window.GBWindowed.setText("解冻\n全屏")
                window.GBWindowed.setEnabled(False)
                window.CloseGB.setEnabled(False)
            if not window.TDState:
                window.NoRemoteRun.setEnabled(0)
                window.label_30.setEnabled(0)
                window.NoRemoteRun.setChecked(0)
            elif (not window.NoRemoteRun.isEnabled()) and not window.NoRemoteRun.isChecked():
                window.NoRemoteRun.setEnabled(1)
                window.label_30.setEnabled(1)
            Sleep(1000)
    def cb1(self,hwnd,lparam):
        global tdgbhwnd,flag5
        if "正在共享屏幕" in GetWindowText(hwnd) and "Afx:" in GetClassName(hwnd):
            window.GBing.setText("<span style=\"color:orange\">进行中</span>")
            window.label_39.setPixmap(QIcon(qta.icon("ri.radar-line",color="orange")).pixmap(32,32))
            window.GBWindowed.setEnabled(True)
            window.CloseGB.setEnabled(True)
            try:
                EnumChildWindows(hwnd,window.EnumChildWindowsProc2,LPARAM)
            except:
                pass
            flag5,tdgbhwnd=1,hwnd
            self.flag=0
        return 1
class NoBlackScreen(Thread):
    def __init__(self):
        super().__init__()
    def run(self):
        while(1):
            if flag3:
                hwnd=FindWindow(0,"BlackScreen Window")
                if hwnd:
                    SetWindowPos(hwnd,HWND_BOTTOM,0,0,0,0,SWP_NOSIZE|SWP_NOMOVE|SWP_HIDEWINDOW)
            else:
                hwnd=FindWindow(0,"BlackScreen Window")
                if hwnd:
                    SetWindowPos(hwnd,HWND_TOPMOST,0,0,0,0,SWP_NOSIZE|SWP_NOMOVE|SWP_SHOWWINDOW)
            Sleep(500)
def loadToolDLL():
    global ff,Tools
    def fileHash(file_path:str,hash_method) -> str:
        if not os.path.exists(file_path):
            return ""
        h=hash_method()
        with open(file_path,'rb') as f:
            while b:=f.read(8192):
                h.update(b)
        return h.hexdigest()
    def filesha1(file_path:str) -> str:
        return fileHash(file_path,sha1)
    if DEBUG:
        try: Tools=CDLL("./NTDTools.dll",winmode=0)
        except: 
            try:
                if filesha1(os.getenv("temp")+"\\NTDTools.dll")!=sha1_dll:
                    try:
                        with open(os.getenv("temp")+"\\NTDTools.dll","wb") as f:
                            f.write(b64decode(tools))
                    except: pass
                Tools=CDLL(os.getenv("temp")+"\\NTDTools.dll",winmode=0)
            except: ff=1
    else:
        try:
            if filesha1(os.getenv("temp")+"\\NTDTools.dll")!=sha1_dll:
                try:
                    with open(os.getenv("temp")+"\\NTDTools.dll","wb") as f:
                        f.write(b64decode(tools))
                except: pass
            Tools=CDLL(os.getenv("temp")+"\\NTDTools.dll",winmode=0)
        except: ff=1
def tryLoadUIA():
    global ff,DEBUG
    if DEBUG:
        return
    if not (Process(os.getpid()).cmdline()[-1]=="--uac" or Process(os.getpid()).cmdline()[-1]=="--nouac") or Process(os.getpid()).cmdline()[-1]=="--forceuac":
        if Process(os.getpid()).cmdline()[-1]!="--forceuac":
            try:
                reg=RegOpenKeyEx(HKEY_LOCAL_MACHINE,'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System',0,KEY_ALL_ACCESS)
                if RegQueryValueEx(reg,"EnableLUA")[0]:
                    ff=2
                    return 
            except:
                ff=2
                return
        try:
            with open(os.getenv("systemroot")+"\\Temp\\NTDUIATemp.tmp","w+") as f:
                p=Process(os.getpid()).cmdline()
                if "python" in p[0]:
                    if not os.getcwd().lower() in p[-1].lower():
                        p[-1]=os.getcwd()+"\\"+p[-1]
                p=p[0]+" \""+os.path.abspath(__file__)+"\""
                f.write("".join(p))
            if not os.path.exists(os.getenv("temp")+"\\NTDUIALoader.exe"):
                with open(os.getenv("temp")+"\\NTDUIALoader.exe","wb") as f:
                    f.write(base64.b64decode(uia))
        except:
            return
        Popen(os.getenv("temp")+"\\NTDUIALoader.exe",shell=True)
        os._exit(0)
def rightMenu(x,y,button,pressed):
    global flag5,tdgbhwnd,menu
    if not pressed and button==mouse.Button.right and flag5:
        if GetForegroundWindow()==tdgbhwnd:
            window.sm.emit(x,y)
    if button==mouse.Button.left:
        window.cm.emit(x,y)
def menuListener():
    with mouse.Listener(on_click=rightMenu) as listener:
        listener.join()
def exceptHook(type,value,traceback):
    f=0
    if not "app" in dir():
        f=1
        app=QApplication(sys.argv)
    w=None
    if "window" in dir():
        w=window
    if QMessageBox.critical(w,"NoTopDomain "+VERSION+" Error","NoTopDomain遇到了致命的错误，导致程序崩溃：\n"+    "Traceback (most recent call last):\n"+format_tb(traceback)[0]+type.__name__+": "+str(value)+"\n是否进入反馈？",QMessageBox.Yes|QMessageBox.No)==16384:
        win=Feedbacker(w)
        win.lineEdit.setText("NoTopDomain问题反馈")
        win.textEdit.setPlainText("我在使用NoTopDomain遇到了致命的错误，导致程序崩溃：\n"+    "Traceback (most recent call last):\n"+format_tb(traceback)[0]+type.__name__+": "+str(value))
        def ce(event):
            event.accept()
            os._exit(0)
        win.closeEvent=ce
        win.show()
        if f:
            sys.exit(app.exec())
    os._exit(0)
def loadHiderDLL():
    if not os.path.exists(os.getenv("temp")+"\\NTDHider.dll"):
        with open(os.getenv("temp")+"\\NTDHider.dll","wb+") as f:
            f.write(b64decode(hider))
        with open(os.getenv("temp")+"\\NTDShower.dll","wb+") as f:
            f.write(b64decode(shower))
    if not os.path.exists(os.getenv("temp")+"\\NTDHider32.dll"):
        with open(os.getenv("temp")+"\\NTDHider32.dll","wb+") as f:
            f.write(b64decode(hider32))
        with open(os.getenv("temp")+"\\NTDShower32.dll","wb+") as f:
            f.write(b64decode(shower32))
    if not os.path.exists(os.getenv("temp")+"\\NTDHide32Runner.exe"):
        with open(os.getenv("temp")+"\\NTDHide32Runner.exe","wb+") as f:
            f.write(b64decode(hide32runner))
def loadHookLibs():
    if not os.path.exists(os.getenv("temp")+"\\NTDHookRunner.exe"):
        with open(os.getenv("temp")+"\\NTDHookRunner.exe","wb+") as f:
            f.write(b64decode(hookrunner))
    if DEBUG:
        try:
            with open(os.getenv("temp")+"\\NTDHooks.dll","wb") as f:
                f.write(open("./libs/NTDHooks.dll","rb").read())
            return
        except: pass
    try:
        with open(os.getenv("temp")+"\\NTDHooks.dll","wb") as f:
            f.write(b64decode(hookdll))
    except PermissionError: pass
if __name__=="__main__":
    if not DEBUG: sys.excepthook=exceptHook
    ff=0
    tryLoadUIA()
    loadToolDLL()
    loadHookLibs()
    loadHiderDLL()
    bl=os.getcwd()
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app=QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    os.chdir(os.getenv("SystemDrive"))
    flag,flag2,flag3,flag4,flag5,flag6,tdgbhwnd=1,1,0,0,0,1,0
    window=NoTopDomain()
    thread1=SetWindowPref(int(window.winId()))
    thread1.start()
    thread2=UnlockKeyboard()
    thread2.start()
    thread3=UnlockMouse()
    thread3.start()
    thread4=setState()
    thread4.start()
    thread5=NoBlackScreen()
    thread5.start()
    thread6=Thread(target=menuListener)
    thread6.start()
    sys.exit(app.exec())