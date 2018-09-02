import win32api
import win32process

hThread = None
def suspendThread(hThread):
    win32process.SuspendThread(hThread)

def resumeThread(hThread):
    win32process.ResumeThread(hThread)

def beginthreadex(function,args_tuple):
    hThread = win32process.beginthreadex(None, 0, function, args_tuple, 0)
    print hThread
    return hThread

def p(args):
    print args
