#include <windows.h>
#include <tlhelp32.h>
#include <string>
using namespace std;
HOOKPROC HookProc(int nCode,WPARAM wParam,LPARAM lParam){
    return 0;
}
extern"C" {
    void UnlockKeyboard(void);
    void SetWindowPref(HWND hwnd);
    void SetWindowNoPref(HWND hwnd);
    void UnlockMouse(void);
    void LoadUIAccess(string cmdline);
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
//BOOL GetMythwarePasswordFromRegedit(char *str) {
//	HKEY retKey;
//	BYTE retKeyVal[MAX_PATH * 10] = { 0 };
//	DWORD nSize = MAX_PATH * 10;
//	LONG ret = RegOpenKeyEx(HKEY_LOCAL_MACHINE, L"SOFTWARE\\TopDomain\\e-Learning Class\\Student", 0, KEY_QUERY_VALUE | KEY_WOW64_32KEY, &retKey);
//	if (ret != ERROR_SUCCESS) {
//		return FALSE;
//	}
//	ret = RegQueryValueExA(retKey, "knock1", NULL, NULL, (LPBYTE)retKeyVal, &nSize);
//	RegCloseKey(retKey);
//	if (ret != ERROR_SUCCESS) {
//		return FALSE;
//	}
//	for (int i = 0; i < int(nSize); i += 4) {
//		retKeyVal[i + 0] = (retKeyVal[i + 0] ^ 0x50 ^ 0x45);
//		retKeyVal[i + 1] = (retKeyVal[i + 1] ^ 0x43 ^ 0x4c);
//		retKeyVal[i + 2] = (retKeyVal[i + 2] ^ 0x4c ^ 0x43);
//		retKeyVal[i + 3] = (retKeyVal[i + 3] ^ 0x45 ^ 0x50);
//	}
//	for (int i = 0; i < int(nSize); i += 1) {
//		printf("%x ", retKeyVal[i]);
//		if (i % 8 == 0) puts("");
//	}
//	int sum = 0;
//	for (int i = 0; i < int(nSize); i += 1) {
//		if (retKeyVal[i + 1] == 0) {
//			*(str + sum) = retKeyVal[i];
//			sum++;
//			if (retKeyVal[i] == 0) break;
//		}
//	}
//	return TRUE;
//}
int main(){
	return 0;
}