# Python 3 Functions - Basics 

# Big, big topic ahead - functions. 

# This is a core topic in Python, and infact, in any other programming language. 
# You are going to use functions a lot to build your applications. 

# But, first of all, what is a function? 

# Well, you can use a function to organise your code in blocks that can be later reused. This is helpful if you want better readability of your code, modularity and also time saving when designing and running your code. 

# Before we start writing code, remember that functions follow the same syntax rules as other structures that we've seen so far, but also add some features that we're going to analyze very soon. 

# First, a function is defined using the 'def' keyword, followed by the name of the function, then a pair of parantheses and then a colon. After the colon, on the next row, you will type in the code you want to store in this function, indented one level to the right, as we did with 'if' or 'for' statements. 

# Lets see this 

def my_first_function(): 
    "This is our first function!"
    print("Hello Python!")

# So, as i said before, we have the def keyword, the name of the function, my_first_function, then the parantheses, and finally the colon. This is the way you define a function. 

# One important thing to remember here is that in between the parantheses you can specify one or several parameters for the function. We will see how to do that in a moment. 

# Until then, lets further study our function definition. 
# After the colon, which signals the start of an indented block, we type in the code we want this function to execute - indented, of course 

# Notice that on the first row inside the function I typed in a string. This is a docstring and its role is to describe the function. However, it is entirely optional - maybe you can use it when you define complex functions with complex applications, to remember the role of the function and how it is connected to other segments of your program. 

# You can access the docstring by using the help() command 
print(help(my_first_function))

# Now, I said earlier that functions are reusable blocks of code. Lets see why 

# After defining a function, with or without any parameters inside the parentheses, we can call that function whenever we need to run the code inside it 

# In order to call a function, you just need to type in that function's name, followed by the parentheses and thats it. Lets see this in action 

my_first_function()

# Another advantage of functions is that you can change the code within a function and see the results changing as well, the next time you call that function. 
# So we can say Functions are dynamic structures. 

# Lets redefine our functions and change the code inside it. then, on the next call, the result should reflect the update we've just made 
def my_first_function():
    print("Hello Java!") 

my_first_function()
my_first_function()
my_first_function()

# Okay, Now lets talk a bit about parameters and arguments and the difference between the two concepts. 

# Lets modify our existing function and insert our first parameter into the picture. Remember parameters are written inside the parantheses. 

# Lets see how they work 

def my_first_function(x): 
    print(x) 

# So, in this case, x is passed as a parameter to the function and then used inside the code within the function. This means that whenever we're going to call the function and pass an argument of our choice to the funciton, that argument will be further passed to the code inside the function 

# As a side note - one thing to keep in mind here is the terminology when using functions. 

# Parameters are the ones written inside parantheses when defining the function. 

# Arguments are the ones written inside parantheses when 'calling' the function. 

# Most of the time, they are used interchangeably, but you should try to follow and use this terminology, though. 

# For now, lets return to our function and call it by passing an argument to the function call 

my_first_function("Hello Everyone")

# So, what we did is we called our function and told Python to use the string inside the parentheses as an argument. Then, the string was passed to print() function and, finally, printed out on the screen. 

# You can also enter multiple parameter within a function definition, like this: 
def my_first_function(x, y): 
    print(f"Hello{x}")
    print(f"Hello{y}") 

# So, according to this piece of code, we expect that when calling the function and passing two strings as arguments inside our parantheses, they will both be printed out, preceeded by the "Hello" string. Lets see if I'm right 

my_first_function("Python", "Java") 

# Notice that x was mapped to "Python" and y was mapped to "Java", because that was the order we used when passing the arguments. Pretty intuitive, I think. 

# Now, we are going to touch on another topic that use the "return" statement. 

# This statement is used to exit a function and return something whenever the function is called. 

# Lets create a new d=function and see how the return statement works. Let me write this first. 

def add_two_numbers(x,y): 
    sum = x + y 

# So we have created a variable inside our function, that will reference the result of adding x and y, which are the function's parameters. Lets see if our function returns something when we call it 
add_two_numbers(3, 7) 

# So, nothing is returned. That's because we haven't specified what exactly we are looking to get back from the function. 

# The function in its current form does nothing more than creating a variable named sum and storing the result of adding 3 and 7. 

# However, it doesn't return anything. It keeps the result secret, for now. Thats why we need the return statement. 

# Lets see how to use it. 
def add_two_numbers(x, y): 
    sum = x + y 
    return sum 

print(add_two_numbers(3, 7)) 

result = add_two_numbers(23, 27) 
print(result)

# So this time we told Python to return the value stored by sum and we got the expected result in return. 

# We can change the function even more and call it by using another set of arguments. 

# Lets add another parameter, z, change the expression inside the function and then return the value of sum squared 

def add_two_numbers(x, y, z):
    sum = (x + y) * z 
    return sum ** 2 

print(add_two_numbers(1, 2, 3)) 

# The last thing I should add here is that if you just use the return statement, without specifying what exactly you want to get out of the function, Python will return 'None' value. So, 'return' without specifying what to return is, actually the same thing as return None. Lets test this 
def greet_user(name): 
    greeting = f"Hello, {name}" 
    return 
print(greet_user("Elvis")) 

# Challenge time 
# Create a Python program using 5 or 4 functions, that ask the user for their name and age. Then the program should output the user info in a nice format displaying the name, age, decades lived, and age in seconds that the use has lived. 

def user_name(name):
    "the name of the user"
    return name

username = print(user_name("Elvis"))


def age(years_lived):
    "age of the user" 
    return years_lived

age_of_user_in_years = print(age(18))

def age(decades_lived): 
    "decades the user has lived" 
    decades = decades_lived // 10 
    return decades 

age_of_user_in_decades = print(age(18))

def age(seconds_lived):
    "seconds the user has lived"
    seconds = seconds_lived * 365.25 * 24 * 60 * 60
    return seconds 

age_of_user_in_seconds = print(age(18)) 


print(f"Hello {username}, you have lived for {age_of_user_in_decades} decades, {age_of_user_in_seconds} seconds which means you are {age_of_user_in_years} years old")



def user_name():
    name = input("Please enter your name: ")
    return name 

def user_age():
    age = int(input("Please enter your age: "))
    return age

def user_age_in_decades(decades):
    return  decades // 10

def user_age_in_seconds(seconds):
    return seconds * 365.25 * 24 * 60 * 60 

def display_user_info():
    name = user_name()
    age = user_age() 
    decades = user_age_in_decades(age) 
    age_in_seconds = user_age_in_seconds(age)
    print(f"Hello {name}, you have lived for {decades} decades, {age_in_seconds} seconds, which means you are {age} years old. ")

# Call the display_user_info() here 
display_user_info() 