# a python program to send an email
import smtplib
import email.utils
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("adityapratti01@gmail.com", "iamcool9$")

msg = "cool baby!"
server.sendmail("adityapratti01@gmail.com", "prattiaditya@gmail.com", msg)
server.quit()
