import smtplib
from email.MIMEMultipart import MIMEMultipart
# mutiple parts
from email.MIMEText import MIMEText
from email.utils import getaddresses

sa="adityapratti01@gmail.com"
ta="prattiaditya@gmail.com" 

text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"

uname="adityapratti01"
pwd='iamcool9$'

msg=MIMEMultipart()
msg['From']=sa
msg['To']=ta
msg['Subject']='Message for Ravi'
part1 = MIMEText(text, 'plain')
msg.attach(part1)

srvr=smtplib.SMTP('smtp.gmail.com:587')

srvr.ehlo()
srvr.starttls()
srvr.ehlo()

srvr.login(uname,pwd)
srvr.sendmail(sa,ta,msg.as_string())
srvr.quit()

