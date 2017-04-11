# a program to print the sum of  even numbers from 2 - 100
def sum_even(a, b):
    count = 0
    for i in range(a, b, 2):
        if(i % 2 == 0):
            count += i
    return count
sum_even(0,100)
