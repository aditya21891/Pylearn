# Introduction to Classes in Python 

class Student:

	def __init__(self,name,grade,age):
		self.name=name
		self.grade=grade
		self.age=age

kitty=Student('kitty',85,15)
danny=Student('danny',80,20)

print(kitty.name)
print(danny.grade)
print(danny.age)


