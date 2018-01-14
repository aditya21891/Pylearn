#this Python Script reads a Text file and Erase the existing text 

import os 
dir=os.getcwd()
print dir 
tf="samopen.txt"

# this part allows us to read the lines in a file and print it 
with open(tf) as fp:
	for lines in fp:
		print lines

