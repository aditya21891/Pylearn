# a python script to read all the links from a webpage and print them

import urllib2
import re
import linkGrabber

links=linkGrabber.Links("https://www.indeed.com/jobs?q=devops+engineer&sort=date")
gb=links.find(Limit=20,pretty=True)

print (gb)

