# Python 3 - Variable

# What is a variable? How to define a variable and what is it good for, in Python?

# A variable is nothing more than just a reserved location in computer's memory, used to sote information - values to be more precise.

#This means that when we create a variable you reserve some space in memory.

# You can store different types of data using a variable - you can store a string, a number, a list or any other data type you can think of.

# Unlike other programming languagges, in Python you dont have to explcitly declare a variable - instead, the declaration is done automatically when you a assign a value to that varaiable, no matter what type of data you decide to assign to that memory location.

# e.g. String username = "Dennis"; in a language like java
# in Python -> usename = "Dennis"

# Futhermore, you can later access the value referenced by that variable and use it in other areas of your Python application.

#Lets think of how you should properly name a variable in Python 

# There are several rules to consider and follow for a clean and compliant code and also for avoiding any conflict with Python's in-built names.

#First, a variable name should always start with a letter, usually lowercase and never start with a number or a symbol. However, there is an excpetiont to this rule - some variable names start with an underscore '_' or double underscore'__', but these are Python specific structures, so lets leave them to Python.

# The variable name may contain lowercase or uppercase letters, numbers, and the underscore, but as I said, not as the first Character.

# Also do not include spaces or any other special characters inside variable names -> this means no dollar signs, no commas, no parantheses, no question marks etc

# AND REMEMBER Python names are case-senstive, so, a variable named 'my_Var' is a different variable from 'my_var', with a lowercase 'v'
# Age ! =age !=AGE

# Another thing about a variable names is that you should keep a reasonable name length, so it will be easier for you to remember it and reference it inside your code

# The last thing I should mention on this topic is that there are some Python reserved names, which you cannot use as a variable name. example:def, while, for , if, list, str

# Lets see hoe we can assign a value to a variable 

#The rule is to use the equal sign '=' -> this should be regarded as an assignment operator, rather than the usual equal sign used in math.

#in the left side of the equal sign you type the variable name, and in the right side you type the value you want to assign to that variable.

# It doesnt matter if you leave a space between each side of the equal sign. Actually, I would advice you to leave a space on each side of the equal sign, for better readability of your code.
num1=7
num1 = 7

# You are also able to do multiple assignment, so you can assign a value to multiple variables, at the same time. The syntax for this would be:
a = b = c = x = y = 10
print(a)
print(b)
print(c)
print(x)
print(y)

# Also, you can assign a different value for each variable within the same line of code, like this:
a, b, c = 10, 20, 30 
print (a)
print(b)
print(c)

# Next -> Data types