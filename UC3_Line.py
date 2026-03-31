#  UC3 — Check which line is larger 

print("Welcome to Line Comparison Computation Program")

import math

# Taking coordinates for Line1
x1=float(input("Enter x1: "))
y1=float(input("Enter y1: "))
x2=float(input("Enter x2: "))
y2=float(input("Enter y2: "))

# Taking coordinates for Line2
x3 = float(input("Enter x3: "))
y3 = float(input("Enter y3: "))
x4 = float(input("Enter x4: "))
y4 = float(input("Enter y4: "))

# calculate both lines length for checking their equality

length1=math.sqrt((x2-x1)**2+(y2-y1)**2) 
length2=math.sqrt((x4-x3)**2+(y4-y3)**2) 

# Compare their length
if length1>length2: 
    print("line1 is greater than line2")
elif length1<length2:
    print("Line2 is greater than line1")
else:
    print("Both are equal")
