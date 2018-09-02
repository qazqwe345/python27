import win32api
import win32con
REG_RUN = r'Software\Microsoft\Windows\CurrentVersion\Run'

'''
win32api.RegOpenKeyEx()
win32api.RegCloseKey()
win32api.RegCreateKeyEx()
win32api.RegDeleteKey()
win32api.RegQueryValueEx()
win32api.RegSetValueEx()
win32api.RegDeleteValue()
win32api.RegEnumKeyEx()
win32api.RegEnumValue()
'''

def showRunList():
    hKey = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,REG_RUN, 0, win32con.KEY_ALL_ACCESS)
    i = 0
    lRet = 0
    dwType = 0
    szValueName = ''
    while (1):
        try:
            szValueName,lRet,dwType = win32api.RegEnumValue(hKey,i)
            print szValueName,lRet,dwType
            i += 1
        except:
            win32api.RegCloseKey(hKey)
            return
        
def AddRunList():
    name = "crawler1.py"
    value = "crawler.py"
    hKey = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,REG_RUN, 0, win32con.KEY_ALL_ACCESS)
    win32api.RegSetValueEx(hKey, name, 0, win32con.REG_SZ, value)
    win32api.RegCloseKey(hKey)

def DelFromRunList():
    name = "crawler1.py"
    value = "crawler.py"
    hKey = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,REG_RUN, 0, win32con.KEY_ALL_ACCESS)
    win32api.RegDeleteValue(hKey,name)
    win32api.RegCloseKey(hKey)
