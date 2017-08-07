# a python program to fing the BMR rate 
wght=input("Please enter your weight in pounds:")
hght=input("Enter your height in inch:")
age=input("Enter your age: ")
bmr=66.5 + (6.23*wght) + (12.7*hght) - (6.8*age)
bar=round(bmr)
print bar  

