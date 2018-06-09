import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# 第三方 SMTP 服务
mail_host="140.114.200.28"  #设置服务器
mail_user="admin@140.114.200.28"    #用户名
mail_pass="admin"   #口令 
 
 
sender = 'admin@140.114.200.28'
receivers = ['chinyuunin@gmail.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
message = MIMEText('我不知道你到底在想什麼 有種就當面說清楚', 'plain', 'utf-8')
message['From'] = Header("江慧萍", 'utf-8')
message['To'] =  Header("友仁 沈", 'utf-8')
 
subject = '我不知道你到底在想什麼 有種就當面說清楚'
message['Subject'] = Header(subject, 'utf-8')
 
 
try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "邮件发送成功"
except smtplib.SMTPException:
    print "Error: 无法发送邮件"
