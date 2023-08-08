#include "MinHook.h"
#include <windows.h>
typedef int (WINAPI *rMessageBoxA)(HWND hWnd,LPCSTR lpText,LPCSTR lpCaption,UINT uType);
rMessageBoxA realMessageBoxA=(rMessageBoxA)&MessageBoxA;
int WINAPI fakeMessageBoxA(HWND hWnd,LPCSTR lpText,LPCSTR lpCaption,UINT uType){
    realMessageBoxA(hWnd,"Hooked!",lpCaption,uType); //改变消息框文本为Hooked!，忽略原本的参数
    return 1;
}
int main(){
    if(MH_Initialize()!=MH_OK) return TRUE;
    if(MH_CreateHook((PVOID*)&MessageBoxA,(PVOID*)&fakeMessageBoxA,reinterpret_cast<void**>(&realMessageBoxA))!=MH_OK)
        return TRUE;
    if(MH_EnableHook((PVOID*)&MessageBoxA)!=MH_OK)
        return TRUE;
    MessageBoxA(0,"unHook","test",0);
    // if(MH_DisableHook((PVOID*)&MessageBoxA)!=MH_OK)
        return TRUE;
    return 0;
}