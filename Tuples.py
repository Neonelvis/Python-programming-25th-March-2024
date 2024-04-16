# Python 3 Tuples - Introduction 

# You can consider tuples as being immutable lists,meaning their contents cannot be changed by adding, removing or replacing elements 

# Ttuples may prove to be uselful when you eant to store some data in the form of a sequence and keep that data untouchable. 

# However, unlike sets, tuples are ordered collections of non-unique elements, meaning indexes and duplicates are allowed. 

# Lets start to practice and create our first tuple 

# Tuples are enclosed by parantheses (round brackets) and their elements are separated by commas

my_tuple = () 

# check type 
print(type(my_tuple)) # returns <class 'tuple'> 

# if you want to create a tuple with a single element, you have to use a trick, meaning that, although you have only one element inside the tuple, you have to write a comma after it, otherwise it will be regarded as a tuple 
my_tuple = (9) 
print(type(my_tuple)) # returns <class 'int>

my_tuple = (9,) 
print(type(my_tuple)) # returns <class 'tuple'> 

# Now you have a tuple set up. You should always remember this when creating tuples having only one element 

# Next, lets populate our tuple with more elements 
my_tuple = (1, 2, 3, 4, 5) 

# Just like strings and lists, tuples support indexing, so if you want to access an element within the tuple, the indexing rules that we've seen before are still applicable. 

# access the first element 
print(my_tuple[0]) 

# access the last element 
print(my_tuple[-1]) 
print(my_tuple[4]) 
 
# since tuples are immutable, you cannot modify an element of a tuple. 
# lets check this 
# my_tuple[0] = 10 # TypeError: 'tuple' object does not support item assignment 

# Also, removing elements is not permitted when working with tuples. 
# del my_tuple[0] # TypeError: 'tuple' object does not support item deletion 

# Another interesting thing you can do with tuples is tuple assignment. This means that you can assign a tuple of variables to a tuple of values and map each variable in the first tuple to the corresponding second tuple 

# lets see this, as well, 
# lets define tuple1 with the following elements 
tuple1 = ('Cisco', '2600', '12.4')

# And now, lets assign a tuple of variables to tuple1 
(vendor, model, ios) = tuple1 

# Finally, lets check if the assignment and variable-to-value mapping has been properly performed
print(vendor)
print(model)
print(ios) 

# This is also called tuple parking and unpacking and you can see it as a kind of mapping between elements of two different tuples.
 
#  An important thing to remember is that both tuples should have same number of elements. Otherwise, if you have different number of elements, a ValueError will be returned. 

tuple2 = (1, 2, 3, 4) 
# (x, y, z) = tuple2 # ValueError: too many values to unpack (expected 3)

# You can also assign in a tuple to a variable in another tuple within a single statement, which is even more convenient
(a, b, c) = (10, 20, 30)
print(a)
print(b)
print(c)

# Tomorrow -> Set Operations and Methods 

# Python 4 Sets - Methods 