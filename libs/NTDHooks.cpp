#include "MinHook.h"
#include <windows.h>
#include <psapi.h>
#include <stdio.h>
typedef BOOL (WINAPI *rCreateProcessA)(LPCSTR lpApplicationName, LPSTR lpCommandLine, LPSECURITY_ATTRIBUTES lpProcessAttributes, LPSECURITY_ATTRIBUTES lpThreadAttributes, BOOL bInheritHandles, DWORD dwCreationFlags, LPVOID lpEnvironment, LPCSTR lpCurrentDirectory, LPSTARTUPINFOA lpStartupInfo, LPPROCESS_INFORMATION lpProcessInformation);
typedef BOOL (WINAPI *rCreateProcessW)(LPCWSTR lpApplicationName, LPWSTR lpCommandLine, LPSECURITY_ATTRIBUTES lpProcessAttributes, LPSECURITY_ATTRIBUTES lpThreadAttributes, WINBOOL bInheritHandles, DWORD dwCreationFlags, LPVOID lpEnvironment, LPCWSTR lpCurrentDirectory, LPSTARTUPINFOW lpStartupInfo, LPPROCESS_INFORMATION lpProcessInformation);
typedef UINT (WINAPI *rWinExec)(LPCSTR lpCmdLine, UINT uCmdShow);
typedef BOOL (WINAPI *rTerminateProcess)(HANDLE hProcess, UINT uExitCode);
typedef LRESULT (WINAPI *rSendMessageA)(HWND hWnd,UINT Msg,WPARAM wParam,LPARAM lParam);
typedef LRESULT (WINAPI *rSendMessageW)(HWND hWnd,UINT Msg,WPARAM wParam,LPARAM lParam);
typedef LRESULT (WINAPI *rPostMessageA)(HWND hWnd,UINT Msg,WPARAM wParam,LPARAM lParam);
typedef LRESULT (WINAPI *rPostMessageW)(HWND hWnd,UINT Msg,WPARAM wParam,LPARAM lParam);
typedef BOOL (WINAPI *rSetWindowPos)(HWND hWnd,HWND hWndInsertAfter,int X,int Y,int cx,int cy,UINT uFlags);
rCreateProcessA realCreateProcessA=(rCreateProcessA)&CreateProcessA;
rCreateProcessW realCreateProcessW=(rCreateProcessW)&CreateProcessW;
rWinExec realWinExec=(rWinExec)&WinExec;
rTerminateProcess realTerminateProcess=(rTerminateProcess)&TerminateProcess;
rSendMessageA realSendMessageA=(rSendMessageA)&SendMessageA;
rSendMessageW realSendMessageW=(rSendMessageW)&SendMessageW;
rPostMessageA realPostMessageA=(rPostMessageA)&PostMessageA;
rPostMessageW realPostMessageW=(rPostMessageW)&PostMessageW;
rSetWindowPos realSetWindowPos=(rSetWindowPos)&SetWindowPos;
BOOL WINAPI fakeCreateProcessA(LPCSTR lpApplicationName, LPSTR lpCommandLine, LPSECURITY_ATTRIBUTES lpProcessAttributes, LPSECURITY_ATTRIBUTES lpThreadAttributes, BOOL bInheritHandles, DWORD dwCreationFlags, LPVOID lpEnvironment, LPCSTR lpCurrentDirectory, LPSTARTUPINFOA lpStartupInfo, LPPROCESS_INFORMATION lpProcessInformation){
    if(strstr(lpCommandLine,"explorer")||strstr(lpCommandLine,"TDChalk"))
        return realCreateProcessA(lpApplicationName,
        lpCommandLine,lpProcessAttributes,lpThreadAttributes,bInheritHandles
        ,dwCreationFlags,lpEnvironment,lpCurrentDirectory,lpStartupInfo,
        lpProcessInformation);
    int can;
    char r[1005];
    char* rr=getenv("temp");
    strcpy(r,rr);
    strcat(r,"\\NTDHooksConfig");
    FILE* fi=fopen(r,"r");
    fscanf(fi,"%d",&can);
    fclose(fi);
    if(can) return 1;
    char res[10005];
    strcpy(res,"极域正尝试执行以下命令，是否继续？\n");
    strcat(res,lpCommandLine);
    int result=MessageBoxA(0,res,"NoTopDomain 警告",MB_ICONWARNING|MB_YESNO);
    if(result==IDYES)
        return realCreateProcessA(lpApplicationName,
        lpCommandLine,lpProcessAttributes,lpThreadAttributes,bInheritHandles
        ,dwCreationFlags,lpEnvironment,lpCurrentDirectory,lpStartupInfo,
        lpProcessInformation);
    else return 1;
}
BOOL WINAPI fakeCreateProcessW(LPCWSTR lpApplicationName, LPWSTR lpCommandLine, LPSECURITY_ATTRIBUTES lpProcessAttributes, LPSECURITY_ATTRIBUTES lpThreadAttributes, WINBOOL bInheritHandles, DWORD dwCreationFlags, LPVOID lpEnvironment, LPCWSTR lpCurrentDirectory, LPSTARTUPINFOW lpStartupInfo, LPPROCESS_INFORMATION lpProcessInformation){
    if(wcsstr(lpCommandLine,L"explorer")||wcsstr(lpCommandLine,L"TDChalk"))
        return realCreateProcessW(lpApplicationName,
        lpCommandLine,lpProcessAttributes,lpThreadAttributes,bInheritHandles
        ,dwCreationFlags,lpEnvironment,lpCurrentDirectory,lpStartupInfo,
        lpProcessInformation);
    int can;
    char r[1005];
    char* rr=getenv("temp");
    strcpy(r,rr);
    strcat(r,"\\NTDHooksConfig");
    FILE* fi=fopen(r,"r");
    fscanf(fi,"%d",&can);
    fclose(fi);
    if(can) return 1;
    wchar_t res[10005];
    wcscpy(res,L"极域正尝试执行以下命令，是否继续？\n");
    wcscat(res,lpCommandLine);
    int result=MessageBoxW(0,res,L"NoTopDomain 警告",MB_ICONWARNING|MB_YESNO);
    if(result==IDYES)
        return realCreateProcessW(lpApplicationName,
        lpCommandLine,lpProcessAttributes,lpThreadAttributes,bInheritHandles
        ,dwCreationFlags,lpEnvironment,lpCurrentDirectory,lpStartupInfo,
        lpProcessInformation);
    else return 1;
}
UINT WINAPI fakeWinExec(LPCSTR lpCmdLine, UINT uCmdShow){
    if(strstr(lpCmdLine,"explorer")||strstr(lpCmdLine,"TDChalk")) return realWinExec(lpCmdLine,uCmdShow);
    int can;
    char r[1005];
    char* rr=getenv("temp");
    strcpy(r,rr);
    strcat(r,"\\NTDHooksConfig");
    FILE* fi=fopen(r,"r");
    fscanf(fi,"%d",&can);
    fclose(fi);
    if(can) return 32;
    char res[10005];
    strcpy(res,"极域正尝试执行以下命令，是否继续？\n");
    strcat(res,lpCmdLine);
    int result=MessageBoxA(0,res,"NoTopDomain 警告",MB_ICONWARNING|MB_YESNO);
    if(result==IDYES) return realWinExec(lpCmdLine,uCmdShow);
    else return 32;
}
BOOL WINAPI fakeTerminateProcess(HANDLE hProcess, UINT uExitCode){
    int can;
    char r[1005];
    char* rr=getenv("temp");
    strcpy(r,rr);
    strcat(r,"\\NTDHooksConfig");
    FILE* fi=fopen(r,"r");
    fscanf(fi,"%d",&can);
    fclose(fi);
    if(can) return 1;
    char res1[10],rres[10005],res3[1005],res4[1005];
    char* res2;
    strcpy(rres,"检测到极域正尝试杀掉该进程：\n");
    itoa(GetProcessId(hProcess),res1,10);
    GetProcessImageFileNameA(hProcess,res4,1005);
    strrev(res4);res2=strtok(res4,"\\");
    strrev(res2);
    if(strstr(res2,"explorer")) return TerminateProcess(hProcess,uExitCode);
    strcat(rres,res2);
    strcat(rres,"\nPID：");
    strcat(rres,res1);
    strcat(rres,"\n要继续吗？");
	if(MessageBoxA(0,rres,"NoTopDomain 警告",MB_ICONWARNING|MB_YESNO)==IDNO){
        SetLastError(ERROR_ACCESS_DENIED);
		return FALSE;
    }
    else return realTerminateProcess(hProcess, uExitCode);
}
BOOL WINAPI fakeSendMessageA(HWND hWnd,UINT Msg,
    WPARAM wParam,LPARAM lParam){
        int can;
        char r[1005];
        char* rr=getenv("temp");
        strcpy(r,rr);
        strcat(r,"\\NTDHooksConfig");
        FILE* fi=fopen(r,"r");
        fscanf(fi,"%d",&can);
        fclose(fi);
        if(can) return 0;
        if(Msg==WM_CLOSE){
            char res1[10],rres[10005],res3[1005],res4[1005];
            char* res2;
            DWORD pId;
            GetWindowThreadProcessId(hWnd,&pId);
            strcpy(rres,"检测到极域正尝试关闭该进程的窗口：\n");
            itoa(pId,res1,10);
            GetProcessImageFileNameA(OpenProcess(PROCESS_ALL_ACCESS,0,pId),res4,1005);
            strrev(res4);res2=strtok(res4,"\\");strrev(res2);
            if(strstr(res2,"StudentMain")||strstr(res2,"studentmain")) return realSendMessageA(hWnd,Msg,wParam,lParam);
            strcat(rres,res2);
            strcat(rres,"\nPID：");
            strcat(rres,res1);
            strcat(rres,"\n要继续吗？");
            if(MessageBoxA(0,rres,"NoTopDomain 警告",MB_ICONWARNING|MB_YESNO)==IDNO)
                return 0;
        }
        return realSendMessageA(hWnd,Msg,wParam,lParam);
}
BOOL WINAPI fakeSendMessageW(HWND hWnd,UINT Msg,
    WPARAM wParam,LPARAM lParam){
        int can;
        char r[1005];
        char* rr=getenv("temp");
        strcpy(r,rr);
        strcat(r,"\\NTDHooksConfig");
        FILE* fi=fopen(r,"r");
        fscanf(fi,"%d",&can);
        fclose(fi);
        if(can) return 0;
        if(Msg==WM_CLOSE){
            char res1[10],rres[10005],res4[10005],res3[1005];
            char* res2;
            DWORD pId;
            GetWindowThreadProcessId(hWnd,&pId);
            strcpy(rres,"检测到极域正尝试关闭该进程的窗口：\n");
            itoa(pId,res1,10);
            GetProcessImageFileNameA(OpenProcess(PROCESS_ALL_ACCESS,0,pId),res4,1005);
            strrev(res4);res2=strtok(res4,"\\");strrev(res2);
            if(strstr(res2,"StudentMain")||strstr(res2,"studentmain")) return realSendMessageW(hWnd,Msg,wParam,lParam);
            strcat(rres,res2);
            strcat(rres,"\nPID：");
            strcat(rres,res1);
            strcat(rres,"\n要继续吗？");
            if(MessageBoxA(0,rres,"NoTopDomain 警告",MB_ICONWARNING|MB_YESNO)==IDNO){
                return 0;
            }
        }
        return realSendMessageW(hWnd,Msg,wParam,lParam);
}
BOOL WINAPI fakePostMessageA(HWND hWnd,UINT Msg,
    WPARAM wParam,LPARAM lParam){
        int can;
        char r[1005];
        char* rr=getenv("temp");
        strcpy(r,rr);
        strcat(r,"\\NTDHooksConfig");
        FILE* fi=fopen(r,"r");
        fscanf(fi,"%d",&can);
        fclose(fi);
        if(can) return 0;
        if(Msg==WM_CLOSE){
            char res1[10],rres[10005],res4[10005],res3[1005];
            char* res2;
            DWORD pId;
            GetWindowThreadProcessId(hWnd,&pId);
            strcpy(rres,"检测到极域正尝试关闭该进程的窗口：\n");
            itoa(pId,res1,10);
            GetProcessImageFileNameA(OpenProcess(PROCESS_ALL_ACCESS,0,pId),res4,1005);
            strrev(res4);res2=strtok(res4,"\\");strrev(res2);
            if(strstr(res2,"StudentMain")||strstr(res2,"studentmain")) return realPostMessageA(hWnd,Msg,wParam,lParam);
            strcat(rres,res2);
            strcat(rres,"\nPID：");
            strcat(rres,res1);
            strcat(rres,"\n要继续吗？");
            if(MessageBoxA(0,rres,"NoTopDomain 警告",MB_ICONWARNING|MB_YESNO)==IDNO){
                return 0;
            }
        }
        return realPostMessageA(hWnd,Msg,wParam,lParam);
}
BOOL WINAPI fakePostMessageW(HWND hWnd,UINT Msg,
    WPARAM wParam,LPARAM lParam){
        int can;
        char r[1005];
        char* rr=getenv("temp");
        strcpy(r,rr);
        strcat(r,"\\NTDHooksConfig");
        FILE* fi=fopen(r,"r");
        fscanf(fi,"%d",&can);
        fclose(fi);
        if(can) return 0;
        if(Msg==WM_CLOSE){
            char res1[10],rres[10005],res4[10005],res3[1005];
            char* res2;
            DWORD pId;
            GetWindowThreadProcessId(hWnd,&pId);
            strcpy(rres,"检测到极域正尝试关闭该进程的窗口：\n");
            itoa(pId,res1,10);
            GetProcessImageFileNameA(OpenProcess(PROCESS_ALL_ACCESS,0,pId),res4,1005);
            strrev(res4);res2=strtok(res4,"\\");strrev(res2);
            if(strstr(res2,"StudentMain")||strstr(res2,"studentmain")) return realPostMessageW(hWnd,Msg,wParam,lParam);
            strcat(rres,res2);
            strcat(rres,"\nPID：");
            strcat(rres,res1);
            strcat(rres,"\n要继续吗？");
            if(MessageBoxA(0,rres,"NoTopDomain 警告",MB_ICONWARNING|MB_YESNO)==IDNO){
                return 0;
            }
        }
        return realPostMessageW(hWnd,Msg,wParam,lParam);
}
BOOL WINAPI fakeSetWindowPos(HWND hWnd,HWND hWndInsertAfter,int X,int Y,
    int cx,int cy,UINT uFlags){
        int can;
        char r[1005];
        char* rr=getenv("temp");
        strcpy(r,rr);
        strcat(r,"\\NTDHooksConfig");
        FILE* fi=fopen(r,"r");
        fscanf(fi,"%*d %d",&can);
        fclose(fi);
        if(can) return realSetWindowPos(hWnd,HWND_NOTOPMOST,X,Y,cx,cy,~((~uFlags)|SWP_NOZORDER));
        else return realSetWindowPos(hWnd,hWndInsertAfter,X,Y,cx,cy,uFlags);
    }
BOOL APIENTRY DllMain(HMODULE hModule,DWORD dReason,LPVOID lpReserved){
    switch(dReason){
        case DLL_PROCESS_ATTACH:
            wchar_t get_path[MAX_PATH];
            GetCurrentDirectoryW(MAX_PATH, get_path);
            if(MH_Initialize()!=MH_OK) return FALSE;
            if(MH_CreateHook((PVOID*)&CreateProcessA,(PVOID*)&fakeCreateProcessA,
                reinterpret_cast<void**>(&realCreateProcessA))!=MH_OK)
                    return FALSE;
            if(MH_EnableHook((PVOID*)&CreateProcessA)!=MH_OK) return FALSE;
            if(MH_CreateHook((PVOID*)&CreateProcessW,(PVOID*)&fakeCreateProcessW,
                reinterpret_cast<void**>(&realCreateProcessW))!=MH_OK)
                    return FALSE;
            if(MH_EnableHook((PVOID*)&CreateProcessW)!=MH_OK) return FALSE;
            if(MH_CreateHook((PVOID*)&WinExec,(PVOID*)&fakeWinExec,
                reinterpret_cast<void**>(&realWinExec))!=MH_OK)
                    return FALSE;
            if(MH_EnableHook((PVOID*)&WinExec)!=MH_OK) return FALSE;
            if(MH_CreateHook((PVOID*)&TerminateProcess,(PVOID*)&fakeTerminateProcess,
                reinterpret_cast<void**>(&realTerminateProcess))!=MH_OK)
                    return FALSE;
            if(MH_EnableHook((PVOID*)&TerminateProcess)!=MH_OK) return FALSE;
            if(MH_CreateHook((PVOID*)&SendMessageA,(PVOID*)&fakeSendMessageA,
                reinterpret_cast<void**>(&realSendMessageA))!=MH_OK)
                    return FALSE;
            if(MH_EnableHook((PVOID*)&SendMessageA)!=MH_OK) return FALSE;
            if(MH_CreateHook((PVOID*)&SendMessageW,(PVOID*)&fakeSendMessageW,
                reinterpret_cast<void**>(&realSendMessageW))!=MH_OK)
                    return FALSE;
            if(MH_EnableHook((PVOID*)&SendMessageW)!=MH_OK) return FALSE;
            if(MH_CreateHook((PVOID*)&PostMessageA,(PVOID*)&fakePostMessageA,
                reinterpret_cast<void**>(&realPostMessageA))!=MH_OK)
                    return FALSE;
            if(MH_EnableHook((PVOID*)&PostMessageA)!=MH_OK) return FALSE;
            if(MH_CreateHook((PVOID*)&PostMessageW,(PVOID*)&fakePostMessageW,
                reinterpret_cast<void**>(&realPostMessageW))!=MH_OK)
                    return FALSE;
            if(MH_EnableHook((PVOID*)&PostMessageW)!=MH_OK) return FALSE;
            if(MH_CreateHook((PVOID*)&SetWindowPos,(PVOID*)&fakeSetWindowPos,
                reinterpret_cast<void**>(&realSetWindowPos))!=MH_OK)
                    return FALSE;
            if(MH_EnableHook((PVOID*)&SetWindowPos)!=MH_OK) return FALSE;

    }
    return TRUE;
}
int main(){
    DllMain(0,DLL_PROCESS_ATTACH,0);
    return 0;
}