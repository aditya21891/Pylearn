# a script to extract only devops related posts from LinkedIn
import webbrowser
import re 
import urllib2

new=2;
url="https://www.linkedin.com/feed/"
webbrowser.open(url,new=new);
Page_Content = urllib2.urlopen(url).read()
pattern = re.compile("\n.*DEVOPS.*\n")
matching_lines = re.findall(pattern, Page_Content)

