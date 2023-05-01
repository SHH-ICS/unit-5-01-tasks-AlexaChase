# Create a program that accepts 2 numbers from the user.
# Your program will output a random number between the range given by the user.
import random
import math
a=float(input("Input a number: "))
b=float(input("Input another number: "))
if a<b:
    a= math.ceil(a)
    b= math.floor(b)
    c=int(random.randint(a,b))
    print(c)
elif a>b:
    a= math.floor(a)
    b= math.ceil(b)
    c=int(random.randint(b,a))
    print(c)
