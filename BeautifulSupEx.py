# this is an example of Beautiful soup 
from bs4 import BeautifulSoup
import urllib2

url = "http://www.pythonforbeginners.com"

content = urllib2.urlopen(url).read()

soup = BeautifulSoup(content)

print soup.prettify()

