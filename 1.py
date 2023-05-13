import os
a = input("filename>>:")
# 输入文件名时不要带.py后缀
# shell = f"../python311/scripts/cython {a}.py -3 --embed"
# os.system(shell)
with open(a+'.c', 'r') as f:    	     
    content = f.read()
content = content.replace('wmain', 'main')
with open(a+'.c', 'w') as f:    
    content = f.write(content)
shell = f"""gcc -I"C:\TDM-GCC-64\x86_64-w64-mingw32\include" -I"C:\TDM-GCC-64\lib\gcc\x86_64-w64-mingw32\9.2.0\include" -I"F:\Phigros\Python311\include" -mconsole -DSIZEOF_VOID_P=8 -L"F: \Phigros\Python311\Lib" -L"F: \Phigros\Python311\libs" -DMS_WIN64 {a}.c -I D:/Python/include -L D:/Python/libs  -o {a} && {a} && pause"""
os.system(shell)
