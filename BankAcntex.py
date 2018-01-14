# A class which demonstrates Bank account details of a customer 

class BankAcnt:
	
	def  __init__(self,account_type,amount):
		self.account_type=account_type
		self.amount=amount 

	def deposit(self,deposit_amount):
		self.amount+=deposit_amount 

	def withdraw(self,withdraw_amount):
		self.amount-=withdraw_amount
	def Loanamount(self,loan_amount):
		self.amount-=loan_amount


	def __str__(self):
		return "{} Amount:{} ". format(self.account_type,self.amount)

adi=BankAcnt("Checkings",10000)

print(adi.account_type)
print(adi.amount)

adi.deposit(250000)

print(adi.amount)

adi.withdraw(1500)

adi.Loanamount(250)

print(adi.amount)
print(adi)


