import smtplib
from email.MIMEMultipart import MIMEMultipart 
# mutiple parts 
from email.MIMEText import MIMEText 
from email.utils import getaddresses

sa="prattiaditya@gmail.com"
ta="adityapratti01@gmail.com" 
body="I am learning mail through python"

uname="prattiaditya"
pwd='marMAG91$'

msg=MIMEMultipart()
msg['From']=sa
msg['To']=ta
msg['Subject']='Message for myself'
msg.attach=MIMEText(body)

srvr=smtplib.SMTP('smtp.gmail.com:587')

srvr.ehlo()
srvr.starttls()
srvr.ehlo() 

srvr.login(uname,pwd)
srvr.sendmail(sa,ta,msg.as_string())
srvr.quit()
