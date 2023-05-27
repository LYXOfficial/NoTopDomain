import os,sys
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

VERSION="b1.7"
DEBUG=FALSE

class NoTopDomain(QMainWindow,Ui_NoTopDomain,QObject):
    sw=pyqtSignal()
    st=pyqtSignal()
    top=pyqtSignal()
    kf=pyqtSignal()
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
                self.location="/aa/bb/"
                self.CopyLink.setDisabled(1)
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
        self.Stasis=QLabel()
        self.UnlockTDHook.clicked.connect(self.unHook)
        if not self.config.get("QssDisabled"):
            self.setStyleSheet(base64.b64decode(qss).decode())
        self.WebsiteYes.clicked.connect(lambda:Thread(target=self.websiteYes).start())
        self.hk=SystemHotkey()
        try:
            self.hk.register(['control' if i=='ctrl' else i for i in self.config.get("AcWindow").split("+")],callback=lambda _:self.sw.emit())
            self.hk.register(['control' if i=='ctrl' else i for i in self.config.get("KillWindow").split("+")],callback=lambda _:self.kf.emit())
            self.hk.register(['control' if i=='ctrl' else i for i in self.config.get("StartTSK").split("+")],callback=lambda _:self.st.emit())
            self.hk.register(['control' if i=='ctrl' else i for i in self.config.get("TopWindow").split("+")],callback=lambda _:self.top.emit())
        except:
            try:
                self.hk.register(("alt","m"),callback=lambda _:self.sw.emit())
                self.hk.register(("alt","k"),callback=lambda _:self.kf.emit())
                self.hk.register(("alt","t"),callback=lambda _:self.st.emit())
                self.hk.register(("alt","y"),callback=lambda _:self.top.emit())
            except:
                self.Stasis.setText("热键注册失败，请尝试更改配置")
        else:
            global ff
            if ff==1:
                self.Stasis.setText("加载工具DLL失败，部分功能受影响")
            elif ff==2:
                self.Stasis.setText("等待操作...(检测到已开启UAC，建议查看帮助)")
            else:
                self.Stasis.setText("等待操作...(建议查看帮助)")
        self.sw.connect(self.showWindow)
        self.GBWindowed.clicked.connect(self.EnableFullScreen)
        self.action_1=QAction("关于")
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
        self.menubar.addActions([self.action_2,self.feedback,self.action_1,self.action_3])
        self.action_1.triggered.connect(self.showAbout)
        self.action_2.triggered.connect(self.showHelp)
        self.action_3.triggered.connect(self.startTSK)
        self.RestartExplorer.clicked.connect(self.restartExplorer)
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
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
        if not self.checkBox.isChecked():
            self.tray.show()
        self.feedback.triggered.connect(self.Feedback)
        self.KeyboardYes.clicked.connect(self.enableKeyboard)
        self.ToolsYes.clicked.connect(self.enableTools)
        self.KeyboardYes.setCheckState(Qt.Checked)
        self.IamTop.setCheckState(Qt.Checked)
        self.IamTop.clicked.connect(self.toTop)
        self.NoShutdown.clicked.connect(self.noShutDown)
        self.KillSome.setMaximumWidth(100)
        self.KillCurrent.clicked.connect(self.killCurrent)
        self.Stasis.st=self.Stasis.setText
        self.Stasis.setText=self.Stasis.st
        self.Stasis.setMaximumWidth(self.width()-10)
        self.Stasis.setMinimumWidth(self.width()-10)
        self.Stasis.setWordWrap(1)
        self.NoControl.clicked.connect(self.unRemoteControl)
        self.statusbar.addWidget(self.Stasis)
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
                    f.write(b64decode(self.ntsd))
                self.ntsd=os.getenv("temp")+"\\ntsd.exe"
        self.startupinfo = STARTUPINFO()
        self.startupinfo.wShowWindow = SW_HIDE
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
                    Popen(self.ntsd+" -c q -pn gatesrv.exe",shell=True,startupinfo=self.startupinfo)
                    Popen(self.ntsd+" -c q -pn masterhelper.exe",shell=True,startupinfo=self.startupinfo)
                else:
                    pids=process_iter()
                    for p in pids:
                        if p.name().lower()=="gatesrv.exe" or p.name().lower()=="masterhelper.exe":
                            handle=OpenProcess(PROCESS_TERMINATE,0,p.pid)
                            TerminateProcess(handle,0)
                self.Stasis.setText("拦截成功")
            except:
                self.Stasis.setText("拦截失败")
                self.NoControl.setCheckState(Qt.CheckState.Unchecked)
        else:
            try:
                os.startfile(self.location+"gatesrv.exe")
                os.startfile(self.location+"masterhelper.exe")
                self.Stasis.setText("恢复成功")
            except:
                self.Stasis.setText("恢复失败")
                self.NoControl.setCheckState(Qt.CheckState.Checked)
    def unHook(self):
        if self.UnlockTDHook.isChecked():
            if QMessageBox.question(self,"警告","可能导致程序闪退，是否继续？")==16384:
                try:
                    if self.config.get("UseNTSD"):
                        Popen(self.ntsd+" -c q -pn prochelper64.exe",shell=True,startupinfo=self.startupinfo)
                        Popen(self.ntsd+" -c q -pn prochelper32.exe",shell=True,startupinfo=self.startupinfo)
                        self.Stasis.setText("解Hook成功")
                        return
                    else:
                        pids=process_iter()
                        for p in pids:
                            if p.name().lower()=="prochelper64.exe" or p.name().lower()=="prochelper32.exe":
                                handle=OpenProcess(PROCESS_TERMINATE,0,p.pid)
                                TerminateProcess(handle,0)
                                self.Stasis.setText("解Hook成功")
                                return
                    try:
                        hook=GetModuleHandle("LibTDProcHook64.dll")
                        FreeLibrary(hook)
                        self.Stasis.setText("解Hook成功")
                    except:
                        hook=GetModuleHandle("LibTDProcHook32.dll")
                        FreeLibrary(hook)
                        self.Stasis.setText("解Hook成功")
                except:
                    self.Stasis.setText("并未开启防杀")
                    self.UnlockTDHook.setCheckState(Qt.CheckState.Unchecked)
            else:
                self.UnlockTDHook.setCheckState(Qt.CheckState.Unchecked)
                self.Stasis.setText("放弃解防杀")
        else:
            try:
                os.startfile(self.location+"prochelper64.exe")
                self.Stasis.setText("恢复成功")
            except:
                try:
                    os.startfile(self.location+"prochelper32.exe")
                    self.Stasis.setText("恢复成功")
                except:
                    self.Stasis.setText("恢复失败")
    def reTrayState(self):
        if self.checkBox.isChecked():
            self.tray.hide()
        else:
            self.tray.show()
    def restart(self):
        os.chdir(bl)
        Popen(" ".join(Process(os.getpid()).cmdline()),shell=True)
        self.close()
    def enableBar(self):
        try:
            hwnd=FindWindow("Afx:00400000:b","")
            if hwnd:
                EnumChildWindows(hwnd,self.EnumChildWindowsProc3,LPARAM)
                self.Stasis.setText("解禁工具栏成功 咕咕咕")
            else:
                self.Stasis.setText("获取极域工具栏失败 咕咕咕")
        except:
            self.Stasis.setText("解禁工具栏失败 咕咕咕")
    def EnumChildWindowsProc3(self,hwndChild,lParam):
        EnableWindow(hwndChild)
    def EnumChildWindowsProc2(self,hwndChild,lParam):
        hmenu=GetMenu(hwndChild)
        if LOWORD(hmenu)==1004:
            if IsWindowEnabled(hwndChild):
                self.GBWindowed.setText("禁用全屏")
            else:
                self.GBWindowed.setText("解冻全屏")
    def startTSK(self):
        os.startfile("taskmgr")
        QApplication.processEvents()
        self.cnt=0
        self.ttimer.setInterval(50)
        self.ttimer.timeout.connect(self.TSK)
        self.ttimer.start()
    def TSK(self):
        if(self.cnt>20):
            self.Stasis.setText("置顶尝试超时")
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
            self.Stasis.setText("启动并勾选置顶任务管理器，完毕")
        except:
            try:
                SetWindowPos(hwnd,HWND_TOPMOST,0,0,0,0,SWP_NOSIZE|SWP_NOMOVE)
                self.Stasis.setText("启动并外挂置顶任务管理器，完毕（优先级较低）")
            except:
                self.Stasis.setText("似乎任务管理器不可以置顶（Win1122H2?")
    def EnableFullScreen(self):
        try:
            hwnd=FindWindow(0,"屏幕广播")
            self.h=hwnd
            if hwnd:
                EnumChildWindows(hwnd,self.EnumChildWindowsProc,LPARAM)
                self.Stasis.setText("解禁按钮成功")
                return
            else:
                EnumWindows(self.cb2,0)
        except:
            self.Stasis.setText("解禁失败")
    def copyLink(self):
        run("echo "+self.location+" | clip",shell=True)
        self.Stasis.setText("复制链接成功")
    def cb2(self,hwnd,lParam):
        if "正在共享屏幕" in GetWindowText(hwnd):
            self.h=hwnd
            EnumChildWindows(hwnd,self.EnumChildWindowsProc,LPARAM)
            self.Stasis.setText("解禁按钮成功")
        return 1
    def EnumChildWindowsProc(self,hwndChild,lParam):
        hmenu=GetMenu(hwndChild)
        if LOWORD(hmenu)==1004:
            if not IsWindowEnabled(hwndChild):
                EnableWindow(hwndChild,TRUE)
                if self.config.get("AutoCommand"):
                    if GetWindowRect(self.h)==GetWindowRect(GetDesktopWindow()):
                        # PostMessage(hwndChild,WM_COMMAND,WPARAM((BM_CLICK<<16)|1004),NULL)
                        x,y=GetCursorPos()
                        g=GetWindowRect(hwndChild)
                        SetCursorPos((g[0]+10,g[1]+10))
                        Sleep(250)
                        g=GetWindowRect(hwndChild)
                        SetCursorPos((g[0]+10,g[1]+10))
                        mouse_event(MOUSEEVENTF_LEFTDOWN|MOUSEEVENTF_ABSOLUTE,0,0)
                        Sleep(50)
                        mouse_event(MOUSEEVENTF_LEFTUP|MOUSEEVENTF_ABSOLUTE,0,0)
                        SetCursorPos((x,y))
                self.GBWindowed.setText("禁用全屏")
                self.Stasis.setText("解禁按钮成功")
                return 0
            else:
                if self.config.get("AutoCommand"):
                    if GetWindowRect(self.h)!=GetWindowRect(GetDesktopWindow()):
                        # PostMessage(hwndChild,WM_COMMAND,WPARAM((BM_CLICK<<16)|1004),NULL)
                        x,y=GetCursorPos()
                        g=GetWindowRect(hwndChild)
                        SetCursorPos((g[0]+10,g[1]+10))
                        g=GetWindowRect(hwndChild)
                        SetCursorPos((g[0]+10,g[1]+10))
                        Sleep(50)
                        mouse_event(MOUSEEVENTF_LEFTDOWN|MOUSEEVENTF_ABSOLUTE,0,0)
                        Sleep(300)
                        mouse_event(MOUSEEVENTF_LEFTUP|MOUSEEVENTF_ABSOLUTE,0,0)
                        SetCursorPos((x,y))
                EnableWindow(hwndChild,FALSE)
                self.GBWindowed.setText("解冻全屏")
                self.Stasis.setText("禁用按钮成功")
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
                         "TopWindow":"alt+y","KillWindow":"alt+k"}
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
        except:
            self.config={"HideTrayIcon":False,"AutoCommand":False,
                         "QssDisabled":False,"UseNTSD":False,
                         "AcWindow":"alt+m","StartTSK":"alt+t",
                         "TopWindow":"alt+y","KillWindow":"alt+k"}
    def saveConfig(self):
        keys=("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w",
              "x","y","z","0","1","2","3","4","5","6","7","8","9","ctrl","alt","control","shift","esc",
              "f1","f2","f3","f4","f5","f6","f7","f8","f9","f10","f11","f12")
        for k in self.showWindowHotKey.text().lower().split("+"):
            if not (k in keys):
                self.Stasis.setText("唤起窗口快捷键设置不合法")
                return
        for k in self.TSKHotKey.text().lower().split("+"):
            if not (k in keys):
                self.Stasis.setText("任务管理器快捷键设置不合法")
                return
        for k in self.topFocusHotKey.text().lower().split("+"):
            if not (k in keys):
                self.Stasis.setText("置顶窗口快捷键设置不合法")
                return
        for k in self.killFocusHotKey.text().lower().split("+"):
            if not (k in keys):
                self.Stasis.setText("杀掉焦点快捷键设置不合法")
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
            with open(os.getenv("temp")+"\\NTDConfig.json","w+") as f:
                dump(self.config,f)
            self.Stasis.setText("保存成功（重启生效）")
        except:
            self.Stasis.setText("保存失败")
    def closeEvent(self,event):
        event.accept()
        try:
            self.tray.hide()
        except:
            pass
        os._exit(0)
    def killFocus(self):
        if not self.isActiveWindow():
            try:
                pid=GetWindowThreadProcessId(GetForegroundWindow())[1]
                if QMessageBox.question(self,"提示","确定要杀掉焦点进程吗？\npid："+str(pid))==16384:
                    if self.config.get("UseNTSD"):
                        Popen(self.ntsd+" -c q -p %d"%pid,shell=True,startupinfo=self.startupinfo)
                    else:
                        handle=OpenProcess(PROCESS_TERMINATE,0,pid)
                        TerminateProcess(handle,0)
                    self.Stasis.setText("已经杀掉焦点窗口，pid："+str(pid))
                if self.isHidden():
                    self.showNormal()
                    self.hide()
            except:
                self.Stasis.setText("未发现杀掉窗口对象")
        else:
            self.Stasis.setText("触发进程保护...")
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
                self.Stasis.setText("部分项目解禁失败："+" ".join(fails))
            else:
                self.Stasis.setText("解禁成功")
        except:
            self.Stasis.setText("解禁失败，请尝试以管理员权限启动")
    def restartExplorer(self):
        pids=process_iter()
        for p in pids:
            if(p.name().lower()=="explorer.exe"):
                handle=OpenProcess(PROCESS_TERMINATE,0,p.pid)
                TerminateProcess(handle,0)
        self.Stasis.setText("重启成功")
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
                self.Stasis.setText("解除成功")
            except:
                self.Stasis.setText("解除失败，尝试以System权限重启？")
        else:
            self.Stasis.setText("放弃解除")
    def ZB(self):
        self.zb.stop()
        # s=[]
        # retKey=RegOpenKeyEx(HKEY_LOCAL_MACHINE,r"SOFTWARE\WOW6432Node\TopDomain\e-Learning Class\Student",0,KEY_ALL_ACCESS)
        # retKeyVal=[(ord(i)-ord("a")+10 if i>="a" else int(i)) for i in hex(int.from_bytes(RegQueryValueEx(retKey,"Knock")[0]))[2:]]
        # RegCloseKey(retKey)
        # nSize=len(retKeyVal)
        # for i in range(0,nSize,4):
        #     retKeyVal[i]=(retKeyVal[i]^0x50^0x45)
        #     retKeyVal[i+1]=(retKeyVal[i+1]^0x43^0x4c)
        #     retKeyVal[i+2]=(retKeyVal[i+2]^0x4c^0x43)
        #     retKeyVal[i+3]=(retKeyVal[i+3]^0x45^0x50)
        # for i in range(nSize-1):
        #     if retKeyVal[i+1]==0:
        #         s.append(retKeyVal[i])
        #         if retKeyVal[i]==0:
        #             break
        # print("".join([chr(i+ord("0")) for i in s]))
        # # 完全不行）））
        # self.TDPwd.setText("mythware_super_password")
        # 装X？不过原本的密码区改成启动任务栏了
        pass
    def showHelp(self):
        try:
            QMessageBox.information(self,'帮助',"""1.%s唤起软件，%s杀死焦点进程（有保护），%s启动任务管理器，%s切换窗口置顶状态

2.如果开启UAC，软件会自动放弃获取UIAccess，这会降低窗口的置顶层级，所以在广播窗口化时会闪烁。

3.若部分功能失败，不妨解除其它限制再试试？

4.解冻全屏后，窗口不会自动缩小，请手动点击悬浮栏右上角的按钮，或者是把设置里面第二项打开。

5.可以通过挂起极域来在教师端伪装连接。（亲测可行）

6.使用 --forceuac 命令行来强制程序获取UIAccess（可能失败，无提示），使用 --nouac命令行来强制程序不获取UIAccess

7.设置一定要保存！除了快捷键以外保存设置都不需要重启。

8.遇到怪异且难以下手的极域？输入超级密码mythware_super_password往往能解决问题"""%(self.config.get("AcWindow").upper(),self.config.get("KillWindow").upper(),self.config.get("StartTSK").upper(),self.config.get("TopWindow").upper()))
        except:
            QMessageBox.information(self,'帮助',"""1.ALT+M唤起软件，ALT+K杀死焦点进程（有保护），ALT+T启动任务管理器，ALT+Y切换窗口置顶状态

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
                    Popen(self.ntsd+" -c q -p %s"%self.KillSome.text(),shell=True,startupinfo=self.startupinfo)
                    self.Stasis.setText("执行成功")
                    return
                else:
                    handle=OpenProcess(PROCESS_TERMINATE,0,int(self.KillSome.text()))
                    TerminateProcess(handle,0)
                    return
            else:
                if self.config.get("UseNTSD"):
                    Popen(self.ntsd+" -c q -pn %s"%(self.KillSome.text() if ".exe" in self.KillSome.text() else self.KillSome.text()+".exe"),shell=True,startupinfo=self.startupinfo)
                    self.Stasis.setText("执行成功")
                    return
                else:
                    flag=0
                    pids=process_iter()
                    for p in pids:
                        if p.name().lower()==self.KillSome.text() or p.name().lower()==self.KillSome.text()+".exe":
                            handle=OpenProcess(PROCESS_TERMINATE,0,p.pid)
                            TerminateProcess(handle,0)
                            self.Stasis.setText("执行成功")
                            flag=1
                    if flag:
                        return
        except:
            self.Stasis.setText("杀进程失败，检查进程名？")
        else:
            self.Stasis.setText("杀进程失败，检查进程名？")
    def noShutDown(self):
        if self.NoShutdown.isChecked():
            try:
                with open(self.location+"shutdown.exe","rb+") as f:
                    with open(self.location+"Shutdown_back.exe","wb+") as f2:
                        f2.write(f.read())
                    f.seek(0)
                    f.write(b64decode(emptyexe))
                self.Stasis.setText("关机程序补丁注入成功")
            except:
                self.Stasis.setText("注入失败，未找到极域")
        else:
            try:
                with open(self.location+"Shutdown_back.exe","rb+") as f:
                    with open(self.location+"Shutdown.exe","wb+") as f2:
                        f2.write(f.read())
                os.remove(self.location+"shutdown_back.exe")
                self.Stasis.setText("关机程序恢复成功")
            except:
                self.Stasis.setText("恢复失败，未找到极域")
    def websiteYes(self):
        if self.WebsiteYes.isChecked():
            try:
                if self.config.get("UseNTSD"):
                    Popen(self.ntsd+" -c q -pn gatesrv.exe",shell=True,startupinfo=self.startupinfo)
                    Popen(self.ntsd+" -c q -pn masterhelper.exe",shell=True,startupinfo=self.startupinfo)
                    run("sc stop TDNetFilter",shell=True,stdout=PIPE)
                    self.Stasis.setText("解禁网站成功")
                else:
                    pids=process_iter()
                    for p in pids:
                        if p.name().lower()=="gatesrv.exe" or p.name().lower()=="masterhelper.exe":
                            handle=OpenProcess(PROCESS_TERMINATE,0,p.pid)
                            TerminateProcess(handle,0)
                    run("sc stop TDNetFilter",shell=True,stdout=PIPE)
                    self.Stasis.setText("解禁网站成功")
            except:
                self.Stasis.setText("解禁网站失败")
        else:
            try:
                os.startfile(self.location+"gatesrv.exe")
                os.startfile(self.location+"masterhelper.exe")
                run("sc start TDNetFilter",shell=True,stdout=PIPE)
                self.Stasis.setText("恢复禁网成功")
            except:
                self.Stasis.setText("恢复禁网失败")
    def Feedback(self):
        self.fb.show()
    def setTop(self):
        if self.isActiveWindow() or self.topLabel.isActiveWindow():     
            self.Stasis.setText("触发进程保护...")
            return
        hwnd=GetForegroundWindow()
        if not GetWindowLong(hwnd,GWL_EXSTYLE) & WS_EX_TOPMOST:
            self.topLabel.setText("置顶窗口")
            self.topLabel.show()
            SetWindowPos(hwnd,HWND_TOPMOST,0,0,0,0,SWP_NOMOVE|SWP_NOSIZE)
            x,y,_,__=GetWindowRect(hwnd)
            SetWindowPos(self.topLabel.winId(),HWND_TOPMOST,x+10,y+10,0,0,SWP_NOSIZE)
            self.tltimer.start()
            self.Stasis.setText("置顶选中窗口成功，hwnd:%d"%hwnd)
        else:
            self.topLabel.setText("取消置顶")
            self.topLabel.show()
            SetWindowPos(hwnd,HWND_NOTOPMOST,0,0,0,0,SWP_NOMOVE|SWP_NOSIZE)
            x,y,_,__=GetWindowRect(hwnd)
            SetWindowPos(self.topLabel.winId(),HWND_TOPMOST,x+10,y+10,0,0,SWP_NOSIZE)
            self.tltimer.start()
            self.Stasis.setText("取消置顶选中窗口，hwnd:%d"%hwnd)
    def nbs(self):
        global flag3
        if flag3:
            self.Stasis.setText("恢复黑屏成功")
        else:
            self.Stasis.setText("屏蔽黑屏成功")
        flag3=not flag3
    def usbYes(self):
        if self.USBYes.isChecked():
            run("sc stop TDFileFilter",shell=True,stdout=PIPE)
            self.Stasis.setText("解禁USB成功")
        else:
            run("sc start TDFileFilter",shell=True,stdout=PIPE)
            self.Stasis.setText("恢复USB成功") 
    def toTop(self):
        global flag
        if not self.IamTop.isChecked():
            flag=0
            self.Stasis.setText("取消置顶")
        else:
            flag=1
            self.Stasis.setText("置顶完毕") 
    def activate(self,reason):
        if reason == QSystemTrayIcon.DoubleClick:
            self.showWindow()
    def enableKeyboard(self):
        global flag2
        if self.KeyboardYes.isChecked():
            flag2=0
            self.Stasis.setText("解键盘锁成功")
        else:
            flag2=1
            self.Stasis.setText("恢复键盘锁成功")
    def hangTD(self):
        if self.HangState:
            pids=process_iter()
            for p in pids:
                if(p.name().lower()=="studentmain.exe"):
                    pid=Process(p.pid)
                    break
            try:
                pid.suspend()
                self.Stasis.setText("挂起成功")
                self.HangState=0
                self.HangUpTD.setText("启动极域")
                self.KillTD.setEnabled(False)
            except:
                self.Stasis.setText("挂起失败")
        else:
            pids=process_iter()
            for p in pids:
                if(p.name().lower()=="studentmain.exe"):
                    pid=Process(p.pid)
                    break
            try:
                pid.resume()
                self.Stasis.setText("恢复成功")
                self.HangState=1
                self.HangUpTD.setText("挂起极域")
                self.KillTD.setEnabled(True)
            except:
                self.Stasis.setText("恢复失败")
    def killTopDomain(self):
        if self.TDState:
            try:
                if self.config.get("UseNTSD"):
                    Popen(self.ntsd+" -c q -pn studentmain.exe",shell=True,startupinfo=self.startupinfo)
                else:
                    pids=process_iter()
                    for p in pids:
                        if p.name().lower()=="studentmain.exe":
                            pid=p.pid
                    handle=OpenProcess(PROCESS_TERMINATE,0,pid)
                    TerminateProcess(handle,0)
                self.Stasis.setText("成功杀掉极域")
                self.TDState=0
                self.KillTD.setText("启动极域！！")
            except:
                self.Stasis.setText("杀极域失败，可能开启了防杀")
        else:
            try:
                os.startfile(self.location+"studentmain.exe")
                self.TDState=1
                self.KillTD.setText("杀掉极域！！")
                self.Stasis.setText("成功启动极域")
                self.HangState=1
                self.HangUpTD.setText("挂起极域")
            except:
                self.Stasis.setText("获取地址失败（未安装？）")
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
        elif not self.isActiveWindow():
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
                window.StudentRunning.setText("极域：<span style=\"color:red\">挂起中</span>")
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
                if not window.IamTop.isChecked():
                    window.IamTop.click()
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
            if not window.IamTop.isChecked():
                window.IamTop.click()
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