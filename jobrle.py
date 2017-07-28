# this program helps me to take input from me  and search for the keyword in a URL 


from bs4 import BeautifulSoup
import requests 
import re 
r=requests.get("https://www.indeed.com/jobs?q=devops+engineer&jt=contract&sort=date/")
soup=BeautifulSoup(r.content)
links=soup.find_all("a")
for link in links:
	 print "<a href='%s'>%s</a>"%(link.get("href"),link.text)  
