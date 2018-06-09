import win32api, win32con
 
reg_root = win32con.HKEY_LOCAL_MACHINE
reg_path = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged"
reg_flags = win32con.WRITE_OWNER|win32con.KEY_WOW64_64KEY|win32con.KEY_ALL_ACCESS
 

key = win32api.RegOpenKeyEx(reg_root, reg_path, 0, reg_flags)
for item in win32api.RegEnumKeyEx(key):
    print(item)
    

win32api.RegCloseKey(key)
