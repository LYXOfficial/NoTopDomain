VERSION="b1.1"
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import Qt,QObject,pyqtSignal,QTimer,QThread
from Ui_NTD import *
from win32api import *
from win32con import *
from win32gui import *
from win32process import *
from win32gui_struct import *
from ctypes import *
from ctypes.wintypes import *
from system_hotkey import SystemHotkey
from multiprocessing import Process,Value
import sys,os,psutil,subprocess,b64,base64,random,webbrowser
class NoTopDomain(QMainWindow,Ui_NoTopDomain,QObject):
    sw=pyqtSignal()
    st=pyqtSignal()
    top=pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setup()
        self.show()
    def EnumChildWindowsProc2(self,hwndChild,lParam):
        hmenu=GetMenu(hwndChild)
        if LOWORD(hmenu)==1004:
            if IsWindowEnabled(hwndChild):
                self.GBWindowed.setText("禁用全屏")
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
                PostMessage(hwnd, WM_COMMAND, 0x7704, 0)
            self.Stasis.setText("启动并勾选置顶任务管理器，完毕")
        except:
            try:
                SetWindowPos(hwnd,HWND_TOPMOST,0,0,0,0,SWP_NOSIZE|SWP_NOMOVE)
                self.Stasis.setText("启动并外挂置顶任务管理器，完毕（优先级较低）")
            except:
                self.Stasis.setText("似乎任务管理器不可以置顶（Win1122H2?")
    def EnableFullScreen(self):
        try:
            hWndList = [] 
            EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList) 
            for hwnd in hWndList:
                self.h=hwnd
                title = GetWindowText(hwnd)
                if title=="屏幕广播":
                    EnumChildWindows(hwnd,self.EnumChildWindowsProc,LPARAM)
                    self.Stasis.setText("解禁按钮成功")
                    return
        except:
            self.Stasis.setText("解禁失败")
    def EnumChildWindowsProc(self,hwndChild,lParam):
        hmenu=GetMenu(hwndChild)
        if LOWORD(hmenu)==1004:
            if not IsWindowEnabled(hwndChild):
                EnableWindow(hwndChild, TRUE)
                # if GetWindowRect(self.h)==GetWindowRect(GetDesktopWindow()):
                #     x,y=GetCursorPos()
                #     g=GetWindowRect(hwndChild)
                #     SetCursorPos((g[0]+10,g[1]+10))
                #     Sleep(250)
                #     g=GetWindowRect(hwndChild)
                #     SetCursorPos((g[0]+10,g[1]+10))
                #     mouse_event(MOUSEEVENTF_LEFTDOWN|MOUSEEVENTF_ABSOLUTE,0,0)
                #     Sleep(50)
                #     mouse_event(MOUSEEVENTF_LEFTUP|MOUSEEVENTF_ABSOLUTE,0,0)
                #     SetCursorPos((x,y))
                # 后面设置里面加上，咕咕咕！
                self.GBWindowed.setText("禁用全屏")
                self.Stasis.setText("解禁按钮成功")
                return 0
            else:
                # if GetWindowRect(self.h)!=GetWindowRect(GetDesktopWindow()) and GetWindowPlacement==SW_NORMAL:
                #     x,y=GetCursorPos()
                #     g=GetWindowRect(hwndChild)
                #     SetCursorPos((g[0]+10,g[1]+10))
                #     g=GetWindowRect(hwndChild)
                #     SetCursorPos((g[0]+10,g[1]+10))
                #     mouse_event(MOUSEEVENTF_LEFTDOWN|MOUSEEVENTF_ABSOLUTE,0,0)
                #     Sleep(100)
                #     mouse_event(MOUSEEVENTF_LEFTUP|MOUSEEVENTF_ABSOLUTE,0,0)
                #     SetCursorPos((x,y))
                EnableWindow(hwndChild, FALSE)
                self.GBWindowed.setText("解冻全屏")
                self.Stasis.setText("禁用按钮成功")
                return 0
        return 1
    def closeEvent(self, event):
        event.accept()
        thread.terminate()
        os._exit(0)
    def killFocus(self):
        if not self.isActiveWindow():
            pid=GetWindowThreadProcessId(GetForegroundWindow())[1]
            handle=OpenProcess(PROCESS_TERMINATE,0,pid)
            TerminateProcess(handle,0)
            self.Stasis.setText("已经杀掉焦点窗口，pid："+str(pid))
        else:
            self.Stasis.setText("触发进程保护...")
    def enableTools(self):
        QMessageBox.information(self,"提示","以下工具/功能将被解禁：\n1.修改密码\n2.注册表编辑器\n3.切换用户\n4.任务管理器\n5.Autorun\n6.注销/开始菜单选项\n7.运行")
        try:
            flag=0
            fails=[]
            reg=RegOpenKeyEx(HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System',0,KEY_ALL_ACCESS)
            dises=["DisableChangePassword","DisableRegistryTools","DisableSwitchUserOption","DisableTaskMgr"]
            for i in dises:
                try:
                    RegSetValueEx(reg,i,0,REG_DWORD,0)
                except:
                    flag=1
                    fails.append(i)
            reg.Close()
            reg=RegOpenKeyEx(HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer',0,KEY_ALL_ACCESS)
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
            self.Stasis.setText("解禁失败")
    def restartExplorer(self):
        subprocess.run("tskill explorer",shell=True,stdout=subprocess.PIPE)
        self.Stasis.setText("重启成功")
    def noImg(self):
        s=QMessageBox.question(self,"警告","重置映像劫持不可逆，是否继续？")
        if(s==16384):
            try:
                reg=RegOpenKeyEx(HKEY_LOCAL_MACHINE, r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options',0,KEY_ALL_ACCESS)
                for item in RegEnumKeyEx(reg):
                    try:
                        r=RegOpenKeyEx(HKEY_LOCAL_MACHINE, r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\\'+item[0],0,KEY_ALL_ACCESS)
                        RegQueryValueEx(r,"debugger")
                    except:
                        pass
                    else:
                        RegDeleteKey(RegOpenKeyEx(HKEY_LOCAL_MACHINE, r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options',0,KEY_ALL_ACCESS),item[0])
                        r.Close()
                self.Stasis.setText("解除成功")
            except:
                self.Stasis.setText("解除失败")
        else:
            self.Stasis.setText("放弃解除")
    def ZB(self):
        self.zb.stop()
        # s=[]
        # retKey=RegOpenKeyEx(HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\TopDomain\e-Learning Class\Student", 0, KEY_ALL_ACCESS)
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
        # 完全不行）））
        self.TDPwd.setText("mythware_super_password")
    
    def showHelp(self):
         QMessageBox.information(self,'帮助',"""1.Alt+M唤起软件，Alt+K杀死焦点进程（不会杀掉工具本身，有保护），Alt+T启动任务管理器，Alt+Y切换窗口置顶状态
2.因设计缺陷，在全屏时唤起后窗口会出现闪烁，属于正常现象
3.若部分功能失败，不妨解除其它限制再试试？
4.部分解除限制功能需要在连接前解除，可以拔掉网线重启电脑
5.可以通过挂起极域来在教师端伪装连接
6.还没做完呢！咕咕咕！""")
    def killCurrent(self):
        try:
            if self.KillSome.text().isdigit():
                handle=OpenProcess(PROCESS_TERMINATE,0,int(self.KillSome.text()))
                TerminateProcess(handle,0)
            else:
                pids=psutil.process_iter()
                for p in pids:
                    if p.name().lower()==self.KillSome.text():
                        handle=OpenProcess(PROCESS_TERMINATE,0,p.pid)
                        TerminateProcess(handle,0)
            self.Stasis.setText("执行成功")
        except:
            self.Stasis.setText("杀进程失败，检查进程名？")
    def noShutDown(self):
        if self.NoShutdown.checkState()==Qt.Checked:
            try:
                with open(self.location+"shutdown.exe","rb+") as f:
                    with open(self.location+"Shutdown_back.exe","wb+") as f2:
                        f2.write(f.read())
                    f.seek(0)
                    f.write(base64.b64decode(b64.emptyexe))
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
        if self.WebsiteYes.checkState()==Qt.Checked:
            try:
                pids=psutil.process_iter()
                for p in pids:
                    if p.name().lower()=="gatesrv.exe" or p.name().lower()=="masterhelper.exe":
                        handle=OpenProcess(PROCESS_TERMINATE,0,p.pid)
                        TerminateProcess(handle,0)
                subprocess.run("sc stop TDNetFilter",shell=True,stdout=subprocess.PIPE)
                self.Stasis.setText("解禁网站成功")
            except:
                self.Stasis.setText("解禁网站失败")
        else:
            try:
                os.startfile(self.location+"gatesrv.exe")
                os.startfile(self.location+"masterhelper.exe")
                subprocess.run("sc start TDNetFilter",shell=True,stdout=subprocess.PIPE)
                self.Stasis.setText("恢复禁网成功")
            except:
                self.Stasis.setText("恢复禁网失败")
    def Feedback(self):
        QMessageBox.information(self,"提示","请前往Github提交issue<br><a href=\"https://www.w3.org/International/i18n-activity/guidelines/issues.zh-hans.html\">怎么用Github的issue？</a>")
        webbrowser.open("https://github.com/lyxofficial/notopdomain/issues")
    def setTop(self):
        if self.isActiveWindow():
            self.Stasis.setText("触发进程保护...")
            return
        hwnd=GetForegroundWindow()
        if not GetWindowLong(hwnd, GWL_EXSTYLE) & WS_EX_TOPMOST:
            SetWindowPos(hwnd,HWND_TOPMOST,0,0,0,0,SWP_NOMOVE|SWP_NOSIZE)
            self.Stasis.setText("置顶选中窗口成功，hwnd: %d"%hwnd)
        else:
            SetWindowPos(hwnd,HWND_NOTOPMOST,0,0,0,0,SWP_NOMOVE|SWP_NOSIZE)
            self.Stasis.setText("取消置顶选中窗口，hwnd: %d"%hwnd)
    def setup(self):
        self.setWindowTitle("NoTopDomain %s By LYX"%VERSION)
        self.st.connect(self.startTSK)
        self.top.connect(self.setTop)
        try:
            reg=RegOpenKeyEx(HKEY_LOCAL_MACHINE, 'SOFTWARE\\WOW6432Node\\TopDomain\\e-Learning Class Standard\\1.00',0,KEY_ALL_ACCESS)
            self.location=RegQueryValueEx(reg,"TargetDirectory")[0]
        except:
            self.location="/usr/bin/"
        try:
            if "Shutdown_back.exe" in os.listdir(self.location):
                self.NoShutdown.setCheckState(Qt.Checked)
        except:
            pass
        try:
            hWndList = [] 
            EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList) 
            for hwnd in hWndList:
                title = GetWindowText(hwnd)
                if title==self.windowTitle() and hwnd!=self.winId():
                    SetForegroundWindow(hwnd)
                    if not IsWindowVisible(hwnd):
                        keybd_event(18,0,0,0)
                        keybd_event(77,0,0,0)
                        keybd_event(77,0,KEYEVENTF_KEYUP,0)
                        keybd_event(18,0,KEYEVENTF_KEYUP,0)
                    self.close()
        except:
            pass
        try:
            reg=RegOpenKeyEx(HKEY_CURRENT_USER, r'SOFTWARE\Policies\Microsoft\Windows\System',0,KEY_ALL_ACCESS)
            RegSetValueEx(reg,"DisableCMD",0,REG_DWORD,0)
            reg.Close()
        except:
            pass
        # try:
        #     hook=GetModuleHandle("LibTDProcHook64.dll")
        #     FreeLibrary(hook)
        # except:
        #     pass #打不开？
        self.setFixedSize(360,390)
        self.setGeometry(100,100,self.width(),self.height())
        self.TDState=1
        self.HangState=1
        self.ttimer=QTimer()
        self.icon=QPixmap()
        self.icon.loadFromData(base64.b64decode(b64.icon))
        self.setWindowIcon(QIcon(self.icon))
        self.zb=QTimer()
        self.zb.setInterval(random.randint(200,3000))
        self.zb.timeout.connect(self.ZB)
        self.zb.start()
        self.Stasis=QLabel()
        self.WebsiteYes.clicked.connect(self.websiteYes)
        try:
            self.hk=SystemHotkey()
            self.hk.register(("alt","m"),callback=lambda _:self.sw.emit())
            self.hk.register(("alt","k"),callback=lambda _:self.killFocus())
            self.hk.register(("alt","t"),callback=lambda _:self.st.emit())
            self.hk.register(("alt","y"),callback=lambda _:self.top.emit())
        except:
            self.Stasis.setText("热键注册失败，请尝试更改配置")
        else:
            self.Stasis.setText("等待操作...")
        self.sw.connect(self.showWindow)
        self.GBWindowed.clicked.connect(self.EnableFullScreen)
        self.action_1=QAction("关于")
        self.action_2=QAction("帮助")
        self.action_3=QAction("启动TSK")
        self.menubar.addActions([self.action_1,self.action_2,self.action_3])
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
        self.tray.show()
        self.feedback.clicked.connect(self.Feedback)
        self.KeyboardYes.clicked.connect(self.enableKeyboard)
        self.ToolsYes.clicked.connect(self.enableTools)
        self.KeyboardYes.setCheckState(Qt.Checked)
        self.IamTop.setCheckState(Qt.Checked)
        self.IamTop.clicked.connect(self.toTop)
        self.NoShutdown.clicked.connect(self.noShutDown)
        self.KillSome.setMaximumWidth(100)
        self.KillSome.textChanged.connect(lambda:self.KillCurrent.setEnabled(1) if "exe" in self.KillSome.text() or self.KillSome.text().isdigit() else self.KillCurrent.setEnabled(0))
        self.KillCurrent.clicked.connect(self.killCurrent)
        self.Stasis.st=self.Stasis.setText
        self.Stasis.setText=self.Stasis.st
        self.Stasis.setMaximumWidth(self.width()-10)
        self.Stasis.setMinimumWidth(self.width()-10)
        self.Stasis.setWordWrap(1)
        self.statusbar.addWidget(self.Stasis)
        self.NoImg.clicked.connect(self.noImg)
        self.USBYes.clicked.connect(lambda:Thread(target=self.usbYes).start())
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
    def usbYes(self):
        if self.USBYes.checkState()==Qt.Checked:
            subprocess.run("sc stop TDFileFilter",shell=True,stdout=subprocess.PIPE)
            self.Stasis.setText("解禁USB成功")
        else:
            subprocess.run("sc start TDFileFilter",shell=True,stdout=subprocess.PIPE)
            self.Stasis.setText("恢复USB成功") 
    def toTop(self):
        global flag
        if self.IamTop.checkState()==Qt.Unchecked:
            flag.value=0
            self.Stasis.setText("取消置顶")
        else:
            flag.value=1
            self.Stasis.setText("置顶完毕") 
    def activate(self,reason):
        if reason == QSystemTrayIcon.DoubleClick:
            self.showWindow()
    def enableKeyboard(self):
        global flag2
        if self.KeyboardYes.checkState()==Qt.Checked:
            flag2.value=0
            self.Stasis.setText("解键盘锁成功")
        else:
            flag2.value=1
            self.Stasis.setText("恢复键盘锁成功")
    def hangTD(self):
        if self.HangState:
            pids=psutil.process_iter()
            for p in pids:
                if(p.name().lower()=="studentmain.exe"):
                    pid=psutil.Process(p.pid)
                    break
            try:
                pid.suspend()
                self.Stasis.setText("挂起成功")
                self.HangState=0
                self.HangUpTD.setText("恢复极域")
                self.KillTD.setEnabled(False)
            except:
                self.Stasis.setText("挂起失败")
        else:
            pids=psutil.process_iter()
            for p in pids:
                if(p.name().lower()=="studentmain.exe"):
                    pid=psutil.Process(p.pid)
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
                pids=psutil.process_iter()
                for p in pids:
                    if p.name().lower()=="studentmain.exe":
                        pid=p.pid
                handle=OpenProcess(PROCESS_TERMINATE,0,pid)
                TerminateProcess(handle,0)
                self.Stasis.setText("成功杀掉极域")
                self.TDState=0
                self.KillTD.setText("老师来了！！！")
            except:
                self.Stasis.setText("杀极域失败")
        else:
            try:
                os.startfile(self.location+"studentmain.exe")
                self.TDState=1
                self.KillTD.setText("杀掉极域！！！")
                self.Stasis.setText("成功启动极域")
                self.HangState=1
                self.HangUpTD.setText("挂起极域")
            except:
                self.Stasis.setText("获取地址失败（未安装？）")
    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.WindowStateChange:
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
class UnlockKeyboard(Process):
    def __init__(self,flag2):
        super().__init__()
        self.flag2=flag2
    def run(self):
        while(1):
            if(self.flag2.value):
                kbdHook=windll.user32.SetWindowsHookExA(WH_KEYBOARD_LL,0,0,0)
                Sleep(15)
                windll.user32.UnhookWindowsHookEx(kbdHook)
class SetWindowPref(Process):
    def __init__(self,flag,hwnd):
        super().__init__()
        self.flag=flag
        self.hwnd=hwnd
    def run(self):
        while(1):
            if(self.flag.value):
                SetWindowPos(self.hwnd,HWND_TOPMOST,0,0,0,0,SWP_NOMOVE|SWP_NOSIZE)
                Sleep(10)
            else:
                SetWindowPos(self.hwnd,HWND_NOTOPMOST,0,0,0,0,SWP_NOMOVE|SWP_NOSIZE)
                Sleep(10)
class setState(QThread):
    def __init__(self):
        super().__init__()
    def run(self):
        s=subprocess.run("tasklist|find /i \"studentmain.exe\"",shell=True,stdout=subprocess.PIPE).returncode
        if s:
            window.TDState=0
            window.KillTD.setText("启动极域！！！")
        while(1):
            if not window.HangState:
                window.StudentRunning.setText("极域：<span style=\"color:red\">挂起中</span>")
            else:
                s=subprocess.run("tasklist|find /i \"studentmain.exe\"",shell=True,stdout=subprocess.PIPE).returncode
                if s:
                    window.StudentRunning.setText("极域：<span style=\"color:green\">未运行</span>")
                    window.HangUpTD.setEnabled(False)
                    window.TDState=0
                    window.KillTD.setText("老师来了！！！")
                else:
                    window.StudentRunning.setText("极域：<span style=\"color:orange\">运行中</span>")
                    window.HangUpTD.setEnabled(True)
                    window.TDState=1
                    window.KillTD.setText("杀掉极域！！！")
                    window.HangState=1
                    window.HangUpTD.setText("挂起极域")
            hWndList = [] 
            EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList) 
            for hwnd in hWndList:
                title = GetWindowText(hwnd)
                if title=="屏幕广播":
                    window.GBing.setText("广播：<span style=\"color:orange\">进行中</span>")
                    window.GBWindowed.setEnabled(True)
                    if window.IamTop.checkState()==Qt.Unchecked:
                        window.IamTop.click()
                    try:
                        EnumChildWindows(hwnd,window.EnumChildWindowsProc2,LPARAM)
                    except:
                        pass
                    return
            window.GBing.setText("广播：<span style=\"color:green\">未进行</span>")
            window.GBWindowed.setText("解冻全屏")
            window.GBWindowed.setEnabled(False)
            Sleep(1000)
if __name__=="__main__":
    app=QApplication(sys.argv)
    os.chdir(os.getenv("SystemDrive"))
    flag,flag2=Value("d",1),Value("d",1)
    window=NoTopDomain()
    thread=SetWindowPref(flag,int(window.winId()))
    thread.start()
    thread2=UnlockKeyboard(flag2)
    thread2.start()
    stateThread=setState()
    stateThread.start()
    sys.exit(app.exec_())