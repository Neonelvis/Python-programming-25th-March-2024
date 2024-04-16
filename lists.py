# Python 3 Lists - Introduction 

# So, what exactly is a list?
# A list is, actually, a sequence consisting, of elements separated by comma. 
# The sequence of elements is enclosed by square bracket. 
# You can have any data types as elements of a list - strings, numbers, tuples, or even other lists, and a list may have any number of elements

# Similarly to strings, which can be regarded as sequence of characters, lists are indexed, meaning each element has a certain position inside the list, starting at 0. 

# You can also use the len() function to see the number of elements in the list and slices to extract a portion of the list. 

# As opposed to string, lists are mutable, meaning that you can modify a list by adding, or removing elements. 

# Lets create our first list, we will name it list1 and will be initially empty 
# In order to have an empty list, you to type the square brackets and thats it, nothing else needed. 
list1 = [] 

# to check that this is indeed a list, lets use the old type() function on list1 
print(type(list1)) # returns <class 'list'> 

# Now, lets add some elements to our list1 
list1 = ['Cisco', 'Juniper', 'Avaya', 10, 10.5, -11]

# So, now we have a list with some strings and numbers as elements. good 

# Lets remember the len() function from strings section and use it on our list1 
print(len(list1)) # returns 6 

# Now, lets see how we can access elements inside the list 
# Well, the same as we did with characters inside a string,using indexes. So: 
# Access the first element 
print(list1[0])
# Access the third element 
print(list1[2])
# Access the last element from right to left 
print(list1[-1])
# Access the 2nd last element from right to left 
print(list1[-2])

# As with strings, if we enter an invalid index we will get an "IndexError" in return, stating that the list index is out of range.
# print(list[100])

# To check that lists are indeed mutable, lets try to replace an element in the list. 
# We still have list1 in memory, so, list1[2] will return 'Avaya' element, Now lets replace it with another vendor, say 'HP' 
print(list1) 

list1[2] = "HP"

print(list1) 

# Plain and simple, this is how you can update a list. Just type in the name of the variable and in between the square brackets, you have to insert the index at which you want the replacement to be made
# Finally, following the equal sign, just enter the new element and thats it, you're good to go. 


# Python 3 Lists - Methods 
# Now , its time to see how to handle lists and lists elements and what tools does Python provide for this. 

# We've already seem the len() function being used on a list. but, what if you want to find out the maximum and minimum value within a list? Well, you have the max() and min() functions for that. 

# consider list2 
list2 = [-11, 2, 12] 

# min value 
print(f"the minimum value in '{list2}' is {min(list2)}")

# max value
print(f"the maximum value in '{list2}' is {max(list2)}")

# What about a list of strings 
list3 = ['a', 'b', 'c']

# min element 
print(min(list3))

# max element 
print(max(list3)) 

# However, if we have a list with various types of elements, say numbers and strings mixed together, like list1, how does Python compare a string with an integer and return the maximum value in the list1? 

list1 = ['Cisco', 'Juniper', 'Avaya', 10, 10.5, -11]

# list1 = [1, 2, 3, 'a','b','c']

# print(min(list1)) #returns a TypeError: '<' not supported between instances of 'str' and 'int'

# Now, lets check the available methods we have at hand 

# Firstly, we should learn how to append a new element to a list 
# Its simple, we have the same list1

# To append an element to a list, just use the append () method, like this 
list1.append(100)

print(list1)

# Now, lets remove an element from our list. We have three options for this:

# 1. -> First, we can use the 'del' command 
del list1[4] # where 4 is the index of the element we want to remove 

print(list1)

# 2 -> Another way to remove an element by its index is using the pop() method like this 
list1.pop(0) # will remove the first element 
print(list1)

# 3 -> The third way actually removes am element by specifying the element itself, using the remove() method 
list1.remove('Avaya')
print(list1)

# Now, lets see how we can insert an element at a particular index in the list. This is accomplished by using the insert () method 
list1.insert(2, "Nortel")
print(list1)

# Another interesting list operation is appending a list to another list 
# lets say we have 
list2 = [9, 99, 999]

# To add the elements of list2 to list1, we can use the extend() method 
# lets see both lists first 
print(list1)
print(list2)

# Now, we can just extend list1 with the content of list2 like this 
list1.extend(list2)

print(list1)

# Now, remember the index() and count() methods from strings? Python makes them available for lists as well. so lets find the index of an element in our list and how to count the occusrrences of an element in the list

# consider list1 
print(list1)

# Index of -11 
print(list1.index(-11)) # returns 3

# lets append the value 10, thus having this value thrice in the list
list1.append(10)
list1.append(10)

print(list1)

# count the occurence of 10 -> 3 
print(list1.count(10)) # returns 3 

# Now, lets have a look at ways of sorting the elements of a list 

# 1 -> First, we can use the sort() functions 
# So, returning to list2, lets add a couple of elements first 
list2.append(1)
list2.append(25)
list2.append(500)

print(list2) 

# Now, lets say we want to have them sorted in ascending order. Simply apply the sort() method on list2 
list2.sort()

print(list2) 

# What if we want the elements sorted in reverse or descending order? Well, we have the reverse() method for this 
list2.reverse()
print(list2)

# The two methods you've just seen are modifying the list in place, meaning that after you apply the method there is no other list created - you have the same list2, only that the elements are displayed in a specific order

# To sort the elements of the list and create a new list in memory at the same time, you have sorted() function availale. Lets see this in action 
print(sorted(list2))
print(list2) 

# If you want to use the same function, sorted(), to reverse the order, just add an argument inside the parantheses. The argument is called reverse and it must have the value True assigned to it. 

print(sorted(list2, reverse=True))

# Two more things worth mentioning here. 
# You can concatenate or repeat a list, as you did with strings, using the plus and multiplication operators, so:

# concatenation 
print(list1 + list2)

# repetition 
print(list2 * 5)

# Tomorrow -> List Slices

# Remember, List slices allow us to extract various parts of a sequence. We already used them to slice strings and in many ways, all the rules applying to string slicing also apply to list slicing. 

# The general syntax is :

# Type the name of the variable pointing to that list, followed by square brackets, next, in between the brackets, we have a colon, on the left side of the colon, we can specify th eindex at which to start the slicing, then, the slice will go upto, BUT NOT INCLUDING the index specified on the right side of the colon. 

# Having said that, lets create a new list and do a couple of list slices 

list3 = [1, 2, 3, 'a', 'b', 'c']

# lets extract the first three elements of the list
print(list3[0:3])
# Another way to extract the first three elements of the list would be - not specifying the first index in between the brackets 
print(list3[:3])

# [3,'a','b']
print(list3[2:5])
# [3,'a','b','c']
print(list3[2:])
# [1, 2, 3, 'a', 'b', 'c']
print(list3[:])

# use -ve indexes
# [3, 'a', 'b',]
print(list3[-4:-1])
# ['a', 'b', 'c']
print(list3[-3:])
# [1, 2, 3,]
print(list3[-6:-3])
# [1, 3, 'b']
print(list3[::2])
# ['c', 'b', 'a', 3, 2, 1]
print(list3[::-1])