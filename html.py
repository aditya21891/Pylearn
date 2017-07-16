# this is a python script to scrape a date from the website
import urllib
import re
urls=["http://store.steampowered.com/","http://www.cnn.com/","https://www.nytimes.com/"]
i=0
regex ='<title>(.+?)</title>'
pattern=re.compile(regex)
while i< len(urls):
    htmlfl=urllib.urlopen(urls[i])
    htmltxt=htmlfl.read()
    title=re.findall(pattern,htmltxt)
    print title
    i=+1
