#
#Python Lab Assignment 2
#


#Q1 Write a Program for Arithmetic Operator

#Solution:

def ex1():
	a=10
	b = 3
	print(a+b)
	print(a-b)
	print(a*b)
	
	print(a/b)
	print(b/a)
	print(a//b)
	print(b//a)

	print(a%b)
	print(b%a)
	print(a**b)

ex1()

#Output:
13
7
30
3.3333333333333335
0.3
3
0
1
3
1000


#Q2 Write a program for assigenment Operator

#Solution:

def ex2():
	c = 10		
	c += 1
	print(c)
	
	c += 3 		#c = c  +3
	print(c)

	c -= 2		#c c - 2
	print(c)
ex2()

#Output:
11
14
12

#Q3 Write a program for Bitwise Operators

#Solution:

def ex3():
	a = 9 #1001
	b = 8 #1000
	print(bin(9))
	print(bin(8))
	print(a & b, bin(a & b))
	print(a | b, bin(a | b))
	print(a ^ b, bin(a ^ b))
ex3()

#Output:
0b1001
0b1000
8 0b1000
9 0b1001
1 0b1

#Q4

#Soltion:

def find_greatest(num1 , num2, num3):
	if num1 >= num2 and num1 >= num3:
		return num1
	elif num2 >= num1 and num2 >= num3:
		return num2
	else:
		return num3	

no1= float(input("Enter the First Number: "))
no2= float(input("Enter the Second Number: "))
no3= float(input("Enter the Third Number: "))	

greatest=find_greatest(no1 , no2, no3) 
print("greatest no : ", greatest)

 	
#Output:

Enter the First Number: 3
Enter the Second Number: 4
Enter the Third Number: 5
greatest no :  5.0


#Q5 Calculate Area of Circle

#Solution

def compute(radius):
	area =3.14*radius**2
	
	print("area=" ,area)
	

radius=float(input("enter radius "))
if radius >0.0:
	compute(radius)
else:
	print("invalid radius")

#Output:

enter radius 3
area= 28.26

#Q6 Calculate Area of Triangle

#Solution:

#input
Base = float(input("Enter the base of triangle: "))
Height = float(input("Enter the height of triangle: "))


# Calculate area
area = 0.5 * Base * Height

#output
print(f"The area of the triangle is: {area}")


#Output:
Enter the base of triangle: 3
Enter the height of: 4
The area of the triangle is: 6.0

 

#Solution:

def calculate_area(length, width):
	return length * width

length = float(input("Ener the length: "))
width = float(input("enter the width "))

area = calculate_area(length, width)
print(f"The area of rectangle is: {area}")

#Output:

Ener the length: 5
enter the width 5
The area of rectangle is: 25.0



# Q8 Calculate area of a square

# solution:
 
def calculate_area(side):
	return side * side

side = float(input("Enter the side of the square: "))

area=  calculate_area(side)
print(f"The area of the square is: {area}")

#Output:

Enter the side of the square: 6
The area of the square is: 36.0







