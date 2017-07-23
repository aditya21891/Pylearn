# program for break 
import webbrowser
import time 
print (" The current time is "+time.ctime())

totbrk=3
cnt=0
if(cnt<=totbrk):
    time.sleep(60)
    webbrowser.open("https://www.youtube.com/watch?v=h2VbU22H1g8")
    cnt=+1 
