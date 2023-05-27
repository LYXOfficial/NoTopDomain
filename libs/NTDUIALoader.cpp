#include<windows.h>
#include<tlhelp32.h>
#include<string>
#include<iostream>
#include<cstdlib>
#include<fstream>
using namespace std;
LPWSTR* CharToLPWSTR(const char* pChar)
{
    LPWSTR *pLPWSTR = nullptr;
    int nLen = strlen(pChar) + 1;
    pLPWSTR = new LPWSTR[nLen];
    MultiByteToWideChar(CP_ACP, 0, pChar, nLen, (LPWSTR)pLPWSTR , nLen);
    return pLPWSTR ;
}

int main() {
	//提权到Debug以获取进程句柄
	//https://blog.csdn.net/zuishikonghuan/article/details/47746451
	HANDLE hToken;
	LUID Luid;
	TOKEN_PRIVILEGES tp;
	if (!OpenProcessToken(GetCurrentProcess(), TOKEN_ADJUST_PRIVILEGES | TOKEN_QUERY, &hToken))return FALSE;
	if (!LookupPrivilegeValue(NULL, SE_DEBUG_NAME, &Luid)) {
		CloseHandle(hToken);
		return FALSE;
	}
	tp.PrivilegeCount = 1;
	tp.Privileges[0].Luid = Luid;
	tp.Privileges[0].Attributes = SE_PRIVILEGE_ENABLED;
	AdjustTokenPrivileges(hToken, false, &tp, sizeof(tp), NULL, NULL);
	CloseHandle(hToken);
	//判断是否已经System权限启动自身
	string s = GetCommandLine(),runs,run=getenv("temp");
	if(s[s.size()-1]=='S'){
		//降权以当前用户进行启动
		//取explorer的PID
		HWND hwnd = FindWindow("Shell_TrayWnd", NULL);
		DWORD pid;
		GetWindowThreadProcessId(hwnd, &pid);
		//打开句柄，窃取令牌
		HANDLE handle = OpenProcess(PROCESS_QUERY_INFORMATION, FALSE, pid);
		HANDLE token;
		OpenProcessToken(handle, TOKEN_DUPLICATE, &token);//取得token
		DuplicateTokenEx(token, MAXIMUM_ALLOWED, NULL, SecurityIdentification, TokenPrimary, &token);
		CloseHandle(handle);
		//为令牌启用UIAccess
		BOOL fUIAccess = TRUE;
		SetTokenInformation(token, TokenUIAccess, &fUIAccess, sizeof (fUIAccess));
		//启动信息
		STARTUPINFOW si;
		PROCESS_INFORMATION pi;
		ZeroMemory(&si, sizeof(STARTUPINFOW));
		si.cb = sizeof(STARTUPINFOW);
		si.lpDesktop = L"winsta0\\default";//显示窗口
		//启动进程，不能用CreateProcessAsUser否则报错1314无特权
		ifstream inFile;
		inFile.open((run+"\\NTDUIATemp.tmp").c_str(),ios::in);
		if(inFile){
			getline(inFile,runs);
			CreateProcessWithTokenW(token, LOGON_NETCREDENTIALS_ONLY, NULL, (LPWSTR)CharToLPWSTR((runs+" --uac").c_str()), NORMAL_PRIORITY_CLASS | CREATE_NEW_PROCESS_GROUP, NULL, NULL, &si, &pi);
			inFile.close();
		}
		CloseHandle(token);
		return 0;
	}
	//枚举进程获取lsass.exe的ID和winlogon.exe的ID，它们是少有的可以直接打开句柄的系统进程
	DWORD idL, idW;
	PROCESSENTRY32 pe;
	pe.dwSize = sizeof(PROCESSENTRY32);
	HANDLE hSnapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
	if (Process32First(hSnapshot, &pe)) {
		do {
			if (0 == _stricmp(pe.szExeFile, "lsass.exe")) {
				idL = pe.th32ProcessID;
			}else if (0 == _stricmp(pe.szExeFile, "winlogon.exe")) {
				idW = pe.th32ProcessID;
			}
		} while (Process32Next(hSnapshot, &pe));
	}
	CloseHandle(hSnapshot);
	
	//获取句柄，先试lsass再试winlogon
	HANDLE hProcess = OpenProcess(PROCESS_QUERY_INFORMATION, FALSE, idL);
	if(!hProcess)hProcess = OpenProcess(PROCESS_QUERY_INFORMATION, FALSE, idW);
	HANDLE hTokenx;
	//获取令牌
	OpenProcessToken(hProcess, TOKEN_DUPLICATE, &hTokenx);
	//复制令牌
	DuplicateTokenEx(hTokenx, MAXIMUM_ALLOWED, NULL, SecurityIdentification, TokenPrimary, &hToken);
	CloseHandle(hProcess);
	CloseHandle(hTokenx);
	//启动信息
	STARTUPINFOW si;
	PROCESS_INFORMATION pi;
	ZeroMemory(&si, sizeof(STARTUPINFOW));
	si.cb = sizeof(STARTUPINFOW);
	si.lpDesktop = L"winsta0\\default";//显示窗口
	//启动进程，不能用CreateProcessAsUser否则报错1314无特权
	CreateProcessWithTokenW(hToken, LOGON_NETCREDENTIALS_ONLY, NULL, lstrcatW(GetCommandLineW(),L" S"), NORMAL_PRIORITY_CLASS, NULL, NULL, &si, &pi);
	CloseHandle(hToken);
}

