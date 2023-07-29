#include <stdio.h>
#include <windows.h>
void InjectDLL(DWORD dwId,LPCSTR path){
    HANDLE mProcess=OpenProcess(PROCESS_ALL_ACCESS, FALSE, dwId);
    LPTHREAD_START_ROUTINE fun =(LPTHREAD_START_ROUTINE)LoadLibraryA;
    SIZE_T pathSize=strlen(path)+1;
    LPVOID mBuffer=VirtualAllocEx(mProcess, NULL, pathSize, MEM_COMMIT, PAGE_READWRITE);
    WriteProcessMemory(mProcess, mBuffer, path, pathSize, NULL);
    CreateRemoteThread(mProcess, NULL, 0, fun, mBuffer, 0, NULL);
    return;
}
int main(){
    char *a=GetCommandLineA(),*src=getenv("temp");
    DWORD pId;
    sscanf(a,"%*s --pid=%d",&pId);
    strcat(src,"\\NTDHooks.dll");
    InjectDLL(pId,src);
    return GetLastError();
}