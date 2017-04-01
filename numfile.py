# program to count the number of files in a folder 
import os,sys
path= sys.argv[1]
files = os.listdir(path)
name= os.getcwd()
#rn= os.rename(old,new)

print path
print name
print len(files)