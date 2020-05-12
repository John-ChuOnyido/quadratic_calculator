#This program solves algebraic expression where the coefficient of x on the right is 0.
def first_degree():
	y = -50
	while y < 50:
		if 2*y + 5 == 13:
			print("Y =", y)
		y += 1
		#calling the function
first_degree()

"""This program solves the quadratic equation of a kinds"""
from math import sqrt #this imports square root form math library
def quad():
	X1 = (-b + sqrt(b**2-4*a*c))/(2*a)
	X2 =(-b-sqrt(b**2-4*a*c))/(2*a)
	print("The solution to the quadratic equation are ", X1, "and", X2)

a = int(input("Please enter the value of a: " ))
b = int(input("Please enter the value of b: " ))
c = int(input("Please enter the value of c: " ))
	
quad()

"""This program solves polynomial of power 3"""
def polynomial(x):
	return x**3-3*x**2-6*x+8
def poly_values():
	x = -100
	while x < 100:
		if John_Chu(x) == 0:
			print("Your solutions are :", x)
		x += 1
			
poly_values()


"""This program allows the user to solve algebraic expression this type: ax+b = cx+d"""
def plugin():
	x = (d-b)/(a-c)
	return "The value of x is:",x
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
d = int(input("Enter the value of d: "))
#calling the function
print(plugin())
