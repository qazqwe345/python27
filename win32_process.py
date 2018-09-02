'''
win32con.SW_HIDE
win32con.SW_SHOWNORMAL
'''
import sys
import ctypes
import win32con
import win32api
import win32process
import win32gui

def executeProcess():
    win32api.WinExec("C:\\windows\\system32\\notepad.exe", win32con.SW_HIDE)

def createProcess():
    (hProcess, hThread, dwProcessId, dwThreadId) = win32process.CreateProcess("C:\\windows\\system32\\notepad.exe",None,None,None,0,0,None,None,win32process.STARTUPINFO())
    print (hProcess, hThread, dwProcessId, dwThreadId)

def closeProcess():
    hNoteWnd = win32gui.FindWindow(None, "未命名 - 記事本")
    if hNoteWnd:
        dwNotePid = win32process.GetWindowThreadProcessId(hNoteWnd)
        print dwNotePid
        hNoteHandle = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, False, dwNotePid[1])
        win32process.TerminateProcess(hNoteHandle, 0)
        win32api.CloseHandle(hNoteHandle)

def enumProcess():
    win32process.EnumProcesses()

def enumProcessEx():
    
    __metaclass__ = type;

    class PROCESSENTRY32(ctypes.Structure):
        _fields_ = [
            ("dwSize",ctypes.c_ulong),
            ("cntUsage",ctypes.c_ulong),
            ("th32ProcessID",ctypes.c_ulong),
            ("th32DefaultHeapID",ctypes.c_void_p),
            ("th32ModuleID",ctypes.c_ulong),
            ("cntThreads",ctypes.c_ulong),
            ("th32ParentProcessID",ctypes.c_ulong),
            ("pcPriClassBase",ctypes.c_long),
            ("dwFlags",ctypes.c_ulong),
            ("szExeFile",ctypes.c_char*260)
        ]

    kernel32 = ctypes.windll.LoadLibrary("kernel32.dll");
    pHandle = kernel32.CreateToolhelp32Snapshot(0x2,0x0);

    

    if pHandle==-1:
        sys.exit()

    proc = PROCESSENTRY32()
    proc.dwSize = ctypes.sizeof(proc)

    while kernel32.Process32Next(pHandle,ctypes.byref(proc)):
        print("ProcessName : %s - ProcessID : %d"%(ctypes.string_at(proc.szExeFile),proc.th32ProcessID))

    kernel32.CloseHandle(pHandle)

def showModule(pid):
    hProcess = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, False, pid)
    
    print win32process.EnumProcessModules(hProcess)
