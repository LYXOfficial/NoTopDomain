import os,sys
import subprocess as su
from json import *
from base64 import *
from random import *
from psutil import *
from hashlib import *
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
from libs.system_hotkey import *

VERSION="b1.8"
DEBUG=FALSE

class NoTopDomain(QMainWindow,Ui_NoTopDomain,QObject):
    sw=pyqtSignal()
    st=pyqtSignal()
    top=pyqtSignal()
    kf=pyqtSignal()
    ef=pyqtSignal()
    ff=pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.loadConfig()
        self.setup()
        self.show()
        self.setFixedSize(self.width(),self.height())
        QApplication.processEvents()
    def setup(self):
        self.logger=open(os.getenv("temp")+"\\NoTopDomain.log","ab+",buffering=0)
        self.logger.write(("[%s] %s %s 启动 DEBUG: %d\n"%(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),__file__,VERSION,DEBUG)).encode())
        self.setWindowTitle("NoTopDomain %s By LYX"%VERSION)
        self.st.connect(self.startTSK)
        self.kf.connect(self.killFocus)
        self.top.connect(self.setTop)
        try:
            reg=RegOpenKeyEx(HKEY_LOCAL_MACHINE,'SOFTWARE\\WOW6432Node\\TopDomain\\e-Learning Class Standard\\1.00',0,KEY_ALL_ACCESS)
            self.location=RegQueryValueEx(reg,"TargetDirectory")[0]
        except:
            try:
                reg=RegOpenKeyEx(HKEY_LOCAL_MACHINE,'SOFTWARE\\TopDomain\\e-Learning Class Standard\\1.00',0,KEY_ALL_ACCESS)
                self.location=RegQueryValueEx(reg,"TargetDirectory")[0]
            except:
                self.location=""
                self.CopyLink.setDisabled(1)
                self.UninstallTopDomain.setDisabled(True)
        try:
            if "Shutdown_back.exe" in os.listdir(self.location):
                self.NoShutdown.setCheckState(Qt.Checked)
        except:
            pass
        try:
            hwnd=FindWindow(0,self.windowTitle())
            if hwnd and hwnd!=int(self.winId()):
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
                self.close()
        except:
            pass
        try:
            reg=RegOpenKeyEx(HKEY_CURRENT_USER,r'SOFTWARE\Policies\Microsoft\Windows\System',0,KEY_ALL_ACCESS)
            RegSetValueEx(reg,"DisableCMD",0,REG_DWORD,0)
            reg.Close()
        except:
            pass
        self.pushButton_2.clicked.connect(self.saveConfig)
        self.setGeometry(100,100,self.width(),self.height())
        self.TDState=1
        self.HangState=1
        self.CopyLink.clicked.connect(self.copyLink)
        self.ttimer=QTimer()
        self.icon=QPixmap()
        self.icon.loadFromData(b64decode(icon))
        self.reStart.clicked.connect(self.restart)
        self.setWindowIcon(QIcon(self.icon))
        self.zb=QTimer()
        self.zb.setInterval(randint(200,3000))
        self.zb.timeout.connect(self.ZB)
        self.zb.start()
        self.fb=Feedbacker()
        SetWindowPos(self.fb.winId(),HWND_TOPMOST,0,0,0,0,SWP_NOSIZE|SWP_NOMOVE)
        self.logLabel=QLabel()
        self.UnlockTDHook.clicked.connect(self.unHook)
        if not self.config.get("QssDisabled"):
            if DEBUG:
                self.setStyleSheet(open(bl+"/libs/NTD.qss",encoding="utf-8").read())
            else:
                self.setStyleSheet(base64.b64decode(qss).decode())
        self.WebsiteYes.clicked.connect(lambda:Thread(target=self.websiteYes).start())
        self.hk=SystemHotkey()
        try:
            self.hk.register(['control' if i=='ctrl' else i for i in self.config.get("AcWindow").split("+")],callback=lambda _:self.sw.emit())
            self.hk.register(['control' if i=='ctrl' else i for i in self.config.get("KillWindow").split("+")],callback=lambda _:self.kf.emit())
            self.hk.register(['control' if i=='ctrl' else i for i in self.config.get("StartTSK").split("+")],callback=lambda _:self.st.emit())
            self.hk.register(['control' if i=='ctrl' else i for i in self.config.get("TopWindow").split("+")],callback=lambda _:self.top.emit())
            self.hk.register(['control' if i=='ctrl' else i for i in self.config.get("Switch").split("+")],callback=lambda _:self.ef.emit())
            self.hk.register(['control' if i=='ctrl' else i for i in self.config.get("ForceFull").split("+")],callback=lambda _:self.ff.emit())
        except:
            try:
                self.hk.register(("alt","m"),callback=lambda _:self.sw.emit())
                self.hk.register(("alt","k"),callback=lambda _:self.kf.emit())
                self.hk.register(("alt","t"),callback=lambda _:self.st.emit())
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
        self.GBWindowed.clicked.connect(self.EnableFullScreen)
        self.ef.connect(lambda:self.EnableFullScreen() if self.GBWindowed.isEnabled() else self.log("切换窗口化仅在检查到广播后可用"))
        self.action_1=QAction("关于")
        self.action_4=QAction("日志")
        self.action_2=QAction("帮助")
        self.action_3=QAction("启动TSK")
        self.feedback=QAction("反馈")
        self.topLabel=QLabel("")
        self.topLabel.setWindowFlag(Qt.SplashScreen)
        self.topLabel.setStyleSheet("font-family:\"Microsoft YaHei UI Light\";padding:5px;background:white;border:1px solid;border-radius:3px")
        self.tltimer=QTimer()
        self.tltimer.setInterval(2000)
        self.tltimer.timeout.connect(self.hidelb)
        self.checkBox.clicked.connect(self.reTrayState)
        self.menubar.addActions([self.action_2,self.feedback,self.action_1,self.action_3,self.action_4])
        self.action_1.triggered.connect(self.showAbout)
        self.action_2.triggered.connect(self.showHelp)
        self.action_3.triggered.connect(self.startTSK)
        self.action_4.triggered.connect(lambda:Popen("notepad \""+os.getenv("temp")+"\\NoTopDomain.log"+"\"",shell=True))
        self.RestartExplorer.clicked.connect(self.restartExplorer)
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        self.KillTD.clicked.connect(self.killTopDomain)
        self.HangUpTD.clicked.connect(self.hangTD)
        self.tray=QSystemTrayIcon(self.windowIcon())
        self.tray.setToolTip("NoTopDomain")
        self.trayMenu=QMenu()
        if not self.config.get("QssDisabled"):
            self.trayMenu.setStyleSheet(menuqss)
        self.a0=QAction("NoTopDomain %s"%VERSION)
        self.a0.setEnabled(False)
        self.a1=QAction("显示/隐藏主界面")
        self.a1.triggered.connect(self.showWindow)
        self.a2=QAction("退出")
        self.a2.triggered.connect(self.close)
        self.a3=QAction("配置")
        self.a3.triggered.connect(self.toSetting)
        self.trayMenu.addActions([self.a0,self.a1,self.a3,self.a2])
        self.tray.setContextMenu(self.trayMenu)
        if not self.checkBox.isChecked():
            self.tray.show()
        self.feedback.triggered.connect(self.Feedback)
        self.UninstallTopDomain.clicked.connect(lambda:Thread(target=self.uninstallTopDomain).start())
        self.KeyboardYes.clicked.connect(self.enableKeyboard)
        self.ToolsYes.clicked.connect(self.enableTools)
        self.KeyboardYes.setCheckState(Qt.Checked)
        self.IamTop.setCheckState(Qt.Checked)
        self.IamTop.clicked.connect(self.toTop)
        self.NoShutdown.clicked.connect(self.noShutDown)
        self.KillSome.setMaximumWidth(100)
        self.KillCurrent.clicked.connect(self.killCurrent)
        self.logLabel.setMaximumWidth(self.width()-10)
        self.logLabel.setMinimumWidth(self.width()-10)
        self.logLabel.setWordWrap(1)
        self.NoControl.clicked.connect(self.unRemoteControl)
        self.statusbar.addWidget(self.logLabel)
        self.NoImg.clicked.connect(self.noImg)
        self.NoBlackScreen.clicked.connect(self.nbs)
        self.USBYes.clicked.connect(lambda:Thread(target=self.usbYes).start())
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
                self.HangUpTD.setText("启动极域")
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
            os.putenv("_NT_DEBUG_LOG_FILE_APPEND",os.getenv("temp")+"\\NTDntsd.log")
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
    def forceFull(self):
        if self.GBWindowed.text()=="禁用全屏":
            t=self.config["AutoCommand"]
            self.config["AutoCommand"]=1
            self.EnableFullScreen()
            self.config["AutoCommand"]=t
        else:
            self.log("强制全屏仅在检测到广播窗口后可用")
    def hidelb(self):
        self.topLabel.hide()
        self.tltimer.stop()
    def unRemoteControl(self):
        if self.NoControl.isChecked():
            try:
                try:
                    hook=GetModuleHandle(self.location+"libTDMaster.dll")
                    FreeLibrary(hook)
                    hook=GetModuleHandle(self.location+"libTDDesk2.dll")
                    FreeLibrary(hook)
                    hook=GetModuleHandle(self.location+"LibDeskMonitor.dll")
                    FreeLibrary(hook)
                except:
                    pass
                if self.config.get("UseNTSD"):
                    Popen("runas /trustlevel:0x40000 \""+self.ntsd+" -c q -pn gatesrv.exe\"",shell=True,startupinfo=self.startupinfo,stdout=PIPE,stderr=PIPE)
                    Popen("runas /trustlevel:0x40000 \""+self.ntsd+" -c q -pn masterhelper.exe\"",shell=True,startupinfo=self.startupinfo,stdout=PIPE,stderr=PIPE)
                else:
                    pids=process_iter()
                    for p in pids:
                        if p.name().lower()=="gatesrv.exe" or p.name().lower()=="masterhelper.exe":
                            handle=OpenProcess(PROCESS_TERMINATE,0,p.pid)
                            TerminateProcess(handle,0)
                self.log("拦截成功")
            except:
                self.log("拦截失败")
                self.NoControl.setCheckState(Qt.CheckState.Unchecked)
        else:
            try:
                os.startfile(self.location+"gatesrv.exe")
                os.startfile(self.location+"masterhelper.exe")
                self.log("恢复成功")
            except:
                self.log("恢复失败")
                self.NoControl.setCheckState(Qt.CheckState.Checked)
    def log(self,ls):
        self.logLabel.setText(ls)
        if DEBUG:
            try: print(ls)
            except: pass
        self.logger.write(("[%s] %s\n"%(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),ls)).encode())
    def unHook(self):
        if self.UnlockTDHook.isChecked():
            if QMessageBox.question(self,"警告","可能导致程序闪退，是否继续？")==16384:
                try:
                    if self.config.get("UseNTSD"):
                        Popen("runas /trustlevel:0x40000 \""+self.ntsd+" -c q -pn prochelper64.exe \" ",shell=True,startupinfo=self.startupinfo,stdout=PIPE,stderr=PIPE)
                        Popen("runas /trustlevel:0x40000 \""+self.ntsd+" -c q -pn prochelper32.exe \" ",shell=True,startupinfo=self.startupinfo,stdout=PIPE,stderr=PIPE)
                        self.log("解Hook成功")
                        return
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
                    self.log("并未开启防杀")
                    self.UnlockTDHook.setCheckState(Qt.CheckState.Unchecked)
            else:
                self.UnlockTDHook.setCheckState(Qt.CheckState.Unchecked)
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
            Sleep(500)
            keybd_event(0xff0d,0,0,0)
            Sleep(100)
            keybd_event(0xff0d,0,KEYEVENTF_KEYUP,0)
            hwnd=FindWindow(0,"输入卸载密码")
            EnumChildWindows(hwnd,self.cb3,LPARAM)
            # EnumChildWindows(hwnd,self.cb4,LPARAM)
            self.log("请在窗口中确认卸载")
        except:
            self.log("调用卸载程序失败")
    def cb3(self,hwnd,lp):
        if GetClassName(hwnd)=="Edit":
            SendMessage(hwnd,WM_SETTEXT,0,self.TDPasswd.text()[:-1])
    def cb4(self,hwnd,lp):
        if GetWindowText(hwnd)=="确定":
            SendMessage(hwnd,WM_LBUTTONDOWN,MK_LBUTTON,0)
            SendMessage(hwnd,WM_LBUTTONUP,MK_LBUTTON,0)
    def reTrayState(self):
        if self.checkBox.isChecked():
            self.tray.hide()
        else:
            self.tray.show()
    def toSetting(self):
        self.showNormal()
        self.setFocus()
        self.PigeonGames.setCurrentIndex(1)
    def restart(self):
        os.chdir(bl)
        Popen(" ".join(Process(os.getpid()).cmdline()).replace(" --uac"," --nouac"),shell=True,startupinfo=self.startupinfo,stdout=PIPE,stderr=PIPE)
        self.close()
    def EnumChildWindowsProc3(self,hwndChild,lParam):
        EnableWindow(hwndChild)
    def EnumChildWindowsProc2(self,hwndChild,lParam):
        hmenu=GetMenu(hwndChild)
        if LOWORD(hmenu)==1004:
            if IsWindowEnabled(hwndChild):
                self.GBWindowed.setText("禁用全屏")
            else:
                self.GBWindowed.setText("解冻全屏")
                if not window.IamTop.isChecked():
                    window.IamTop.click()
    def startTSK(self):
        os.startfile("taskmgr")
        QApplication.processEvents()
        self.cnt=0
        self.ttimer.setInterval(50)
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
            if(not (UnpackMENUITEMINFO(mii)[1] & MFS_CHECKED)):
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
            if hwnd:
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
        if "正在共享屏幕" in GetWindowText(hwnd):
            self.h=hwnd
            EnumChildWindows(hwnd,self.EnumChildWindowsProc,LPARAM)
            self.log("解禁按钮成功")
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
                        SendMessage(hwndChild,WM_LBUTTONDOWN,MK_LBUTTON,0)
                        SendMessage(hwndChild,WM_LBUTTONUP,MK_LBUTTON,0)
                self.GBWindowed.setText("禁用全屏")
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
                        SendMessage(hwndChild,WM_LBUTTONDOWN,MK_LBUTTON,0)
                        SendMessage(hwndChild,WM_LBUTTONUP,MK_LBUTTON,0)
                EnableWindow(hwndChild,FALSE)
                self.GBWindowed.setText("解冻全屏")
                self.log("禁用按钮成功")
                return 0
        return 1
    def loadConfig(self):
        try:
            try:
                with open(os.getenv("temp")+"\\NTDConfig.json","r+") as f:
                    f.seek(0)
                    self.config=load(f)
            except:
                with open(os.getenv("temp")+"\\NTDConfig.json","w+") as f:
                    self.config={"HideTrayIcon":False,"AutoCommand":False,
                         "QssDisabled":False,"UseNTSD":False,
                         "AcWindow":"alt+m","StartTSK":"alt+t",
                         "TopWindow":"alt+y","KillWindow":"alt+k",
                         "Switch":"alt+q","ForceFull":"alt+f"}
                    f.seek(0)
                    dump(self.config,f)
            if self.config.get("HideTrayIcon"):
                self.checkBox.click()
            if self.config.get("AutoCommand"):
                self.checkBox_2.click()
            if self.config.get("QssDisabled"):
                self.checkBox_3.click()
            if self.config.get("UseNTSD"):
                self.checkBox_4.click()
            self.showWindowHotKey.setText(self.config.get("AcWindow").upper())
            self.TSKHotKey.setText(self.config.get("StartTSK").upper())
            self.topFocusHotKey.setText(self.config.get("TopWindow").upper())
            self.killFocusHotKey.setText(self.config.get("KillWindow").upper())
            self.GBWindowSwitchHotKey.setText(self.config.get("Switch").upper())
            self.ForceFullHotKey.setText(self.config.get("ForceFull").upper())
        except:
            self.config={"HideTrayIcon":False,"AutoCommand":False,
                         "QssDisabled":False,"UseNTSD":False,
                         "AcWindow":"alt+m","StartTSK":"alt+t",
                         "TopWindow":"alt+y","KillWindow":"alt+k",
                         "Switch":"alt+q","ForceFull":"alt+f"}
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
            self.config["QssDisabled"]=self.checkBox_3.isChecked()
            self.config["UseNTSD"]=self.checkBox_4.isChecked()
            self.config["AcWindow"]=self.showWindowHotKey.text().lower()
            self.config["StartTSK"]=self.TSKHotKey.text().lower()
            self.config["TopWindow"]=self.topFocusHotKey.text().lower()
            self.config["KillWindow"]=self.killFocusHotKey.text().lower()
            self.config["Switch"]=self.GBWindowSwitchHotKey.text().lower()
            self.config["ForceFull"]=self.ForceFullHotKey.text().lower()
            with open(os.getenv("temp")+"\\NTDConfig.json","w+") as f:
                dump(self.config,f)
            self.log("保存成功（重启生效）")
        except:
            self.log("保存失败")
    def closeEvent(self,event):
        event.accept()
        try:
            self.tray.hide()
            self.logger.close()
        except:
            pass
        os._exit(0)
    def killFocus(self):
        if not self.isActiveWindow():
            try:
                pid=GetWindowThreadProcessId(GetForegroundWindow())[1]
                if QMessageBox.question(self,"提示","确定要杀掉焦点进程吗？\npid："+str(pid))==16384:
                    if self.config.get("UseNTSD"):
                        Popen("runas /trustlevel:0x40000 \""+self.ntsd+" -c q -p %d\" "%pid,shell=True,startupinfo=self.startupinfo,stdout=PIPE,stderr=PIPE)
                    else:
                        handle=OpenProcess(PROCESS_TERMINATE,0,pid)
                        TerminateProcess(handle,0)
                    self.log("已经杀掉焦点窗口，pid："+str(pid))
                if self.isHidden():
                    self.showNormal()
                    self.hide()
            except:
                self.log("未发现杀掉窗口对象")
        else:
            self.log("触发进程保护...")
    def enableTools(self):
        QMessageBox.information(self,"提示","以下工具/功能将被解禁：\n1.修改密码\n2.注册表编辑器\n3.切换用户\n4.任务管理器\n5.Autorun\n6.注销/开始菜单选项\n7.运行")
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
        s=QMessageBox.question(self,"警告","重置映像劫持不可逆，是否继续？")
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
                    return
            except:
                reg=RegOpenKeyEx(HKEY_LOCAL_MACHINE,r'SOFTWARE\TopDomain\e-Learning Class Standard\1.00')
                r=RegQueryValueEx(reg,"UninstallPasswd")
                if r[1] and r[0]!='Passwd[123456]':
                    self.TDPasswd.setText(r[0][7:-1])
                    return
            Tools.GetMythwarePasswordFromRegedit()
            with open(os.getenv("temp")+"\\NTDPwd.txt",encoding="utf-8") as f:
                self.TDPasswd.setText(f.read())
        except:
            if self.location:
                self.TDPasswd.setText("mythware_super_password")
            else:
                self.TDPasswd.setText("未找到极域")
    def showHelp(self):
        try:
            QMessageBox.information(self,'帮助',"""1.%s唤起软件，%s杀死焦点进程（有保护），%s启动任务管理器，%s切换窗口置顶状态，%s快速强制广播全屏，%s切换窗口化按键状态
2.如果开启UAC，软件会自动放弃获取UIAccess，这会降低窗口的置顶层级，所以在广播窗口化时会闪烁。
3.若部分功能失败，不妨解除其它限制再试试？
4.解冻全屏后，窗口不会自动缩小，请手动点击悬浮栏右上角的按钮，或者是把设置里面第二项打开。
5.可以通过挂起极域来在教师端伪装连接。（亲测可行）
6.使用 --forceuac 命令行来强制程序获取UIAccess（可能失败，无提示），使用 --nouac命令行来强制程序不获取UIAccess
7.设置一定要保存！除了快捷键以外保存设置都不需要重启。
8.遇到怪异且难以下手的极域？输入超级密码mythware_super_password往往能解决问题"""%(self.config.get("AcWindow").upper(),self.config.get("KillWindow").upper(),self.config.get("StartTSK").upper(),self.config.get("TopWindow").upper(),self.config.get("ForceFull").upper(),self.config.get("Switch").upper()))
        except:
            QMessageBox.information(self,'帮助',"""1.ALT+M唤起软件，ALT+K杀死焦点进程（有保护），ALT+T启动任务管理器，ALT+Y切换窗口置顶状态，ALT+F快速强制广播全屏，ALT+Q切换窗口化按键状态
2.如果开启UAC，软件会自动放弃获取UIAccess，这会降低窗口的置顶层级，所以在广播窗口化时会闪烁。
3.若部分功能失败，不妨解除其它限制再试试？
4.解冻全屏后，窗口不会自动缩小，请手动点击悬浮栏右上角的按钮，或者是把设置里面第二项打开。
5.可以通过挂起极域来在教师端伪装连接。（亲测可行）
6.使用 --forceuac 命令行来强制程序获取UIAccess（可能失败，无提示），使用 --nouac命令行来强制程序不获取UIAccess
7.设置一定要保存！除了快捷键以外保存设置都不需要重启。
8.遇到怪异且难以下手的极域？输入超级密码mythware_super_password往往能解决问题""")
    def killCurrent(self):
        try:
            if self.KillSome.text().isdigit():
                if self.config.get("UseNTSD"):
                    Popen("runas /trustlevel:0x40000 \""+self.ntsd+" -c q -p %s\" "%self.KillSome.text(),shell=True,startupinfo=self.startupinfo,stdout=PIPE,stderr=PIPE)
                    self.log("执行成功")
                    return
                else:
                    handle=OpenProcess(PROCESS_TERMINATE,0,int(self.KillSome.text()))
                    TerminateProcess(handle,0)
                    return
            else:
                if self.config.get("UseNTSD"):
                    Popen("runas /trustlevel:0x40000 \""+self.ntsd+" -c q -pn %s\" "%(self.KillSome.text() if ".exe" in self.KillSome.text() else self.KillSome.text()+".exe"),shell=True,startupinfo=self.startupinfo,stdout=PIPE,stderr=PIPE)
                    self.log("执行成功")
                    return
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
        else:
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
                    Popen("runas /trustlevel:0x40000 \""+self.ntsd+" -c q -pn gatesrv.exe\" ",shell=True,startupinfo=self.startupinfo,stdout=PIPE,stderr=PIPE)
                    Popen("runas /trustlevel:0x40000 \""+self.ntsd+" -c q -pn masterhelper.exe\" ",shell=True,startupinfo=self.startupinfo,stdout=PIPE,stderr=PIPE)
                    run("sc stop TDNetFilter",shell=True,stdout=PIPE)
                    self.log("解禁网站成功")
                else:
                    pids=process_iter()
                    for p in pids:
                        if p.name().lower()=="gatesrv.exe" or p.name().lower()=="masterhelper.exe":
                            handle=OpenProcess(PROCESS_TERMINATE,0,p.pid)
                            TerminateProcess(handle,0)
                    run("sc stop TDNetFilter",shell=True,stdout=PIPE)
                    self.log("解禁网站成功")
            except:
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
    def setTop(self):
        if self.isActiveWindow() or self.topLabel.isActiveWindow():     
            self.log("触发进程保护...")
            return
        hwnd=GetForegroundWindow()
        if not GetWindowLong(hwnd,GWL_EXSTYLE) & WS_EX_TOPMOST:
            self.topLabel.setText("置顶窗口")
            self.topLabel.show()
            SetWindowPos(hwnd,HWND_TOPMOST,0,0,0,0,SWP_NOMOVE|SWP_NOSIZE)
            x,y,_,__=GetWindowRect(hwnd)
            SetWindowPos(self.topLabel.winId(),HWND_TOPMOST,x+10,y+10,0,0,SWP_NOSIZE)
            self.tltimer.start()
            self.log("置顶选中窗口成功，hwnd:%d"%hwnd)
        else:
            self.topLabel.setText("取消置顶")
            self.topLabel.show()
            SetWindowPos(hwnd,HWND_NOTOPMOST,0,0,0,0,SWP_NOMOVE|SWP_NOSIZE)
            x,y,_,__=GetWindowRect(hwnd)
            SetWindowPos(self.topLabel.winId(),HWND_TOPMOST,x+10,y+10,0,0,SWP_NOSIZE)
            self.tltimer.start()
            self.log("取消置顶选中窗口，hwnd:%d"%hwnd)
    def nbs(self):
        global flag3
        if flag3:
            self.log("恢复黑屏成功")
        else:
            self.log("启动黑屏屏蔽")
        flag3=not flag3
    def usbYes(self):
        if self.USBYes.isChecked():
            run("sc stop TDFileFilter",shell=True,stdout=PIPE)
            self.log("解禁USB成功")
        else:
            run("sc start TDFileFilter",shell=True,stdout=PIPE)
            self.log("恢复USB成功") 
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
                self.HangUpTD.setText("启动极域")
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
                self.HangUpTD.setText("挂起极域")
                self.KillTD.setEnabled(True)
            except:
                self.log("恢复失败")
    def killTopDomain(self):
        if self.TDState:
            try:
                if self.config.get("UseNTSD"):
                    Popen("runas /trustlevel:0x40000 \""+self.ntsd+" -c q -pn studentmain.exe\" ",shell=True,startupinfo=self.startupinfo,stdout=PIPE,stderr=PIPE)
                else:
                    pids=process_iter()
                    for p in pids:
                        if p.name().lower()=="studentmain.exe":
                            pid=p.pid
                    handle=OpenProcess(PROCESS_TERMINATE,0,pid)
                    TerminateProcess(handle,0)
                self.log("成功杀掉极域")
                self.TDState=0
                self.KillTD.setText("启动极域！！")
            except:
                self.log("杀极域失败，可能开启了防杀")
        else:
            if ff==2:
                try:
                    if self.location:
                        Popen(f"""runas /trustlevel:0x20000 "{self.location}studentmain.exe" """,stdout=PIPE,shell=True)
                        self.TDState=1
                        self.KillTD.setText("杀掉极域！！")
                        self.log("成功启动极域")
                        self.HangState=1
                        self.HangUpTD.setText("挂起极域")
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
                        self.KillTD.setText("杀掉极域！！")
                        self.log("成功启动极域")
                        self.HangState=1
                        self.HangUpTD.setText("挂起极域")
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
        QMessageBox.about(self,'关于',"""NoTopDomain By LYX<br>%s<br>Powered By <a href="https://blog.csdn.net/weixin_42112038/article/details/127480471">极域机房工具箱1.1</a><br><a href="https://yisous.xyz">博客</a> <a href="https://luogu.com.cn/user/761305">Luogu</a> <a href="https://github.com/lyxofficial">Github</a>"""%VERSION)
    def showWindow(self):
        if self.isHidden():
            self.showNormal()
        elif not (self.isActiveWindow()) and not self.IamTop.isChecked():
            self.activateWindow()
        else:
            self.hide()
class UnlockKeyboard(Thread):
    def __init__(self):
        super().__init__()
    def run(self):
        while(1):
            if(flag2):
                Tools.UnlockKeyboard()
                Tools.UnlockMouse()
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
        global flag3
        pids=process_iter()
        for p in pids:
            if(p.name().lower()=="studentmain.exe"):
                window.TDState=0
                window.KillTD.setText("启动极域！！")
        while(1):
            if not window.HangState:
                pid,s=0,1
                pids=process_iter()
                for p in pids:
                    if(p.name().lower()=="studentmain.exe"):
                        s,pid=0,p.pid
                        break
                if not s:
                    window.StudentRunning.setText("极域：<span style=\"color:red\">挂起中</span> <span style=\"color:gray\">PID:%s</span>"%pid)
            else:
                pid,s=0,1
                pids=process_iter()
                for p in pids:
                    if(p.name().lower()=="studentmain.exe"):
                        s,pid=0,p.pid
                        break
                if s:
                    window.StudentRunning.setText("极域：<span style=\"color:green\">未运行</span>")
                    window.HangUpTD.setEnabled(False)
                    # window.EnableTDBar.setEnabled(False)
                    window.TDState=0
                    window.KillTD.setText("启动极域！！")
                else:
                    window.StudentRunning.setText("极域：<span style=\"color:orange\">运行中</span> <span style=\"color:gray\">PID:%s</span>"%pid)
                    window.HangUpTD.setEnabled(True)
                    # window.EnableTDBar.setEnabled(True)
                    window.TDState=1
                    window.KillTD.setText("杀掉极域！！")
                    window.HangState=1
                    window.HangUpTD.setText("挂起极域")
            self.flag=1
            hwnd=0
            hwnd=FindWindow(0,"BlackScreen Window")
            if hwnd:
                self.flag=0
                window.GBWindowed.setText("解冻全屏")
                window.GBWindowed.setEnabled(False)
                if not flag3:
                    window.GBing.setText("<span style=\"color:purple\">黑屏安静中</span>")
                else:
                    window.GBing.setText("<span style=\"color:blue\">黑屏安静已屏蔽</span>")
            hwnd=0
            hwnd=FindWindow(0,"屏幕广播")
            if hwnd:
                window.GBing.setText("广播：<span style=\"color:orange\">进行中</span>")
                window.GBWindowed.setEnabled(True)
                try:
                    EnumChildWindows(hwnd,window.EnumChildWindowsProc2,LPARAM)
                except:
                    pass
                self.flag=0
            else:
                EnumWindows(self.cb1,0)
            if self.flag:
                window.GBing.setText("广播：<span style=\"color:green\">未进行</span>")
                window.GBWindowed.setText("解冻全屏")
                window.GBWindowed.setEnabled(False)
            Sleep(1000)
    def cb1(self,hwnd,lparam):
        if "正在共享屏幕" in GetWindowText(hwnd):
            window.GBing.setText("广播：<span style=\"color:orange\">进行中</span>")
            window.GBWindowed.setEnabled(True)
            try:
                EnumChildWindows(hwnd,window.EnumChildWindowsProc2,LPARAM)
            except:
                pass
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
    if DEBUG:
        try:
            try:
                Tools=CDLL("./NTDTools.dll",winmode=0)
            except:
                Tools=CDLL("./NTDTools32.dll",winmode=0)
            return
        except:
            pass
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
    try:
        if filesha1(os.getenv("temp")+"\\NTDTools.dll")!=sha1_dll:
            try:
                with open(os.getenv("temp")+"\\NTDTools.dll","wb") as f:
                    f.write(b64decode(tools64))
                with open(os.getenv("temp")+"\\NTDTools32.dll","wb") as f:
                    f.write(b64decode(tools32))
            except:
                pass
        try:
            Tools=CDLL(os.getenv("temp")+"\\NTDTools.dll",winmode=0)
        except:
            Tools=CDLL(os.getenv("temp")+"\\NTDTools32.dll",winmode=0)
    except:
        ff=1
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
                    p[1]=os.getcwd()+"\\"+p[1]
                f.write(" ".join(p))
            if not os.path.exists(os.getenv("temp")+"\\NTDUIALoader.exe"):
                with open(os.getenv("temp")+"\\NTDUIALoader.exe","wb") as f:
                    f.write(base64.b64decode(uia))
        except:
            return
        Popen(os.getenv("temp")+"\\NTDUIALoader.exe",shell=True)
        exit(0)
if __name__=="__main__":
    ff=0
    tryLoadUIA()
    loadToolDLL()
    bl=os.getcwd()
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app=QApplication(sys.argv)
    os.chdir(os.getenv("SystemDrive"))
    flag,flag2,flag3=1,1,0
    window=NoTopDomain()
    thread=SetWindowPref(int(window.winId()))
    thread.start()
    thread2=UnlockKeyboard()
    thread2.start()
    stateThread=setState()
    stateThread.start()
    blackScreenThread=NoBlackScreen()
    blackScreenThread.start()
    sys.exit(app.exec())