# this class is an example of abstraction 

class Animal:
	def __init__(self,name):
		self.name=name

	def talk(self):
		pass

animex=Animal("jenny")

print(animex.name)
print(animex.talk())


class Cat(Animal):

	def talk(self):
		return "Meow"

pets=Cat("Ruby")
print(pets.name)
print(pets.talk())


class Dog(Animal):

	def talk(self):
		return "WOOF"


petdog=Dog("Rocky")
print(petdog.name)
print(petdog.talk())