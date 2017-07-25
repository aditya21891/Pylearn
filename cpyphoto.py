#this program is a file to copy all my photos into a folder

import shutil
import time 
import os 
print time.ctime()
def main():
    path = '/Users/adityapratti/Pictures'
    source = os.listdir(path)
    destination = '/Users/adityapratti/Photo'
    for f in source:
        if f.endswith('.JPG'):
            shutil.move(os.path.join(path,f),os.path.join(destination,f))


if __name__=='__main__': 
    main()
