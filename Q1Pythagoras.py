# Create a program that will accept the two legs of a right-angle triangle, a and b, and
# display the length of the hypotenuse, c.
# Remember to use prompts for the input and labels for the output. Use the
# formula a2 + b2 = c2 to calculate your answer
import math
a= float(input("Insert length a:"))
b= float(input("Insert length b:"))
Csquared= (a**2) + (b**2)
c= math.sqrt(Csquared)
print("The hypotenuse is:", c)
