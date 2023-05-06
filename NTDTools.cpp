#include <windows.h>
HOOKPROC KeyProc(int nCode,WPARAM wParam,LPARAM lParam){
    return 0;
}
extern"C" {
    void UnlockKeyboard(void);
    void SetWindowPref(HWND hwnd);
    void SetWindowNoPref(HWND hwnd);
}
void UnlockKeyboard(){
    HHOOK kbdHook=SetWindowsHookEx(WH_KEYBOARD_LL,(HOOKPROC)KeyProc,GetModuleHandle(NULL),0);
    Sleep(25);
    UnhookWindowsHookEx(kbdHook);
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