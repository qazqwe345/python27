
import win32api
import win32gui
import win32con
def onClose():
    hWnd = win32gui.FindWindow('Notepad', None)
    if hWnd==0:
        win32gui.MessageBox(0,"did'n find notepad","cc",0)
    else:
        win32gui.SendMessage(hWnd, win32con.WM_CLOSE, 0, 0)


def onExec():
    win32api.WinExec("notepad.exe", win32con.SW_SHOW)


def onEditWnd():
    hWnd = win32gui.FindWindow(0, '�s��r���.txt - �O�ƥ�')
    if hWnd==0:
        win32gui.MessageBox(0,"did'n find notepad","cc",0)
        return
    pCaptionText = '��������'
    win32gui.SendMessage(hWnd, win32con.WM_SETTEXT, 0, pCaptionText)

def onGetWnd():
    hWnd = win32gui.FindWindow(0, '�s��r���.txt - �O�ƥ�')
    print win32gui.FindWindow(0, '���R�W - �O�ƥ�')
    print win32gui.FindWindow(0, '�s��r���.txt - �O�ƥ�')
    if hWnd==0:
        win32gui.MessageBox(0,"did'n find notepad","cc",0)
        return
    pCaptionText='0'*1024
    win32gui.SendMessage(hWnd, win32con.WM_GETTEXT, 1024, pCaptionText)
    win32gui.MessageBox(0,pCaptionText,"cc",0)
