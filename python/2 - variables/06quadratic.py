# create a program to find solve the quadratic formula
# x = (-b + (b*b - 4*a*c) **.5) / (2*a)
# x = (-b - (b*b - 4*a*c) **.5) / (2*a)

a = int(input("enter value for a: "))
b = int(input("enter value for b: "))
c = int(input("enter value for c: "))

quad1 = (-b + (b*b - 4*a*c) **.5) / (2*a)
quad2 = (-b - (b*b - 4*a*c) **.5) / (2*a)

print(quad1)
print(quad2)