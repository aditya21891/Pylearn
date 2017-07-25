# program to copy and paste files 
from sys import argv 
script,inputfile=argv
def printall(f):
	print f.read()
def rewind (f):
	f.seek(0)
def printaline(linecount,f):
	print linecount, f.readline()

currentfile=open(inputfile)	
print" Let's print the whole file \n"

printall(currentfile)
print" Now let's rewind like  a tape "

rewind(currentfile)
print" The lines in the file"

currentline=1
printaline(currentline,currentfile)

currentline=currentline+1
printaline(currentline,currentfile)

currentline=currentline+1
printaline(currentline,currentfile)
