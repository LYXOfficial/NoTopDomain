//蒟蒻 QwQ
#include <windows.h>
#include <cstdio>
#include <tlhelp32.h>
#include "MinHook.h"
using namespace std;
HOOKPROC HookProc(int nCode,WPARAM wParam,LPARAM lParam){
    return 0;
}
extern"C" {
    void UnlockKeyboard(void);
    void SetWindowPref(HWND hwnd);
    void SetWindowNoPref(HWND hwnd);
    void UnlockMouse(void);
    void GetMythwarePasswordFromRegedit(void);
    int StartMythware(LPWSTR location);
    bool GetWindowRightMenu(HWND hwnd);
    bool KillProcessByThread(int pid);
    void InjectDLL(DWORD pid,LPCSTR path);
}
void UnlockKeyboard(){
    HHOOK kbdHook=SetWindowsHookEx(WH_KEYBOARD_LL,(HOOKPROC)HookProc,GetModuleHandle(NULL),0);
    Sleep(50);
    UnhookWindowsHookEx(kbdHook);
}
void UnlockMouse(){
    HHOOK mseHook = (HHOOK)SetWindowsHookEx(WH_MOUSE_LL, (HOOKPROC)HookProc, GetModuleHandle(NULL), 0);
    ClipCursor(0);
    Sleep(50);
    UnhookWindowsHookEx(mseHook);
}
void SetWindowPref(HWND hwnd){
    SetWindowPos(hwnd,HWND_TOPMOST,0,0,0,0,SWP_NOMOVE|SWP_NOSIZE);
    Sleep(50);
}
void SetWindowNoPref(HWND hwnd){
    SetWindowPos(hwnd,HWND_NOTOPMOST,0,0,0,0,SWP_NOMOVE|SWP_NOSIZE);
    Sleep(50);
}
void GetMythwarePasswordFromRegedit() {
    char str[1145];
    int f=1;
	HKEY retKey;
	BYTE retKeyVal[MAX_PATH * 10] = { 0 };
	DWORD nSize = MAX_PATH * 10;
	LONG ret = RegOpenKeyEx(HKEY_LOCAL_MACHINE, "SOFTWARE\\WOW6432Node\\TopDomain\\e-Learning Class\\Student", 0, KEY_QUERY_VALUE | KEY_WOW64_32KEY, &retKey);
    if (ret != ERROR_SUCCESS) {
        LONG ret = RegOpenKeyEx(HKEY_LOCAL_MACHINE, "SOFTWARE\\TopDomain\\e-Learning Class\\Student", 0, KEY_QUERY_VALUE | KEY_WOW64_32KEY, &retKey);
		if (ret != ERROR_SUCCESS) return;
    }
	ret = RegQueryValueExA(retKey, "Knock", NULL, NULL, (LPBYTE)retKeyVal, &nSize);
	if (ret != ERROR_SUCCESS) {
		ret = RegQueryValueExA(retKey, "knock1", NULL, NULL, (LPBYTE)retKeyVal, &nSize);
        if (ret != ERROR_SUCCESS) return;
        f=0;
        RegCloseKey(retKey);
	}
    else RegCloseKey(retKey);
	for (int i = 0; i < int(nSize); i += 4) {
		retKeyVal[i + 0] = (retKeyVal[i + 0] ^ 0x50 ^ 0x45);
		retKeyVal[i + 1] = (retKeyVal[i + 1] ^ 0x43 ^ 0x4c);
		retKeyVal[i + 2] = (retKeyVal[i + 2] ^ 0x4c ^ 0x43);
		retKeyVal[i + 3] = (retKeyVal[i + 3] ^ 0x45 ^ 0x50);
	}
	int sum = 0;
	for (int i = 1; i <=int(nSize); i += 1) {
		if (retKeyVal[i + 1] == 0) {
			str[sum] = retKeyVal[i];
			sum++;
			if (retKeyVal[i] == 0) break;
		}
	}
    str[sum]='\0';
    char* s=getenv("temp");
    strcat(s,"\\NTDPwd.key");
    freopen(s,"w",stdout);
    puts(str);
    freopen("CON", "w", stdout);
    return;
}
int StartMythware(LPWSTR location){
    HWND hwnd = FindWindow("Shell_TrayWnd", NULL);
    if(!hwnd) return 2;
    DWORD pid;
    GetWindowThreadProcessId(hwnd, &pid);
    HANDLE handle = OpenProcess(PROCESS_QUERY_INFORMATION, FALSE, pid);
    HANDLE token;
    OpenProcessToken(handle, TOKEN_DUPLICATE, &token);
    DuplicateTokenEx(token, MAXIMUM_ALLOWED, NULL, SecurityIdentification, TokenPrimary, &token);
    CloseHandle(handle);
    STARTUPINFOW si;
    PROCESS_INFORMATION pi;
    ZeroMemory(&si, sizeof(STARTUPINFOW));
    si.cb = sizeof(STARTUPINFOW);
    si.lpDesktop = (wchar_t*)L"winsta0\\default";
    auto res=CreateProcessWithTokenW(token, LOGON_NETCREDENTIALS_ONLY, NULL, location, NORMAL_PRIORITY_CLASS | CREATE_NEW_PROCESS_GROUP, NULL, NULL, &si, &pi);
    CloseHandle(token);
    if(!res) return 1;
    else return 0;
}
bool KillProcessByThread(int pid){
    HANDLE hSnapshot = CreateToolhelp32Snapshot(TH32CS_SNAPTHREAD, pid);
    if (hSnapshot != INVALID_HANDLE_VALUE) {
        bool rtn = true;
        THREADENTRY32 te = {sizeof(te)};
        BOOL fOk = Thread32First(hSnapshot, &te);
        for (; fOk; fOk = Thread32Next(hSnapshot, &te)) {
            if (te.th32OwnerProcessID == pid) {
                HANDLE hThread = OpenThread(THREAD_TERMINATE, FALSE, te.th32ThreadID);
                if (!TerminateThread(hThread, 0)) rtn = false;
                CloseHandle(hThread);
            }
        }
        CloseHandle(hSnapshot);
        return rtn;
    }
    return false;
}
void InjectDLL(DWORD dwId,LPCSTR path){
    printf("%s\n",path);
    HANDLE mProcess=OpenProcess(PROCESS_ALL_ACCESS, FALSE, dwId);
    LPTHREAD_START_ROUTINE fun =(LPTHREAD_START_ROUTINE)LoadLibraryA;
    SIZE_T pathSize=strlen(path)+1;
    LPVOID mBuffer=VirtualAllocEx(mProcess, NULL, pathSize, MEM_COMMIT, PAGE_READWRITE);
    WriteProcessMemory(mProcess, mBuffer, path, pathSize, NULL);
    CreateRemoteThread(mProcess, NULL, 0, fun, mBuffer, 0, NULL);
    return;
}
int main(){
    // CallDLLInject(114,2);
    // StartMythware(L"explorer.exe");
    // GetMythwarePasswordFromRegedit();
	return 0;
}