#
# Python Lab Assignment 1
#

#Q1 print "Hello World"

Solution:

print("Hello World")

Output:
Hello World

#Q2 Describe local variable and Global Varibale Code

Solution:

#Local variable: A variable defined inside a function and accessible only within that function.
#Global Variable: A Variable defined outside any function, accessible globally thoughout the  script.

#Global variable
x= "I am Global"

def my_function():

#Local varible:
	y= "I am Local"
	print(y)

my_function
print(x)

Output:
I am Global

#Q3 Write code that describes an indentation Error


Solution:

def swati_function():
print("this line is not indented properly")

#Correct Code
#def swati_function():
#	print("This line indented properly")

Output:
Error
 print("this line is not indented properly")

#Q4 Local and Global variables with Same Name

Solution:

x = "Global Variable"

def my_function():
	x = "Local Variable"
	print("Inside function:", x)
	
my_function()
print("Outside function:", x)

Output:

Inside function: Local Variable
Outside function: Global Variable

#Q5 Code for String , Int, and Float Input

Solution:

#String Input
name= input("Enter Name: ")

# Integer Input
age = int(input("Enter Age: "))

# Float Input
height = float(input("Enter Height: "))

print("Name: " , name)
print("Age: " , age)
print("Height: " ,height) 

Output:

Enter Name: swati
Enter Age: 12
Enter Height: 5.8
Name:  swati
Age:  12
Height:  5.8



