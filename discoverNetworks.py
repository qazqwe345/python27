import optparse
import mechanize
import re
import urllib
import win32api

def wiglePrint(username,password,netid):
    browser = mechanize.Browser()
    reqData = urllib.urlencode({'credential_0':username,'credential_1':password})
    browser.open('https://wigle.net/login',reqData)
    params = {}
    params['netid'] = netid
    reqParams = urllib.urlencode(params)
    respURL = 'https://wigle.net/search'
    resp = browser.open(respURL,reqParams).read()
    mapLat = 'N/A'
    mapLon = 'N/A'
    rLat = re.findall(r'maplat=.*\&',resp)

    if rLat:
        mapLat = rLat[0].split('&')[0].split('=')[1]
        rLon = re.findall(r'maplon=.*\&',resp)

        if rLon:
            mapLon = rLon[0].split
        print '[-] Lat:'+mapLat+',Lon:'+mapLon


wiglePrint("qazqwe345","qqq111","00:1c:7f:3f:f2:d1")
