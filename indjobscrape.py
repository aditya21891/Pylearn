# this python script to extract jobs from a website indeed 

import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time

URL ="https://www.indeed.com/jobs?q=Devops+Engineer+%24+40%2C000&l=Chicago%2C+IL"
page = requests.get(URL) 
soup = BeautifulSoup(page.text, “html.parser”) 
print(soup.prettify()) 
