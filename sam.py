#addition of two numbers 
def sumProblem(x, y):
	sum = x + y
	print(’The sum of ’, x, ’ and ’, y, ’ is ’, sum, ’.’, sep=’’)
def main():
	sumProblem(2, 3)
	sumProblem(1234567890123, 535790269358)
	a = int(input("Enter an integer: "))
	b = int(input("Enter another integer: "))
sumProblem(a, b)
main()