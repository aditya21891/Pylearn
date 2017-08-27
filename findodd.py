# a program to find whether a number is even or odd and find multiples of 4 
Number = int(input('Enter a number: '))
Division_number = int(input('Enter the number to divide with: '))
if Number % 2 == 0:
    print('The number entered ' + str(Number) + ' is Even.\n')
else:
    print('The number entered ' + str(Number) + ' is Odd.')
if Number % 4 == 0:
    print('The number entered ' + str(Number) + ' is a multiple of 4.')
else:
    print('The number entered ' + str(Number) + ' is not a multiple of 4.')
if Number % Division_number == 0:
    print(Number, "divides evenly by", Division_number)
else:
    print(Number, "doesn't divide evenly by", Division_number)
