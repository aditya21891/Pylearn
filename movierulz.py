# this python script is used to extract the Tollywood movies from the webpage movierulz

from bs4 import BeautifulSoup
from urllib2 import urlopen
import re 


mvlink="http://www.movierulz.mg/"
tolname=urlopen(mvlink).read()

soup = BeautifulSoup(tolname,'lxml')
#print soup.prettify()

llinks=soup.find_all("a")

for link in llinks:
	print "<a href='%s'>%s</a>" % (link.get("href"),link.text)


latmov=soup.find_all("div",{"class":"boxed-film"})
ltname=soup.find_all("<p><b>")

print ltname 
