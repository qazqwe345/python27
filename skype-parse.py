import sqlite3
import optparse
import os

def printProfile(skypeDB):
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute("select fullname,skypename,city,country,datetime(profile_timestamp,'unixepoch') from accounts;")

    for row in c:
        print('[*]--Found Account --')
        print('[+]User:' + str(row[0]))
        print('[+]Skype Username:'+str(row[1]))
        print('[+]Location:'+str(row[2])+','+str(row[3]))
        print('[+]Profile Date:'+str(row[4]))

def printContacts(skypeDB):
    
