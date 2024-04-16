# Python 3 - Break, Continue, and Pass 

# The break and continue statements are used to handle the flow of a while or for loop in a Python program, meaning the programmer can interrupt or restart the execution of a loop structure, in certain conditions.

# Lets start with the break statement, which is used to terminate the loop in which it resides. 

for number in range(10): 
    if number == 7: 
        break 
    print(number) 

# Now, what if we have a for loop nested inside another for loop? 
list1 = [4, 5, 6] 
list2 = [10, 20, 30] 

for i in list1: 
    for j in list2:
        if j == 20:
            break 
        print(i * j) 
    print("Outside the nested loop") 

# Now, lets have a look at the continue 

# When Python stumbles upon a continue statement inside a for or while loop, it ignores the rest of the code below, for the current iteration, goes upto the top of the loop and immediately starts the next iteration. 

# In order to see this in practice, lets consider the same lists for for loops as earlier, but replace break with continue

list1 = [4, 5, 6] 
list2 = [10, 20, 30] 

for i in list1: 
    for j in list2:
        if j == 20:
            continue 
        print(i * j) 
    print("Outside the nested loop") 

# Finally, lets talk about the pass statement 

# pass is equivalent of "do nothing". It is actually a placeholder, for whenever you want to leave the addition of a piece of code for later and move on to write other segments of your program. 

# Lets see a short example of this 
for i in range(10):
    pass

print("Hello Everyone!") 
