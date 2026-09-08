import math
print("Enter length of side A.")
a = float(input())
print("Enter length of side B.")
b = float(input())

c1 = math.sqrt(a*a+b*b)/2
c2 = round(c1,2)

print("C is equal to", c2)