# a program to Caluculate values
print("Welcome to  my calc")
typeofop=raw_input("Would you like to add(a), substract(s), Multiply(m), Divison(d) ? ")
if typeofop == "a":
    x=int(input("Enter the first number: "))
    y=int(input("Enter the second number:"))
    print x + y
elif typeofop == "s":
    x=int(input("Enter the first number: "))
    y=int(input("Enter the second number:"))
    print x - y
elif typeofop == "m":
    x=int(input("Enter the first number: "))
    y=int(input("Enter the second number:"))
    print x * y
elif typeofop == "d":
    x=int(input("Enter the first number: "))
    y=int(input("Enter the second number:"))
    print x / y
else :
    print("Wrong input" + typeofop)
