# Python 3 Booleans - Logical Operators

# As a short definition, we can say that boolean defines only two values -> True and False. (1 - True , 0 - False)

# The name boolean comes from George Boole. He was a 19th century English Mathematician philosopher. 

# Leaving the history aside and returning to Python, you can think of these two values as being equivalent to 1 and 0 

# In Python,true is written with a capital letter T and False with a capital F, keep that in mind. 

# We've already seen True and False in some examples during the lectures, so they are not completely new to you at this point in the course. 

# Basically, they are used to evaluate whether an expression is true or false and can be further used in conditional or loop structures, as we will see that later in the course. 

# For now, lets evaluate some basic expressions and see how Python evaluates each of them 

print (1 == 1) # returns True

print (1 == 2) # returns false

print ("python" != "Python") # return True 

print (3 <= 4 ) #return True 

# Ok. you got the idea. These were some pretty basic evaluations we have done. 

# Now, there are three main boolean operations, each of them having a specific operator namely "and", "or", and "not"

# 1 -> "and" means both the operands should be true, in order to have the entire expression evaluated as true 

print((1 == 1) and (2 == 2)) # returns True 

print((1 == 1) and (2 == 3)) # returns False 

# The conclusion here is that, when using AND operator, if both expressions are True, then the result will also be true. On the other hand, if at least one expressionus evaluated as false, then the result will be false, as well. 

# 2 -> OR works like this -> If at least one of the expressions evaluates to True, then the final result is True. If they are both False, then the final result will be false, as well. 
# So, when using OR, it is enough if only one expression is True, in orfer to have true as the final result. 
print((1 == 1) or (2 == 2)) # returns True 
print((1 == 1) or (2 != 3)) # returns True 
print(((1 == 1) or (2 != 2)) and ("jave" == "java")) # returns 

# 3 -> Finally, using NOT means simply denying an expression. If that expression is True, the denying it will to false, and vice-versa
# lets verify this 
print(not(1 == 1)) # returns false
print(not(1 == 2)) # returns True 

# One more thing to keep in mind here: Some Python values always evaluate to False. They are:-
# None
# 0
# 0.0
# empty string ""
# empty list []
# empty set set ()
# empty tuple ()
# empty dictionary {}

# Python provides the bool() function to help us evaluate values and expressions ad True or false. So, lets use this function to check the always false function 
print(bool(None)) # returns false 
print(bool(0)) # returns false 
print(bool(0)) # returns false 
print(bool("")) # returns false 

# All other values in Python are considered to be true 
print(bool(0.1)) # returns True 
print(bool(" ")) # returns True

# Real World Example -> Login System ... 

# User credential in the DB Database 
user_name_in_db = "Elvis"
password_in_db = "P@$$w0rd"

# user credentials provided dueing a Login Attempt
user_name = "Elvis"
password = "P@$$w0rd"

# check if the user credentials are correct
if (user_name == user_name_in_db) and (password == password_in_db):
    print("Login Succssful!!!")
else:
    print("Wrong username or Password, Please try again!!!")
    


# Next ->Lists