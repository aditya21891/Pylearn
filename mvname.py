#  A python script to read Link from text file and display the movie names in website 
from urlparse import urlparse 
import urllib2
import re 
from bs4 import BeautifulSoup
response=urllib2.urlopen("http://www.5starmusiq.com/Latest.asp")
html=response.read()
# print html
obj=urlparse(html)
mname=re.findall(r"<td colspan=\"2\"><h1 align=\"center\">(.*?)</h1></td>",str(html))
print mname 
soup = BeautifulSoup(html,"lxml")
for line in soup.find_all('a'):
	print(line.get('href'))