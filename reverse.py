# a python program to print the reverse of a string
# a function to print the reverse
def reverse(txt):
    lst = []
    count = 1

    for i in range(0,len(txt)):
        lst.append(txt[len(txt)-count])
        count += 1

    lst = ''.join(lst) # join the letters together without a space
    return lst
    
