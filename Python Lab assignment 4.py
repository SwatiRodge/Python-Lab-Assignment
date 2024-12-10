# 
# Python Lab assignment $
#

# Q1 Write a Python Program that takes a number as input and prints "Even " if the number is even and "odd if it's odd.

num=int(input("enter an integer "))

if num%2==0:
	print("even")
else:
	print("odd")

#Output:

enter an integer 3
odd

# Q2 Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age.

age = int(input("enter your age: "))
if age >= 18:
	print("Eligible to vote")
else:
	print("Not Eligible to vote")

#Output:


enter your age: 3
Not Eligible to vote


enter your age: 19
Eligible to vote

# Q3. Write a Python program that determines if a given year is a leap year or not.
 
#Solution

year = int(input("Enter a Year "))

if (year % 4 ==0 and year % 100 != 0) or (year % 400 == 0):

	print(year, "year is leap year")
else:
	print(year, "year is not leap year")

#Output

Enter a Year 3
3 year is not leap year

Enter a Year 4
4 year is leap year

#Q4 Create a Python program that checks it a user-given number is positive, negative, or zero.


#Solution:

number = float(input("Enter a number: "))

if number > 0:
    
	print("Positive")

elif number < 0:
    
	print("Negative")

else:
    
	print("Zero")


#Output

Enter a number: 3
Positive

Enter a number: -5
Negative

Enter a number: 0
Zero

#Q5 Write a Python program that determines the largest of three numbers entered by the user.

num1 = float(input("Enter the first number: "))

num2 = float(input("Enter the second number: "))

num3 = float(input("Enter the third number: "))


if num1 >= num2 and num1 >= num3:
    
	print(f"The largest number is {num1}")

elif num2 >= num1 and num2 >= num3:
    
	print(f"The largest number is {num2}")

else:
    
	print(f"The largest number is {num3}")

#Output


Enter the first number: 4
Enter the second number: 5
Enter the third number: 8
The largest number is 8.0


