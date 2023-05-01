# Create a program that will ask the user an addition question.
# The program will generate two random numbers between 1 and 100, and display them as an addition question with appropriate prompts.
import random
a= random.randrange(1,100)
b= random.randrange(1,100)
print(a, "+", b, "=",)
userinput= int(input())
if userinput== (a+b):
    print("Correct!")
if userinput!= (a+b):
    print("The answer was", a + b)
