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
	//��Ȩ��Debug�Ի�ȡ���̾��
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
	//�ж��Ƿ��Ѿ�SystemȨ����������
	string s = GetCommandLine(),runs,run=getenv("temp");
	if(s[s.size()-1]=='S'){
		//��Ȩ�Ե�ǰ�û���������
		//ȡexplorer��PID
		HWND hwnd = FindWindow("Shell_TrayWnd", NULL);
		DWORD pid;
		GetWindowThreadProcessId(hwnd, &pid);
		//�򿪾������ȡ����
		HANDLE handle = OpenProcess(PROCESS_QUERY_INFORMATION, FALSE, pid);
		HANDLE token;
		OpenProcessToken(handle, TOKEN_DUPLICATE, &token);//ȡ��token
		DuplicateTokenEx(token, MAXIMUM_ALLOWED, NULL, SecurityIdentification, TokenPrimary, &token);
		CloseHandle(handle);
		//Ϊ��������UIAccess
		BOOL fUIAccess = TRUE;
		SetTokenInformation(token, TokenUIAccess, &fUIAccess, sizeof (fUIAccess));
		//������Ϣ
		STARTUPINFOW si;
		PROCESS_INFORMATION pi;
		ZeroMemory(&si, sizeof(STARTUPINFOW));
		si.cb = sizeof(STARTUPINFOW);
		si.lpDesktop = L"winsta0\\default";//��ʾ����
		//�������̣�������CreateProcessAsUser���򱨴�1314����Ȩ
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
	//ö�ٽ��̻�ȡlsass.exe��ID��winlogon.exe��ID�����������еĿ���ֱ�Ӵ򿪾����ϵͳ����
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
	
	//��ȡ���������lsass����winlogon
	HANDLE hProcess = OpenProcess(PROCESS_QUERY_INFORMATION, FALSE, idL);
	if(!hProcess)hProcess = OpenProcess(PROCESS_QUERY_INFORMATION, FALSE, idW);
	HANDLE hTokenx;
	//��ȡ����
	OpenProcessToken(hProcess, TOKEN_DUPLICATE, &hTokenx);
	//��������
	DuplicateTokenEx(hTokenx, MAXIMUM_ALLOWED, NULL, SecurityIdentification, TokenPrimary, &hToken);
	CloseHandle(hProcess);
	CloseHandle(hTokenx);
	//������Ϣ
	STARTUPINFOW si;
	PROCESS_INFORMATION pi;
	ZeroMemory(&si, sizeof(STARTUPINFOW));
	si.cb = sizeof(STARTUPINFOW);
	si.lpDesktop = L"winsta0\\default";//��ʾ����
	//�������̣�������CreateProcessAsUser���򱨴�1314����Ȩ
	CreateProcessWithTokenW(hToken, LOGON_NETCREDENTIALS_ONLY, NULL, lstrcatW(GetCommandLineW(),L" S"), NORMAL_PRIORITY_CLASS, NULL, NULL, &si, &pi);
	CloseHandle(hToken);
}

