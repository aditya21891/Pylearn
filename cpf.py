#program for functions
def two_parm(*args):
	arg1,arg2=args
	 print"arg1: %r,arg2: %r" %(arg1,arg2)
	 
def one_parm(arg1):
	print"arg1:%r" %arg1

def noneparm():
	print"I got nothing."
	
two_parm("Adi","prat")
one_parm("sun")
noneparm()

	