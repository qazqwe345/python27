import os
import win32api
import win32con

def returnDir():
    dirs = ['c:\\Recycler\\','C:\\Recycled\\','C:\\$Recycle.Bin\\']
    for recycleDir in dirs:
        if os.path.isdir(recycleDir):
            print recycleDir
            return recycleDir
    return None

def sid2user(sid):
    try:
        key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE,"SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList\\"+sid)
        (value,type) = win32api.RegQueryValueEx(key,'ProfileImagePath')
        user = value.split('\\')[-1]
        print user
        return user
    except:
        return sid

def findRecycled(recycleDir):
    dirList = os.listdir(recycleDir)
    for sid in dirList:
        try:
            files = os.listdir(recycleDir+sid)
            user = sid2user(sid)
            print ('\n[*]Listing Files For User:'+str(user))
            for file in files:
                print('[+]Found File:'+str(file))
        except Exception as e:
            print e

recycledDir = returnDir()
findRecycled(recycledDir)

