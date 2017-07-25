import smtplib
from email.MIMEMultipart import MIMEMultipart 
# mutiple parts 
from email.MIMEText import MIMEText 
from email.utils import getaddresses

sa="prattiaditya@gmail.com"
ta="adityapratti01@gmail.com" 

text = "Hi Adi!\nThank you\nHave a good day\n"



uname="/your username/"
pwd='/your password/'

msg=MIMEMultipart()
msg['From']=sa
msg['To']=ta
msg['Subject']='Message for myself'
part1 = MIMEText(text, 'plain')
msg.attach(part1)


srvr=smtplib.SMTP('smtp.gmail.com:587')

srvr.ehlo()
srvr.starttls()
srvr.ehlo() 

srvr.login(uname,pwd)
srvr.sendmail(sa,ta,msg.as_string())
srvr.quit()
