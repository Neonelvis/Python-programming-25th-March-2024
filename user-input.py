# Python3 - user input

#  ctrl + /   (shortcvut for inserting a comment)

# Throughtout the course, you're going to learn how to insert some input into a Python program.

# Actually, you are going to use a specific function, in order to ask the user for some input, store the information he/she is entering at the prompt then use that information further into the program

# This is especially useful when you need to build an interactive application, usually having some sort of menu that the user needs to interactg with

# Examples of such menus are "Please enter you username: " or "Choose an option from the following list: " and so on...

# The function we are talking about is called input ()

# Lets prompt the user to enter a string that he/she wants to be printed out on the screen

# Let me write the code and the anylyze it inch by inch

user_says = input("Please enter the string you wish to print: ")

# Looking at the above line of code, you may ask yourself : what is this "user_says" thing?

# Well, thats a python variable and dont worry, we will talk more about variables very soon For now, just keep in mind that by using a variable, you can store or save the value entered by the user, for later use.

# The so called storing or saving of the user's input is accomplished using the equal sign "=", which is called an assignment operator.

# Following the equal sign, we have the input () function.
# Next, inside input()'s pair of parantheses, you have to type in a description, a phrase, which is actually a string asking the user for input. This is completely upto you with an appropriate sentence.

# A good practice here is to also enter a colon and a space after the text, so when the user inputs some data, it will be clearly separated from the sentence you wrote -> just to make everything pretty and easy to read.

#Finally, do not forget to close everyting you wirte in between parantheses, also using either double or single quotes.

#Last but not least, in order to have out text printed out on the screen and visible to the user, we should use the prihnt() function in Python, to print otu the content of the user_says variable.

print(user_says)

#Shortcut for opening terminal -> ctrl + J

# Next - Variables