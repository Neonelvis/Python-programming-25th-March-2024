# Python 3 Loops - For Loops 

# For Loop 

# The for statement is used whenever you want to iterate over a sequene and execute a piece of code for all or some elements of that sequence - list or string, or whaterver you have. 

# Lets start with an example of iterating or looping over a sequence and, first, lets define a list 

vendors = ['Cisco', 'HP', 'Nortel', 'Avaya', 'Juniper'] 

# Now, lets see how we can work with a for - loop 

# First, you'll notice that there are some similarities to the if/elif/else syntax, meaning that the colon is again used to signal that an indented code follows the for statement, speaking about indenteation, we MUST  indent code inside a for-loop 

# Syntax 
# We start by typing in the for keyword, then we enter the iterating variable, which is a user-defined temporary variable, so you can name it however you like, then we type in the 'in' keyword, to tell Python that we are going to iterate over the sequence following the keyword and, finally, we enter the sequence itself, followed by a colon. 

for each_vendor in vendors: 
    print(each_vendor) 
    
# We can also iterate over a string 
my_string = "Cisco" 

for letter in my_string:
    print(letter) 
    print(letter * 2) 
    print(letter * 3) 
    
# Now, its time to see how to use a for-loop to iterate over a range. Remember the range data type, that can be used to generate an iterator over which we can iterate and the extract some values. 

# Lets consider a range starting with 0 and going upto, but not including, 10, with the default step of 1. That would return the integers 0 all the way to 9, in an ascending order. 

# Lets create this range 
my_range = range(10) 

# Now, lets use a for-loop to iterate over this range 
for i in my_range: 
    print(i) 
    
# Output -> 1 2 3 4 5 6 7 8 9 
# challenge -> output this -> 0 2 4 6 8 10 12 14 16 18 

for i in my_range: 
    print(i * 2) 
    
# Now, lets see a more common use of the range() function inside a for statement. What if we want to iterate over a list using list indexes? What do i mean by that? Okay, we still have the vendors list in memory. 

print(vendors) 

# Now, remember the len() function from earlier? Lets apply it to our list. 
print(len(vendors)) #returns 5 

# We know that range(5) return the integers starting with 0 upto but not including 5, right? Moreover, we can convert this range to a list, using list() function. Lets do this 
print(list(range(5))) # returns [0, 1, 2, 3, 4] 

# We can look at the elements of the list as being the indexes of each element of our list, vendors. So element 'cisco' would be positioned at index 0, 'HP' index 1 and so on 

# This means that if we want to get a list of indexes to iterate over, using the for-loop, we can use range (len(vendors)) 
print(range(len(vendors))) 

# For now, lets create a for-loop that prints out each element of the vendors list by its index 

# Challenge 
for element_index in range(len(vendors)): 
    print (vendors[element_index])
    
# Output: 
# Cisco
# HP
# Nortel
# Avaya
# Juniper  

# Next while loop 

# Python 3 - While Loop 

# The second type of Python loops is while. But, what is the difference between for and while loops. 

# Well, unlike a for loop, wguch executes a code a number of times, depending on the sequence it iterates over, a while loop executes a piece of code as long as a user-defined condition evaluates as true. If the specified condition does not change, meaning it doesn't become False, then the while loop will continue running forever and we end up with an infinite loop. 

# when the condition becomes False, Python continues to execute the code following the while loop, if any 

# Now, lets see an example of a while loop. 
# First we should create a variable, x, with the value 1. 

x = 1 

# Syntax for a while loop 
# To create a while loop, you have to type in the while keyword, followed by the condition you want to evaluate and then a colon. Below, after indentation you will specify the code to be executed as long as the condition evaluated as True. 

while x <= 10: 
    print(x) 
    x = x + 1 # x +=1 or x++

# Another way to work with while loops is by using an expression as True, in order to make Python do something over and over again, until you tell it to quit.

# A great example would be an interactive menu, where the user can select a value and execute a piece of code, then return to the main menu and so on 

# The way to do this is by simply using "while True:", which makes sure that the expression is always evaluated as True. 

# The syntax for this would be: 
# while True: 
    #  do something ... 

print("===" * 20)

# Output -> 0 2 4 6 8 
y = 0 
while y <= 8: 
    print(y)
    y = y + 2

print("===" * 20)

# Output -> 60 45 30 15 0 -15 -45 -60
z = 60 
while z >= -60: 
    print(z) 
    z -=15 

print("===" * 20)

# Often, you will see for loops within other loops - same thing with 'if' and 'while' statements. You will also need to use 'if' statements inside 'for' loops or 'while' loops, depending on what you are trying to achieve in your programs. 
# Next we are going to take a look at this kind of structures, which are called 'Nested Structures' 

# Next -> Nested Structure