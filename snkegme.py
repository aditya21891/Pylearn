# A snake game using python 

import pygame,sys,random,time 

chek_error=pygame.init()

if chek_error[1] > 0 :
	print("(!) Had {0} inintializing errors , exiting ...". format(chek_error[1]))
	sys.exit(-1)
else:
	print("(+) Pygame successfull initialized !")    
