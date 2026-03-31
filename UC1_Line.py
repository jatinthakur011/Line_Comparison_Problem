# Start with Displaying Welcome to Line Comparison Computation Program on Master Branch

print("Welcome to Line Comparison Computation Program on Master Branch")

# UC1 — Calculate Line Length
import math

# taking coordinates input
x1=float(input("Enter x1: "))
x2=float(input("Enter x2: "))
y1=float(input("Enter y1: "))
y2=float(input("Enter y2: "))

# calculate length using formula
length=math.sqrt((x2-x1)**2 + (y2-y1)**2)

print("Length of line= ",length)