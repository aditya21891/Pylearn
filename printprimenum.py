repeat = 'y'
prime = True
number = raw_input("Enter any whole number: ")
number = int(number)
n = number
while n >= 1:
    i = 2
    while i >=2 and i < n:
        if n % i == 0:
            prime = False
            break
        i= i + 1

    if prime == True:
        print (n)
    n =n - 1
    prime = True
