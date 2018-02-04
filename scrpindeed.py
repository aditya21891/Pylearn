# this python script to extract jobs from a website indeed 

import requests
import bs4
from bs4 import BeautifulSoup
import time

URL ="https://www.indeed.com/jobs?q=Devops+Engineer+%24+40%2C000&l=Chicago%2C+IL"
page = requests.get(URL)
a=page.text 
soup = BeautifulSoup(a, "html.parser") 
print(soup.prettify()) 

def extract_job_title_from_result(soup):
  jobs = []
  for div in soup.find_all(name='div', attrs={'class':'row'}):
    for a in div.find_all(name='a', attrs={'data-tn-element':'jobTitle'}):
        jobs.append(a['title'])
        return(jobs)

extract_job_title_from_result(soup)

