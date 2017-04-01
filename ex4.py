# program to enter a text from a file and view it 
from sys import argv # for giving input 
script,filename=argv # input variables
txt=open(filename,'w')    #open function to  read  file 
print"Here's your file %r:" %filename 
print txt.read()
