import os
import subprocess
from PIL import Image

pic = './images/validate.png'

im = Image.open(pic)
imgry = im.convert('L')
imgry.show()

threshold = 120
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
out = imgry.point(table, '1')
out.show()
out.save('./images/3.gif')

img = Image.open('./images/3.gif') # Your image here!  
img = img.convert("RGBA")
img.save('./images/3.png')

img2 = Image.open(pic)
img2 = img2.convert("RGBA")
img2.save('./images/3.jpg')
"""
img = Image.open('test.png') # Your image here!  
img = img.convert("RGBA")
"""

"""
import requests，StringIO
r =requests.get(imgurl)
imgbuf = StringIO.StringIO(r.content)
img =Image.open(imgbuf)
"""

def image_to_string(img, cleanup=True, plus=''):
    # cleanup为True则识别完成后删除生成的文本文件
    # plus参数为给tesseract的附加高级参数
    subprocess.check_output('tesseract ' + img + ' ' +
                            img + ' ' + plus, shell=True)  # 生成同名txt文件
    text = ''
    with open(img + '.txt', 'r') as f:
        text = f.read().strip()
    if cleanup:
        os.remove(img + '.txt')
    return text

print(image_to_string('./images/3.gif'))  # 打印识别出的文本，删除txt文件
print(image_to_string('./images/3.png'))
print(image_to_string('./images/3.jpg'))
print(image_to_string(pic) )
"""
print(image_to_string('./images/cc0.gif', False))  # 打印识别出的文本，不删除txt文件
print(image_to_string('./images/cc0.gif', False, '-l eng'))  # 打印识别出的文本，不删除txt文件，同时提供高级参数
"""



