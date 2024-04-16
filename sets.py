# Python 3 Sets - Introduction 

# What is a set? You may ask yourself

# Well, a set is basically an unordered collection of unique elements

# Generally speaking, you may regard sets as being lists that have no duplicate elements. 

# Lets see the way to create a set. In fact, there are two ways 

# The first one is by using the set() function, which is a built-in function. 

# To also prove that sets do not allow duplicates, lets create a list with duplicate elements and apply the set() function on this list 

list4 = [1, 2, 3, 4, 5, 2, 3]

print(type(list4))

# convert the list to a set 
print(set(list4)) # returns {1, 2, 3, 4, 5} 

# So, you can see that the set() function removed the duplicate elements in list4. Which is a very useful feature to have at hand. 

# You can also dirctly create a set by passing a raw sequence to the set() function. like a string or list, and referencing the result using a variable. 

set1 = set([11,12, 13, 14, 15, 15, 15, 11]) 
print(set1)
print(type(set1))

# The second way to create a set is to use the curly braces. This method of creating a set is available in versions of Python starting with 2.7 according to www.python.org 

set2 = {11,12, 13, 14, 15, 15, 15, 11}

print(set2) 
print(type(set2))

# We can also find out the number of elements in a set, using the same len() function, as we did with strings and lists 
print(len(set2)) # returns 5 

# Now, checking whether an element is or is not a member of a set is also possible using the 'in' and 'not in' keywords 
print(11 not in set2) # return False
print(11 in set2) # return True 
print(16 not in set2) # returns True 

# We have to remember that sets are mutable, so we can add or remove elements from a set, in the following manner 

# Adding an element to a set -> add() method 
set2.add(16) 
print (set2)

# Removing an element from a set -> remove() method 
set2.remove(11) 
print(set2)

set2.add(16)
set2.add(16)
print(set2)

# Notice that if you try to add an element which already exists in the set, Python will not agree with you, although no error will be raised/returned. It just doesn't add it. 

# Now, lets see some operations and methods that can be applied on sets 


# Python 3 Sets - Methods
# To better understand set methods and operations, lets create two sets first 

set1 = {1, 2, 3, 4} 
set2 = {3, 5, 8} 

# Python defines some methods for identifying the similarities or differences between two sets of elements, but also other methods to better make use of this data type. Lets see them in action. 

# First, lets see how we can identify the common elements of the two sets defined. 
# To do this, we can use the intersection() method, like this 
print(set1.intersection(set2)) 
print(set2.intersection(set1))

# Now, lets see which elements does set1 have and set2 doesn't, by using the difference() method
print(set1.difference(set2))
print(set2.difference(set1))

# To unify the two sets, you can use the union() method and the result also being a set, a collection of unique elements, will include element 3 just once. So, do not confuse the union of sets with concatenation 
print(set1.union(set2)) 

# Another thing you can do is remove a random element in the set, is by using the pop() method 
print(set1.pop()) # returns the element removed from the set 
print(set1) 

# Finally, we can clear a set using the clear() method 
set1.clear()
print(set1) # a returns set() to indicate an empy set 
print(type({})) # returns an empty dictionary
print(type({1})) # returns an set 

# Next -> Python 3 Tuples - Introduction 