#
#Swati Suhas Rodge
#Python Lab Assignment No 6
#

#Q1 Print the reverse order series  using a while loop
#Solution
n = 15
while n >= 1:
    
	print(n)
    
	n = n - 1
#Output:
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1


#Q2 Create a code that describe the use of break statement in while loop
#Solution:

x = 0


while x < 10:
    
	print(x)
    
	if x == 3:         
		break
    
	x += 1

#Output:

0
1
2
3

#Q3 Write a Python program using a while loop to iterate through each character of the string "Python" and print each character on a new line. Additionally, calculate and print the length of the string.

#Solution:
string = "Python"
index = 0

while index < len(string):
	print(string[index])
	index += 1
print("length of the string is ", len(string))


#Output:
P
y
t
h
o
n
length of the string is  6


#Q4  Write a Python program that takes an integer input from the user and calculates its factorial using a while loop. Display the result as the factorial of the entered number.
#Solution:
num = int(input("Enter  an integer "))
 
factorial = 1
i = 1
while i <= num:
	factorial = factorial * i
	i = i + 1
print("Factorial of " , num , "is : ", factorial) 


#Output:
Enter  an integer 5
Factorial of  5 is :  120



# Q.5 Write a python program to check whether a number is palindrome or not? 
#Solution:

name = input("Enter a string: ")

s2 = ""

for s in name:
	s2 = s + s2

# comapare original vs reverse

if name == s2:
	print("String is palindrome")
else:
	print("It is not a palindrome")

#Output:

Enter a string: nayan
String is palindrome



# Q.6 Accept numbers using input() function until the user enters 0. If user input 0 then break the while loop and display the sum of all the numbers.
#Solution:


total_sum = 0

while True:

	num = int(input("Enter a number: "))
	
	# Break the loop if the input is 0
	if num == 0:
		break

	total_sum = total_sum + num

print("The sum of all numbers is: ", total_sum)


#Output:

Enter a number: 45
Enter a number: 76
Enter a number: 87
Enter a number: 98
Enter a number: 0
The sum of all numbers is:  306


# Q.7) Program to check whether the given number is Armstrong or not.



# Function to check if a number is an Armstrong number

def is_armstrong(number):
    
   
	num_digits = len(number)
    
	armstrong_sum = 0
    
	i = 0  
	# While loop to calculate the sum of powers of each digit
    
	while i < num_digits:
        
		digit = int(number[i])  # Get the current digit
        
	armstrong_sum += digit ** num_digits  # Add digit^num_digits to the sum
       
	i += 1  # Move to the next digit

    

	return int(number) == armstrong_sum

number1 = input("Enter the first number: ")

number2 = input("Enter the second number: ")


if is_armstrong(number1):
    
	print(f"{number1} is an Armstrong number.")

else:
    print(f"{number1} is not an Armstrong number."

if is_armstrong(number2):
    
	print(f"{number2} is an Armstrong number.")

else:
    print(f"{number2} is not an Armstrong number.")




#Output:


Enter the first number: 457

Enter the second number: 153

457 is not an Armstrong number.

153 is an Armstrong number.



