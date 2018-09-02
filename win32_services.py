import win32service
import win32con

type1 = win32con.SERVICE_DRIVER
type2 = win32con.SERVICE_WIN32

def showServiceList(dwServiceType):
    hSCM = win32service.OpenSCManager(None,None,win32service.SC_MANAGER_ALL_ACCESS)
    enum = win32service.EnumServicesStatus(hSCM, dwServiceType, win32service.SERVICE_STATE_ALL)
    win32service.CloseServiceHandle(hSCM)
    
    for i in enum:
        if i[2][1] == win32service.SERVICE_PAUSED:
            print i[0],"|",i[1],"PAUSED"
        if i[2][1] == win32service.SERVICE_STOPPED:
            print i[0],"|",i[1],"STOPPED"
        if i[2][1] == win32service.SERVICE_RUNNING:
            print i[0],"|",i[1],"RUNNING"


def startService(szServiceName):
    hSCM = win32service.OpenSCManager(None,None,win32service.SC_MANAGER_ALL_ACCESS)
    hSCService = win32service.OpenService(hSCM,szServiceName, win32service.SERVICE_ALL_ACCESS)
    win32service.StartService(hSCService,None)
    win32service.CloseServiceHandle(hSCM)
    win32service.CloseServiceHandle(hSCService)

def stopService(szServiceName):
    hSCM = win32service.OpenSCManager(None,None,win32service.SC_MANAGER_ALL_ACCESS)
    hSCService = win32service.OpenService(hSCM,szServiceName, win32service.SERVICE_ALL_ACCESS)
    win32service.ControlService(hSCService, win32service.SERVICE_CONTROL_STOP)
    win32service.CloseServiceHandle(hSCM)
    win32service.CloseServiceHandle(hSCService)
