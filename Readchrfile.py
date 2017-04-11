# program to read the characters in a file.
from sys import argv
script,filename=argv
txt=open(filename)
print"The name of file is %r:" %filename
print txt.read()
print " Here is the filename"
file_ag=raw_input('$')
txt_ag=open(file_ag)

print txt_ag.read()