import smtplib,os

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.utils import getaddresses
from email.utils import COMMASPACE,formatdate
from email.MIMEBase import MIMEBase
from email import encoders

sa="adityapratti01@gmail.com"
ta="prattiaditya@gmail.com" 

# content of email
text = "Hi Ravi! \n Thank you \n Have a good day\n"

uname="adityapratti01"
pwd='iamcool9$'

msg=MIMEMultipart()
msg['From']=sa
msg['To']=ta
msg['Subject']='Message for Ravi'
part1 = MIMEText(text, 'plain')
msg.attach(part1)

file= "raw.txt"
attachment=open("/Users/adityapratti/Desktop/mypyscript/python/raw.txt", "rb")
part=MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition','attachment;filename= %s'% os.path.basename(file))
        

srvr=smtplib.SMTP('smtp.gmail.com:587')
srvr.ehlo()
srvr.starttls()
srvr.ehlo()

srvr.login(uname,pwd)
srvr.sendmail(sa,ta,msg.as_string())
srvr.quit()

