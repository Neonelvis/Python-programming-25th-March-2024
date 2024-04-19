# Python 3 - Working with files

# We use the open() function when working with files. 

# The open() function takes in two arguments -> 
# 1. name of the file you are openning 
# 2. mode at which you are openning the file with

# syntax 
# open (file_name, mode) 

# We have several modes 
# 1. read -> 'r' : open a file for reading data, and raises an error if the file doesn't exist 
# 2. append -> 'a' : opens a file to append to it, creates file if it doesnt exist 
# 3. write -> 'w' : open  afile to write to it, overwrites existing data, creates the file if it does not exist 
# 4. create -> 'x' : creates a new file 

# Reading data from a file 

# Lets create a new file 
# fruits_file = open('fruits.txt', 'x')

# reading from a file 
# my_file = open('fruits.txt', 'r') 

# file_contents = my_file.read()

# my_file.close() 

# print(file_contents)

# appending to a file 
# student = 'Elvis'

# my_file = open('students.txt', 'a') 

# my_file.write(student + "\n") 

# my_file.close() 

# writing to a file 
# new_student = 'Dennis'

# my_file = open('students.txt', 'w') 

# my_file.write(new_student)

# my_file.close() 

# context managers -> with 

# read fruits
with open('fruits.txt', 'r') as f: 
    file_content = f.read() 
    print(file_content) 

# Challenge Time 

# 1. Write a Python script which queries the user for input (infinite loop with exit possibility) and writes the input to a file. 

# solution 
# is_running = True 

# while is_running:
#     print("Please choose from the menu")
#     print("1. Add Your Input")
#     print("q. Quit")

#     # get user input 
#     user_input = input("Enter your choice: ")
#     # check for  user input 
#     if user_input == '1':
#         data_to_store = input("Please provide your input data: ")

#         with open('sample.txt', 'a') as file: 
#             file.write(data_to_store + '\n') 
#     elif user_input == 'q':
#         is_running == False 


# 2. Add another option to your user interface (UI): The user should be abke to output the data stored in the file in the terminal 
is_running = True 

while is_running:
    print("Please choose from the menu")
    print("1. Add Your Input")
    print("2. Output data")
    print("q. Quit")

    # get user input 
    user_input = input("Enter your choice: ")
    # check for  user input 
    if user_input == '1':
        data_to_store = input("Please provide your input data: ")

        with open('sample.txt', 'a') as file: 
            file.write(data_to_store + '\n') 
    elif user_input == '2':
        with open('sample.txt', 'r') as file:
            contents = file.read()
            print(contents)
    elif user_input == 'q':
        is_running == False 


# 3. Store user input in a list (instead of directly adding it to a file) and write that list to the file. -> using JSON and pickle 

