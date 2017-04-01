new=True;
while new:
	print("1 = Add")
    print("2 = Sub")
    print("3 = Multiply")
    print("4 = Division")
    print("5 = Exit program")
	cmd=int((input("Enter the operation to be performed: "))
	if cmd == 1:
		print("Add")
	    a=int(input("Enter the first number: "))
        b=int(input("Enter the second number:"))
        result=a + b
        print (a ,'+' ,b ,'=' , result)
    elif cmd ==2:
        print("Subtraction")
        a = int(input("Enter first number :"))
        b = int(input("Enter secund number :"))
        result = a - b
        print(a ,"-" , b ,"=" , result)
    elif cmd == 3:
        print("Multiply")
        a = int(input("Enter first number :"))
        b = int(input("Enter secund number :"))
        result = a * b
        print(a ,"*" ,b ,"=" , result)
    elif cmd == 4:
        print("Division")
        a = int(input("Enter first number :"))
        b = int(input("Enter secund number :"))
        result = a / b
        print(a ,"/" ,b ,"=" , result)
    elif cmd == 5:
        print("Quit!")
        new = False
