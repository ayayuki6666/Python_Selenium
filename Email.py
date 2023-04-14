import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

mail_port="smtp.qq.com"
mail_user="2239301685@qq.com"
mail_pwd="vtuwaudhryylebci"
mail_rece="yaolin6666@gmail.com"
# 创建 SMTP 对象
smtp = smtplib.SMTP()
# 连接（connect）指定服务器
smtp.connect(mail_port, port=25)
# 登录，需要：登录邮箱和授权码
smtp.login(user=mail_user, password=mail_pwd)

message = MIMEMultipart()

message.attach(MIMEText('Python 邮件发送测试……', 'plain', 'utf-8'))
message['From'] = Header("Shino", 'utf-8')  # 发件人的昵称
message['To'] = Header("Shino", 'utf-8')  # 收件人的昵称
message['Subject'] = Header('Python SMTP 邮件测试', 'utf-8')  # 定义主题内容

att1 = MIMEText(open('Test_02/unit_result.html', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="unit_result.html"'
message.attach(att1)

smtp.sendmail(from_addr=mail_user, to_addrs=mail_rece, msg=message.as_string())