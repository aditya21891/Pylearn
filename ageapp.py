# This is the prep work for Age caluculator app 

import datetime
import Tkinter as tk 

window=tk.TK() 
window.geometry("400*400")

class Person:

	def __init__(self,name,birthdate):
		self.name=name
		self.birthdate=birthdate 

	def age(self):
		today=datetime.date.today()
		age=today.year - self.birthdate.year 
		return age

adi=Person('Aditya', datetime.date(1991,8,21))
print(adi.name)
print(adi.birthdate)

print(adi.age())

