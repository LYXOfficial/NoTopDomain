#include <windows.h>
HOOKPROC HookProc(int nCode,WPARAM wParam,LPARAM lParam){
    return 0;
}
extern"C" {
    void UnlockKeyboard(void);
    void SetWindowPref(HWND hwnd);
    void SetWindowNoPref(HWND hwnd);
    void UnlockMouse(void);
}
void UnlockKeyboard(){
    HHOOK kbdHook=SetWindowsHookEx(WH_KEYBOARD_LL,(HOOKPROC)HookProc,GetModuleHandle(NULL),0);
    Sleep(25);
    UnhookWindowsHookEx(kbdHook);
}
void UnlockMouse(){
    // HHOOK mseHook = (HHOOK)SetWindowsHookEx(WH_MOUSE_LL, (HOOKPROC)HookProc, GetModuleHandle(NULL), 0);
    // ClipCursor(0);
    // UnhookWindowsHookEx(mseHook);
    // Sleep(10);
    // 因为鼠标卡顿用户体验不好暂时不要
}
void SetWindowPref(HWND hwnd){
    SetWindowPos(hwnd,HWND_TOPMOST,0,0,0,0,SWP_NOMOVE|SWP_NOSIZE);
    Sleep(20);
}
void SetWindowNoPref(HWND hwnd){
    SetWindowPos(hwnd,HWND_NOTOPMOST,0,0,0,0,SWP_NOMOVE|SWP_NOSIZE);
    Sleep(20);
}
int main(){
    return 0;
}