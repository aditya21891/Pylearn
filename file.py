# program to enter a text from a file and view it 
from sys import argv
script,filename=argv
txt= open(filename)
print"Here's your file %r:" %filename 
print txt.read()
