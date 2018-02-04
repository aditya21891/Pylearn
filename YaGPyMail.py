# this script is to send Email using yag 
import yagmail
yag = yagmail.SMTP()
yag = yagmail.SMTP('prattiaditya@gmail.com', 'iamcooL9')
subject = 'Testing for Yagmail'
body = 'Test Email is working'
to='adityapratti01@gmail.com'

yag.send(to = to, subject = subject,contents = body)
