# a python script to send emails
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login("prattiaditya@gmail.com", "marMAG91$")
msg = "HI!"
server.sendmail("prattiaditya@gmail.com", "adityapratti01@gmail.com", msg)
server.quit()
