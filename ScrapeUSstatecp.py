# this is a program to scrape states with capitals.

import urllib2
from bs4 import BeautifulSoup

link="http://www.50states.com/tools/thelist.htm"
page=urllib2.urlopen(link)
soup = BeautifulSoup(link, ‘html.parser’)
  
