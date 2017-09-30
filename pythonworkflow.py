#/usr/bin/env python 

""" This is a test program to find the number of random guess
a user takes to find a number between 1 and 100 """

import random 
def main():
	print"this is a sample game with python to guess a number:"
	print"We are also going to find out how many tries user takes"
	randomnum=random.randint(1,100)
	found=False
	
	while not found:
		userguess=input("Enter the number you guess:")
		if userguess == randomnum :
			print "You guessed the right number"
			found=True
		elif userguess > randomnum :
			print " Guess lower"
		else:
			print" Guess, higher" 
		

if __name__ =="__main__":
	main()
