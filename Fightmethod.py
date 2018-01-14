#a Fighter game which uses  methods to decrease the health.

class Fighter:

	def __init__(self,name):
		self.name=name
		self.health=100 
		self.damage=10 

	def attack(self,other_guy):
		other_guy.health=self.health-self.damage
		print("{}attacks{}!".format(self.name,other_guy.name))

	def __str__(self):
		return "{}:{}".format(self.name,self.health)	


sentdex=Fighter("SentDex")
me=Fighter("Adams")
print(sentdex)
print(me)

me.attack(sentdex)
print(sentdex.health)

class Boxer(Fighter):
	