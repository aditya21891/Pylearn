# A python program to work with JSON format 

import json 

people_string= '''
{
	"people" ;[
	{
	"name": "John Smith",
	"phone": "845-544-8229",
	"email": ["johnsmith09@yahoo.com","Johndwayne@gmail.com"],
	"has_license": false 
	},
	{
	"name": "Michelle Roy",
	"phone": "945-321-809",
	"email": null,
	"has_license": true
	},
  ]
}
'''
data=json.loads(people_string) 
print(type(data))