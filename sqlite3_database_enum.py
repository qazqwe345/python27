import sqlite3
import os

Dir = r"C:\Users\san\AppData\Roaming\Mozilla\Firefox\Profiles\wbeec143.default"
Dir2 = r"C:\Users\san\.sqlmap\output\www.sharecourse.net"
Dir3 = r"C:\Python27"


def enum(fulldir):
    conn = sqlite3.connect(fulldir)
    c = conn.cursor()
    c2 = conn.cursor()
    c.execute("select tbl_name from sqlite_master where type=='table'")

    for row in c:
        print str(row)
        row = str(row).replace("(u'","").replace("',)","")
        sql = "select sql from sqlite_master where tbl_name=='"+row+"' and type=='table'"
        c2.execute(sql)
        for colmn in c2:
            print (colmn)
        sql = "select * from "+row
        c2.execute(sql)
        
        wr = open("database.txt",'wb')
        rows = c2.fetchall()
        for i in rows:
            for j in i:
                
                wr.write(str(j))
        wr.close()
        #print rows
        '''for colmn in c2:
            print colmn
        '''
def search(Dir):
    dirList = os.listdir(Dir)
    print (dirList)
    for fileName in dirList:
        fullName=os.path.join(Dir,fileName)
        
        try:
            enum(fullName)
            print (fullName)
        except:pass
        


enum(r"c:/Python27/LoginData.sqlite")
#search(Dir3)
