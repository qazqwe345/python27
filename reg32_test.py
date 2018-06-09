import win32api

import win32con

key = win32api.RegCreateKeyEx(win32con.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows", win32con.WRITE_OWNER |win32con.KEY_WOW64_64KEY|win32con.KEY_ALL_ACCESS)
win32api.RegSetValueEx (key,"MyNewkey", 0, win32con.REG_SZ, keyValue)
