#include <Windows.h>
extern "C" __declspec(dllexport) int SetWindowDisplayAffinity(HWND a,int b);
DWORD pid;
BOOL CALLBACK EnumWindowCallBack(HWND hWnd, LPARAM lParam){
    HMODULE dll=LoadLibraryA("user32.dll");
    typedef int(*AddFunc)(HWND,int);
    AddFunc SetWindowDisplayAffinity;
    SetWindowDisplayAffinity=(AddFunc)GetProcAddress(dll,"SetWindowDisplayAffinity");
    DWORD dwpid;
    if(GetWindowThreadProcessId(hWnd,&dwpid))
        if(dwpid==pid&&(GetWindowLong(hWnd,GWL_STYLE)&WS_VISIBLE))
            SetWindowDisplayAffinity(hWnd,0);
    return 1;
}
int DllMain(){
    
    pid=GetCurrentProcessId();
    EnumWindows(EnumWindowCallBack,0);
    return 0;
}