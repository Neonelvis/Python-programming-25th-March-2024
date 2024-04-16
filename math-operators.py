# Python 3 Numbers - Math Operators

# Python defines three numerical types namely:
# -> Integers
# -> Floating-point numbers 
# -> Complex numbers

# The complex numbers are usually used in some advanced math operations and are not of great interest for our current needs. Instead we will work a lot with integers and floating point numbers and thats why we will focus on these two numerical types and their corresponding operators and functions. 

# Lets define a variable and assign it an integer and another variable associated with a floating-point number, or float.

# Consider the following variables 
num1 = 10
num2 = 2.51

# Check the type of these variables -> Python provides the type() funtion for this

print(type(num1)) # returns <class 'int'>
print(type(num2)) # returns <class 'float>

# Lets see what operations we are able to perform using integers and floating point numbers 
# 1. Arithmetic Operators 
x = 20
y = 6 

# 1. Addition - '+' 
print(x + y)
# 2.Subtraction -> '-'
print (x - y)
# 3. Multiplication -> '*'
print (x * y) 
# 4. Division -> '/' 
print (x / y) 
# 5. Integer division -> '//' (return the integer from a division)
print(x//y)
# 6. Modulo -> '%' (this means finding out the remainder after the division of one number by another)
print (x % y)
# 7. Raising to a power -> '**' 
print (x**y)

# Challenge time
# Write a Python program that asks the user for the radius of a circle and the returns the perimeter and area of the circle 

radius = int(input ("Radius = "))
perimeter = (radius * 2  * 22/7)
print ("Perimeter = " + str(perimeter))
area = (22/7 * radius**2)

print ("Area = " + str(area))

# define PI 
PI = 22/7 

# Ask the user for the radius
radius = float(input("Please enter the circle radius: "))

# compute the perimeter ofthe circle 
perimeter = PI * (radius + radius)

# compute the area of the circle 
area = PI * (radius * radius)

# output the results in a nice format 
print (f"The perimeter and area of a circle whose radius is {radius}cm, is {perimeter}cm and {area}cm\u00B2 respectively.")

print(f"Pound sign: \u00A5") 


# 2. Comparison Operators -> used to compare values and returns booolean values (True or False)
a = 20
b = 6

# less than -> '<' 
print(a < b)
# greater than -> '>'
print (a > b)
# less than or equal to -> '<=' 
print (a <= b)
# greater than or equal to -> '>=' 
print (a >= b)
# equal to -> '==' 
print (a == b)
# not equal to -> '!=' 
print (a != b)


# Order of Evaluation in Python 

# lets talk about the order of evaluation for these operators inside a mathematical expression 
# What if we have to deal with multiple operators within the same expression? which operations have priority over others?

# Well, the order is as follows:
# 1. Firstly, the raising to a power has the highest priority 
# 2. Then, we have the multiplication, division, and modulo operation with equal priorites, and lastly 
# 3. We have addition and subtraction also with equal priorities

# Lets see an example
# 100 - 5 **2 /5 *2
# 100 - 25 / 5 *2 
# 100 - 5 * 2
# 100 - 10 
# 90 

# Conversions 
# lets see how we can convert an integer to a float and vice-versa 
# Well, Python has two functions available for these operations. lets see them

print(int(1.7)) # returns 1 (truncation)
print(int(19.9999)) # returns 19 (truncation)
# The result is 1, because the int() function will round down the number in between the parantheses to the nearest integer, which is 1 

print(float(2)) # returns 2.0 
# The result is 2.0. The float() function will add .0, converting 2 from integer to a floating-point number 

# Finally, lets have a look at a few functions which may come in handy in the future when working with numbers. 

# 1. abs() :returns the absolute value. This is actually the distance between the number that we provide and zero 
print(abs(5)) # returns 5
print(abs(-15)) # returns 15 

# 2. max() : return the largest number between 2 numbers 
print(max(2,10)) # return 10

# 3. min() : returns the smallest number between 2 numbers 
print(min(2,10)) # return 2

# 4. pow() : another way of raising a number to a power using built-in Python function 
# e.g. pow(a,b) where a is the base number and b is the exponent 
print(pow(10,3)) # returns 1000 

# challenge time
# Write a Python program that prompts the user to enter their name and age. The program will then output the decades and the minutes the user has lived. Print out the results in a nice format 
# (A decade is 10 years e.g. 22 years old -> 2 decades)

# Get the username
user_name = input ("Please enter your Name: ")

# get the user age 
user_age = int(input("Enter your age too: "))

# convert the user age into minutes
age_in_minutes = user_age * 365 * 0.25 * 24 * 60

# convert the user age into decades lived 
decades_lived = user_age // 10

# print out the user info in a nice format

print(f"Hello, {user_name}, you have lived for {decades_lived} decade(s), and {age_in_minutes} minutes which means you are {user_age} years old")