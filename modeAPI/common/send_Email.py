'''巡检，将结果通过邮件通知给对应开发'''
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from common.config_yaml import YamlHandler

'''
1. 创建SMPT的操作对象并连接smtp目标服务器，可以是163，QQ
2. 根据自己的账号登录目标服务器（自己邮箱地址和邮箱授权码）
3. 调用对象中的方法，发送邮件到目标地址

'''

#读取yaml数据
read_date = YamlHandler('../config/config_email.yaml').read_yaml()
def send_email_by_qq(reciver):
    sender_mail = read_date['sender_mail']
    sender_pass = read_date['sender_pass']  # QQ邮箱授权码
    print(read_date)

    # 设置总的邮件体对象，对象类型为mixed
    msg_root = MIMEMultipart('mixed')
    # 邮件添加的头尾信息等
    msg_root['From'] = read_date['msg_root_From']
    msg_root['To'] = reciver
    # 邮件的主题，显示在接收邮件的预览页面
    subject = read_date['subject']
    msg_root['subject'] = Header(subject, 'utf-8')

    # 构造文本内容
    text_info = read_date['text_info']
    text_sub = MIMEText(text_info, 'plain', 'utf-8')
    msg_root.attach(text_sub)

    # 构造超文本
    url = read_date['url']
    html_info = read_date['html_info']
    html_sub = MIMEText(html_info, 'html', 'utf-8')
    # 如果不加下边这行代码的话，上边的文本是不会正常显示的，会把超文本的内容当做文本显示
    html_sub["Content-Disposition"] = 'attachment; filename="test.html"'
    # 把构造的内容写到邮件体中
    msg_root.attach(html_sub)

    # 构造图片
    image_file = open(read_date['image_path'],'rb').read()
    image = MIMEImage(image_file)
    image.add_header('Content-ID', '<image1>')
    # 如果不加下边这行代码的话，会在收件方方面显示乱码的bin文件，下载之后也不能正常打开
    image["Content-Disposition"] = 'attachment; filename="red_people.png"'
    msg_root.attach(image)

    # 构造附件
    txt_file = open(read_date['txt_file_path']).read()
    txt = MIMEText(txt_file, 'base64', 'utf-8')
    txt["Content-Type"] = 'application/octet-stream'
    # 以下代码可以重命名附件为hello_world.txt
    txt.add_header('Content-Disposition', 'attachment', filename='hello_world.txt')
    msg_root.attach(txt)

    try:
        sftp_obj = smtplib.SMTP('smtp.qq.com', 25)
        sftp_obj.login(sender_mail, sender_pass)
        sftp_obj.sendmail(sender_mail, reciver, msg_root.as_string())
        sftp_obj.quit()
        print('sendemail successful!')

    except Exception as e:
        print('sendemail failed next is the reason')
        print(e)


if __name__ == '__main__':
    # 可以是一个列表，支持多个邮件地址同时发送，测试改成自己的邮箱地址
    reciver = read_date['reciver']
    send_email_by_qq(reciver)
