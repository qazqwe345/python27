
import zipfile
import threading

def extractFile(zFile,password):
    try:
        zFile.extractall(pwd=password)

        print("Found Password: " , password)
        return password
    except Exception as e:
        
        pass

def main():
    zFile = zipfile.ZipFile('userdata.zip')
    passFile = open('passwords.pay','r')
    for line in passFile.readlines():
        password = line.strip('\n')
        extractFile(zFile,password)
        
 


if __name__=='__main__':
    main()
