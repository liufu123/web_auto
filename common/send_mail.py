import yagmail
from liufu_web_auto.common.read_ini import Read_ini
import os
import time

class Send_mail():
    '''发送邮件'''
    def send_mail(self,report):
        config = Read_ini()
        username = config.get_value('mail_account', 'user')
        psw = config.get_value('mail_account', 'psw')
        # yag = yagmail.SMTP(user='13265861735@163.com', password='lfjj0918', host='smtp.163.com')
        yag = yagmail.SMTP(user = username,password = psw,host = 'smtp.163.com')
        subject = "自动化测试报告"
        zhengwen = "请查看附件"
        yag.send('527535141@qq.com', subject, contents=[zhengwen, report])
        print("邮件发送成功！")

if __name__ == "__main__":
    report_path = os.path.join(os.getcwd(), 'report')
    now_time = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = os.path.join(report_path, now_time + 'result.html')
    a = Send_mail()
    a.send_mail(filename)