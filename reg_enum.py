import win32api, win32con
 
reg_root = win32con.HKEY_LOCAL_MACHINE
reg_path = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged"
reg_flags = win32con.WRITE_OWNER|win32con.KEY_WOW64_64KEY|win32con.KEY_ALL_ACCESS
 

key = win32api.RegOpenKeyEx(reg_root, reg_path, 0, reg_flags)
for i in range(100):
    guid = win32api.RegEnumKey(key,i)
    print guid
    netKey = win32api.RegOpenKey(key,str(guid))
    addr=win32api.RegEnumValue(netKey,5)
    (n,name,t)=win32api.RegEnumValue(netKey,4)
    print (addr[1],name)
    

win32api.RegCloseKey(key)
