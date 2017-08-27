# A python file to collect social data

import urllib2
import json

def fullcontact(email):
    api_key='9ba137efe64eb200'
    email=email
    fullurl='https://api.fullcontact.com/v2/person.json?apiKey=' + api_key + '&email=' + email
    loadurl=urllib2.urlopen(fullurl)
    jsonData=json.load(loadurl)


    print jsonData
    photos=jsonData['photos']

    for item in photos:
        print item['url']

fullcontact("prattiaditya@gmail.com")
