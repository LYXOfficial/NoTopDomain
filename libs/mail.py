import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
import os
def mail(c="test",t="test",f=""):
    mail_host = "smtp-mail.outlook.com"
    mail_user = "ariasakafeedbacksforprogram@hotmail.com"
    mail_pass = "misakaMikoto0502"
    mail_nick = "NoTopDomain Feedback System"
    sender = 'ariasakafeedbacksforprogram@hotmail.com'
    receivers = ['lyx2010official@outlook.com']
    content = c
    if f:
        content+="\nFrom %s"%f
    title = t
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = formataddr([mail_nick, mail_user])
    message['To'] = ",".join(receivers)
    message['Subject'] = title
    try:
        smtpObj = smtplib.SMTP(mail_host, 587)
        smtpObj.starttls()
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)
if __name__=="__main__":
    mail()