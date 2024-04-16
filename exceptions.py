# Python 3 - Exceptions 

# In Python, you may encounter two main types of errors -> syntax errors and exceptions

# A syntax error occurs when you dont follow Python's syntax and maybe you forget to add a colon, or the indentation is not proper. 

# Lets try this and skip the colon following a for statement, on purose.

# for i in range(10) 

# we get a SyntaxError as expected. This is an example of an error in Python. 

# Now, lets talk about exceptions 

# Unlike syntax errors, exceptions are raised during the execution of the program, interrupting the normal flow of the application. 

# lets see a couple of examples 

# First, lets use the same for loop to generate one of the many types of exceptions, called NameError 

# I will misspell the name of the range() function and wait for Python to notice my mistake
# for i in rnge(10): 
#     print(i) 

# NameError: name 'rnge' is not defined 
# What do we have here? A NameError. This means either that i misspelled a word in my code, in this case the name of a function , or the variable or function I'm trying to use is not yet defined in my namespace  

# Another type of exception is raised when trying to divide a number by 0. 
# Lets see this 

# print (4 / 0)

# ZeroDivisionError: division by zero
# Fair enough, we cannot divide a number by zero, so Python raises a special exception for that particular case 

# There are many types of exceptions in Python. We wont analyze all of them now, because you will most likely encounter most exception sas you start creating and troublehsooting your own real programs. 

# However you can find a comprehensive list of Python 3 exceptions in the link 
# https://docs.python.org/3/tutorial/errors.html  
# https://docs.python.org/3/library/exceptions.html 

# Next -> Python 3 Functions - Basics 