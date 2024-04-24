# Objects and Classes 

# Apart from what we've seen until now, Python also has an object-oriented approach.

# Upto this point, we have seen one way of programming in Python, using functions 

# Object-Oriented programming is based on Classes, Objects and Methods. 

# In short, as a definition, a class is a data type containing its own variables, attributes and functions(which, by the way, in object-oriented programming are called methods) 

# A standard definition of a class would tell you that a class is like a blueprint/template for creating objects. 
 
# An object may be regarded as an instance of a defined class and the attribute values for a particular object define the state of the object. 

# An object is a real world entity. 

# Another term that is very much used when discussing classes is inheritance. 
# This means that a new class may inherit all the names and functionalities from an existing class. 
# We will talk more about inheritance later 

# In order to properly define a class, you will use the class keyword, then type in the class name. 

# Now, be careful here because the convention is to use camelcase for class names. This means each word in the name of the class will be capitalized and no spaces are allowed. 

# Actually, except the camelcase rule, all the rules regarding variables and function names appy to class names, as well. 

# So, lets name our class simply MyRouter 

# After the name of the class, in between the parantheses, you should type in the word "object", all lowercase. 

# This is the new style of defining classses, starting with Python 2.2 
# The thing you should keep in mind here is that if a class doesn't inherit from another class, then you should always type in the word object inside paranthesis, when defining a class. 

# This is a default setting and it means that this class inherits from a default class names object. 

# I know this may seem confusing, so, we won't get into any more details on this topic. 

# Just dont forget to add that word, object. 

# So, we have class MyRouter(object) then, as for any other block of code we've seen so far, we'll type in a colon. 

# class MyRouter(object):

# On the next row, using one elevel of indentation, of course, we shall input the content of the class. 

# As with functions, on the first row after the class definiton you can type in a documentation string or docstring, in between quotes, to provide a hint about that class' functionality. 

# So lets enter some text in betweem double quotes 

class MyRouter(object):
    "This is a class that describes the characteristics of a router" 


# Following the optional docstring, the first thing you define inside a class is the special __init__() method, also called a class constructor 

# the word init will be preceeded and followed by double underscores. This is the way Python identifies a special. 

# The role of __init__() is to initialize some variables and the method is called whenever you create a new instance of the class  in which it resides. 
# Actually it is the first code that is executed whenever you create a new instance of the class

# Any special method or regular method within a class is defined using the def keyword, as you would with regular functions. 

# The difference here is that each time you define a method inside a class, the first parameter inside the parantheses is itself 

# You have to remember to always input this word as the first parameter of every class method. 

# self is no more than just a reference to the current instance of the class.  

# Now, after typing in self, you define any other parameters that you want to be defined and initialized whenever you create a new instance of the class im which it resides. 

# In our case , we want to define some parameters that characterize our router, so we will add routername, model, serialno, ios. 

# Now, lets define the object or instance attributes we need to describe the router, according to the parameters of the __init__ method

# Remember that self is used to point out that we are referring to the current instance of the class 

# The next lines of code will again be indented under the definition of the __init__ method 

# That how you define object attributes 

# Now, lets also define a new method inside the class, that will do nothing more than just print out the attributes and concatenate the model of the router with the manufacturing date  

# The definition of this new method will sit at the same level of indentation as the definition of the __init__ method. 

# Notice that self is again inserted as the first parameter. 

# Yours should do this every time you define a method inside a class. 

# Next, inside the method again indenting our code one level to the right, we enter the print() functions we need 

# Now, lets see what's the deal with the objects we talked about. 

# An object is actually an instance of the a/the class 

# You can create as many objects as you want, by simply calling the class name and entering the arguments required by the  __init__ method, in betwween parantheses - all of them, except self, which is automatically passed by Python 

class MyRouter(object): 
    "This is a class that describes the characteristics of a router " 
    def __init__(self, routername, model, serialno, ios): 
        self.routername = routername
        self.model = model 
        self.serialno = serialno 
        self.ios = ios 

# A method to print the rouer properties 
def print_router(self, manuf_date):
    print("The router is: ", self.routername)
    print("The router model is: ", self.model)
    print("The serial number is: ", self.serialno)
    print("The ios version: ", self.ios)
    print("The model and date combines is: " , self.model + manuf_date)




# Now lets create our first object 
router1 = MyRouter('R1', '2600', '123456789', '12.4') 

# print(router1) 

# Indeed we see that we created an object. Python confirms it. 

# Now, what can we do with this object? 

# First you can access each of its attributed, lets see how 
print(router1.routername)
print(router1.model)
print(router1.serialno)
print(router1.ios)

router1.print_router('23-04-24')
