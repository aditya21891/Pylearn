# a python game to guess a number from 1 to 10
from sys import argv
import random
script,user=argv
prmpt='>'
print "Welcome to the game %s"%user
i=random.randint(1,10)
y=raw_input(prmpt)
m=0
print "the number you guessed %s"%y
if(i ==y):
    print("your guess is right")
    m+=1
    print m
else :
    print "Sorry wrong guess "
