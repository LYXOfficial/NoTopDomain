from win32api import *
from win32con import *
from win32gui import *
from win32print import *
from win32process import *
from win32gui_struct import *
from commctrl import *
from ctypes import *


def get_all_tray_icons():
    # 获取系统托盘窗口句柄
    hwnd = FindWindow("Shell_TrayWnd",None)
    hwnd = FindWindowEx(hwnd,0,"TrayNotifyWnd",None)
    hwnd = FindWindowEx(hwnd,0,"SysPager",None)
    hwnd = FindWindowEx(hwnd,0,"ToolbarWindow32",None)
    icons_info = []
    hProcess=OpenProcess(PROCESS_ALL_ACCESS,FALSE,GetWindowThreadProcessId(hwnd))
    lpButton=POINTER(c_void_p)
    lpButton=windll.kernel32.VirtualAllocEx(hProcess,NULL,32,MEM_COMMIT,PAGE_READWRITE)
    for i in range(256):
        SendMessage(hwnd,TB_GETBUTTON,i,lpButton)
        ReadProcessMemory(hProcess,lpButton,)

            

    return icons_info

if __name__ == "__main__":
    icons_info = get_all_tray_icons()
    for info in icons_info:
        print(info)