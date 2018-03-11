lower=1
upper=100
primes=[1:100]
print("Prime numbers between",lower,"and",upper,"are:")
for num in range(lower,upper + 1):
    if num > 0:
     for i in range(2,num):
         if (num % i) == 0:
             break
     else:
         print(num)
         primes.append(num)

for i in reverse:
    print primes[i]
