# Python 3 - Strings

# Lets define a string first 

# A string is a sequence of characters, meaning -> letters, numbers, and other characters like the dollar sign, spaces and punctuation marks enclosed by single quotes, double quotes or even tripple quotes when spanning multiple lines 

# Lets define a string and assign it to a variable 
my_string = "this is my first string"
print (my_string)
mystring = 'this is my first string'
print(mystring)

# What do we need tripple quotes for? We need them whenever we want to enter a string on multiple lines -> for instance a comment in our code 
my_string = """This
is 
my
first
string"""
print (my_string)

# Indexing
# Python uses indexing to mark the position of an element within a sequence of elements -> a string is a sequence of elements and the elements of a string are the characters themselves. One character one element.

# The first element of any sequence, when counting from left to right, has the index 0, the second has the index 1, the third of the sequence is positioned at index 2 

# So when using indexes, remember to start counting from 0 

# When counting backwards, from right to left, the first index will be -1

# The last character in a string will have index -1, when looking from right to left. 

# Indexes are enclosed by square brackets, when we want to access some letter of a string

# lets see this in practice

string1 = "Cisco Router"

# Now, how to extract the first character of this string? By using an index, of course. And as stated, that would be at index 0. So, to access the element of string1, positioned on index 0 in the string, we should type the following:

# the name of the variable, string1, and then without inserting any spaces, the index number between the brackets, so, 

print(string1[0]) # returns C 

# Lets find the third character of the string1. What index should we use?
print(string1[2])
print(string1[5])

# Now for negative indexes,
# lets access the last character in the string -> will be -1
print(string1[-1]) # returns r (the last element)

# One more thing about indexes?
# What if we enter an invalid index for our string?

# Lets se what i mean by this 
# First, lets find out string1's length.
# We can count how many characters are in that string visually but what if we have a very very veeeery long string, maybe a newspaper page?
# Python has a solution for this and its called the len() function 

print(len(string1)) # returns the number of characters which is 12 

# Back to the first question, what happens if we enter an invalid index?

# print(string[20]) # returns IndexError : string index out of range






# Python 3 string methods
# We've talked about indexing and how we can determine the length of a sequence, in our case a string, using the len() function.

# Now lets see other operations
# 1. First, one more thing about indexes, you can find out the index of a character in a given string by using the index() method 
# Just remember that this method returns the first occurence of that particular character in the string 

a = "Cisco Switch"

# You can clearly see that letter 'i' appears 2 times in the string. So lets find out the index of the first occurrence of 'i' in the string

print(a.index("i")) # returns  1 

# Explanation (syntax)
# We have the name of the variable associated with the string 'a', then a dot. then the name of the method, 'index()', and then in between parantheses, we enter the character we want to find out the index for, which is 'i'

# 2. Another useful Python method is one that helps you find out how many times does a character appear in a string or generally speaking, an element inside a particular sequence. This method is called count()

# The syntax for count() is similar to the one for the index() 
# To use the count() method, just type in the name of the variable, then a dot, then the word 'count', then open and close parantheses and finally, the letter you want to count sorrounded by quotes.

print(a.count('c')) # returns 2

# 3. Another string method is find(). This method simply searches for a sequences of characters inside the string and if it finds a match, then it returns the index where the sequence begins.

print(a.find("sco")) # returns 2

# On the other hand if python does not find a match, then it will return the value -1. Lets see this and search for the substring "xyz"
print (a.find("xyz")) #returns -1 

# if a.find("x") = -1: 
#     print("the substring was not found in the string.")
# else:
#     print("Was found!")

# 4. We can also use some predefined Python methods to turn a string from uppercase to lowercase or vice-versa, if we want that 
# This can be accomplished by using the lower() and upper() methods
print (a) 

# to lower
print(a.lower())

# to upper
print (a.upper())

# Keep one thing in mind here! Although we just applied the lower() and upper() methods, the initial string is still the same. No changes have been applied.
# This is a great proof that strings are indeed immutable
print (a)

# 5. You can also verify that a string starts or ends wit h a particular character or substring.
# We have to methods for that, namely startswith() and endswith()
print(a.startswith("C")) # returns True 
print(a.endswith("h")) #returns True

# 6. Three important methods which you should keep in mind, because you will use them a lot when working with strings, are the strip(),split(), and join()

# 6.1 The strip method eliminates all white spaces from the start and the end of a string 

# lets say we have a new string, one with 3 spaces before "Cisco" and 4 spaces after "Switch"

b = "   Cisco Switch    "

# Lets apply the strip() method 
print(b.strip()) #returns a cleaned string
print(b) # returns the initial strip

# Now, consider that instead of the three spaces on each side of the string, we had 3 dollar signs $ that we want to remove 

c = "$$$Cisco Switch$$$$"

# We want to eliminate the leading and trailing dollar signs. For this we should specify the character we want to remove in between the strip()'s parantheses, so:
print(c)
print(c.strip("$"))

# what if we want all spaces removed fromthe string including those inside the string? Then, we have the replace() method instead of strip()

# Lets refer to the string referenced by variable b, which has spaces at the start and end of the string

# You can use the replace method to get a clean string
print(b.replace(" ", "")) 

# 6.2 split() method -> as its name implies, this method simply splits a string into substrings. Furthermore you can specify a delimiter for splitting the string. The result of this method is a list.

# Lets say we have a string referenced by a variable d like this 
d = "Cisco,Juniper,HP,Avaya,Nortel"

# The network device manufacturers in the string are delimited by commas. So, the comma will be regarded as our delimiter for the split. 

# What if we want to extract each provider from the string in a nice format 
# Well, in this case, the split() method saves the day 
# Lets type the following
print(d.split(","))

# Python returns a list where each provider in the string is an element of this list and can be further used into an application 

# 6.3 join() method used for dealing with string
# Lets remember string 'a' -> 'Cisco Switch' 

# What if we want to insert a character in between every two characters of the string? So we want to change this string a to "C_i_s_c_o__S_w_i_t_c_h"

# For this we will use the join() method the followng way and is a bit different from the syntax we've seen before

# First, you type in the character you want to use as a separator,enclosed with double quotes, Its upto you, so this character would be the underscore in our case. 

print("_".join(a))

# Python 3 Strings - Operators and formatting 

# What else can we do with strings?

# For instance, we can concatenate them. Concatenation means ubifying two or more strings into a single string.

# You can do this using the "+" operator, like you would when adding two numbers.

# So, lets try this 
# Lets set x with the value "Cisco"
x = "Cisco"

# and y with the value "Switch"
y = "Switch"

space = " "

z = x + space + y
# and finally, add them together 
print(x + y)

print (z)

# Another thing we can do is string repetition, by using the multiplication operator
print(x * 5)

# you can also verify if a character is in a string or not, using the "in" an "not in" operators
print("o" in x) # returns true
print("o" not in y) # returns true
print("S" in x) # returns false

# Now, what's the deal with string formatting 

# Lets say we have some kind of string template and we want to constantly modify only a few words inside the text but keep the overall template the same.
# To see what i mean, lets asuume we have the following string. Doesn't matter what it stands for, just focus on the string itself. 

my_string = "Cisco Model: 2600XM, 2 WAN Slots, IOS 12.4"

# We want to keep this string as a template and just change the model name, number of slots and IOS version a couple of times, while running our Python program. So, this would be a dynamic change each time 

# For this we should use the percent operator (%), followed by letter (s) for string, (d) for digit or (f) for floating-point number. Lets see the syntax

formatted_string = "Cisco Model: %s, %d WAN Slots, IOS %f" % ("2600XM", 2, 12.4)


# Now, lets translate this:
# the %s means that this is a place holder for a string we will specify in between parantheses, at the end of this line. 
# the %d operator follows the same logic, but for a number instead of a string and finally,
# the %f refers to a floating-point number, a number with a decimal point
# Now, moving on, the first value from within the parantheses is going to be associated with the first format operator in the string;
# The second value from within the parantheses is going to be associated with the second format operator in the string, and so on, for all the format operators you have in your string.
# Also do not forget to insert the % sign between the string and the parantheses containing the values.
# This operator maps the format operators inside the string with the values inside the parantheses. 
print(formatted_string)
formatted_string = "Cisco Model: %s, %d WAN Slots, IOS %f" % ("2691XM", 4, 12.3)
print(formatted_string)
formatted_string = "Cisco Model: %s, %d WAN Slots, IOS %f" % ("7200XR", 8, 15.4)
print(formatted_string)
formatted_string = "Cisco Model: %s, %d WAN Slots, IOS %f" % ("1841M", 1, 12.2) 
print(formatted_string)

# Something you might have noticed is the addition of several decimal places when dealing with floating-point numbers. In order to control this behaviour, you can easily choose the the number of decimal places you want to print out.
 
# Simply insert a dot and a value in between the percent operator and the letter f 
print( "Cisco Model: %s, %d WAN Slots, IOS %.2f" % ("2600XM", 2, 12.4))

# Instead of formatting operators like the ones we've just seen, we can use another notation, replacing %s,, %d or %f with a pair of curly brackets.
formatted_string = "Cisco Model: {}, {} WAN Slots, IOS {}".format("2600XM", 2, 12.4)
print (formatted_string)

# We can use some sort of indexing when dealing with this type of string formatting

# Lets assign a value for each of these pairs of curly braces
print( "Cisco Model: {1}, {0} WAN Slots, IOS {2}".format("2600XM", 2, 12.4))

# f-string formatting
first_name = "John"
user_age = 20 
print(f"My name is {first_name}, and i am {user_age} years old.")



# Python 3 String - Slices

# Slices allow us to extract various parts of a string (or a list or any other sequence of elements).

# The syntax for a string slice is the following:

# mystring[10:15]
# We have the name of the variable pointing to the string, followed by a pair of square brackets, in between the brackets, we have a colon, on the left side of the colon, we specify the index at which to start the slicing process. The slice will go upto, BUT NOT INCLUDE, the index specified on the right side of the colon. 

string1 = "0 E2 10.110.8.9 [160/5] Via 10.119.254, 0:01:00, Ethernet2"

# Lets extract the first IP Address in the string, 10.110.254

print(string1[5:15])

# Now, what if we dont specify the second index inside the brackets? Well, then the string slice would start at the index specified before the colon and would end at the end of the string. 
# this way we will get the rest of the string starting from the character at index 5 . Lets test this as well
print(string1[5:])

# What if we only use the second index, the one after the colon, but we dont specify the first index? Then, the slice would simply start at the beginning of the string and would go up to, BUT NOT INCLUDE, the character at the index we enter after the colon. Lets see this
print(string1[:15])

# What if we dont enter any indexes at all?
print(string1[:])

# What about negative indexes?
# Lets try extracting a couple of slices using negative value for our indexes. 

# What if we want to extract a slice containing the substring "Ethernet",this time using negative indexes?

# What if we want to obtain the last 5 characters of our string? How do we do that?

# What if we want to slice string1 starting at the beginning of the string and leave out the last 5 characters?

print(string1[-9:-1])
print(string1[-5:])
print(string1[:-5])

# One more thing about slices. 
# You can specify a third element within the square bracket, after the indexes, also separated by colon. This is called a step 
# variable_name[start_index:stop_index:step]

# For instance, if you would like to skip every second character of the string and obtain new string with these elements removed, you can write the following slice: 
print(string1[::2])

# The last thing i'll show you is how to print out the string in reverse order, using slices and indexes. For this, we will again use a slice and a step. 
# But, what would be the value of that step?
# Well, since we want to string in reverse order, we should start with the last character of the string, right? so, lets try it!
print(string1[::-1])

# On Tuesday -> Python 3 Numbers - Math operators