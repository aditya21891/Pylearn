# A python script to show number of string occurrences in a file.
from sys import argv 
script,file=argv 
trgt=open(file,'r')         # variable to open the file
cnt=0                       # variable to count the number of times string is repeated
fst=trgt.readlines()        # variable to read the lines of file
for i in fst:               # Loop through the file
	if "adi" in i:
		cnt=cnt+1
print(cnt)
print("Hello I found adi for %d times"%cnt)
trgt.close()