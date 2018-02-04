# this python script is used to reply in whatsapp 
from selenium import webdriver


chrome_path = "/Users/adityapratti/Desktop/mypyscript/chromedriver"
driver = webdriver.Chrome(chrome_path)
driver.get('http://web.whatsapp.com')	


name = raw_input('Enter the name of user or group : ')
msg = raw_input('Enter the message : ')
count = int(raw_input('Enter the count : '))

#Scan the code before proceeding further
#input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//div[contains(@title = "{}")]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('input-container')

for i in range(count):
    msg_box.send_keys(msg)
    driver.find_element_by_class_name('compose-btn-send').click()

