#A program which indicate me take a break for every 2 hours from system 
import webbrowser 
import time 

for x in range(4):
  time.sleep(2*60)
  webbrowser.open("https://www.youtube.com/watch?v=jIqRbFQl-ds")
