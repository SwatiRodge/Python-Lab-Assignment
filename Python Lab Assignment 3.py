#
# Python Lab assignment 3
#


# Q1 Using input() function take one number from the user and using ternary operators check whether the number is even or odd

#soltion:

num=int(input("enter an integer "))

if num%2==0:
	print("even")
else:
	print("odd")

#Output:

enter an integer 3
odd

# Q2 Using input  function take two number and then swap the number

#Soluion:

a = int(input("Enter the First number: "))
b = int(input("Enter the Second number: "))

a,b = b, a

print("After Swapping First number : ", a, "After Swapping Second Number: ", b)

#Output:

Enter the First number: 3
Enter the Second number: 4
After Swapping First number :  4 After Swapping Second Number:  3


#Q3 Write a Program to Convert Kilometers to Miles

#Solution:

Kilometers = float(input("Enter Distance In Kilomemeters: "))

miles = Kilometers / 1.609

print("Kilometers is equal to Miles : ", round(miles,2 ))

#Output:

Enter Distance In Kilomemeters: 3
Kilometers is equal to Miles :  1.86



# Q4 Find the Simple Interest on Rs. 200 for 5 years at 5% per year

#Solution:

principal = 200
rate = 5 
time = 5

simple_interest = (principal * rate * time) / 100

print(f"The simple interest is Rs. {simple_interest}.")


#Output:

The simple interest is Rs. 50.0.




