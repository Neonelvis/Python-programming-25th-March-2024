# Python 3 Dictionaries - Introduction

# Okay, lets study another very important data type, that you'll need for your Python adventure, Dictionaries

# A dictionary is an unordered set of 'key-value' pairs, separated by comma and enclosed by curly braces. 

# They are very useful for storing information in a specific format. For instance, considering a router, we can store data about the device in the following format:
# 'vendor': 'cisco', 'model': '2600', 'ios': '12.4', 'ports': 4 

# Dictionaries are mutable, which means we can modify their contents using dictionary specific procedures. Why do I say dictionary-specific? Because, unlike strings or lists, dictionaries are not indexed by the position of each element, like we previously had 0 for the first element, 1 for the next and so on... 

# Dictionaries are indexed by key. The key is the value on the left side of the colon of each key-value pair. We will see this in practice, dont worry 

# For now, lets create an empty dictionary 

dict1 = {}

print(dict1) # returns {} -> empty dictionary 

# Check the type of dict1 
print(type(dict1)) # returns <class 'dict'> 

# This is how you create an empty dictionary 

dict1 = {'vendor': 'cisco', 'model': '2600', 'ios': '12.4', 'ports': 4} 

# Lets notice a few things here: 

# First, because the keys in the dictionary are actually strings, each key is enclosed by quotes. This may be those most widely spread data type used for a dictionary. You may also use a number as a key, in order to have some kind of numbering system, like this: 

d1 = {1: 'First Element', 2: 'Second Element', 3: 'Third Element'} 

# Okay, lets get back to our dict1 dictionary 

# A key thing to remember here is that each key in the dictionary must be unique and should be of an immutable type -> this means strings, numbers or tuple as keys but not lists 

# On the other hand, values don't have to be unique, and can be either of a mutable or immutable data type. 


# Python 3 Dictionaries - Methods 

# lets consider dict1 

# First, lets extract the corresponding value for a specified key. This can be done similarly to accessing elements inside a list, only that we dont specify an index, we specify the associated key for the valuewe want to extract. 

print(dict1) 

# output 12.4 

print(dict1['ios']) 
print(dict1.get('ios'))

# Remember, we said that dictionaries are mutable. 
# So, lets try to add a new key-value pair to our dictionary. This is done by simply assigning a new value to the new key. 
dict1['RAM'] = '128'
print(dict1)

# Change IOS to 15.8 
dict1['ios'] = '15.8' 
print(dict1)

# We can also delete a pair from the dictionary using del command -> delete key 'ports' 
del dict1['ports']
print(dict1) 

# Next, remember the len() function from strings, lists and tuples? we can use it here, as well, to fin dout the number of key-value pairs inside a dictionary 
print(len(dict1)) # returns 4 

# You can verify if a certain string is a key in our dictionary or not, like 
print('IOS' in dict1) # returns False 
print("IOS" not in dict1) # returns True 

# Now, there are three important Python methods to deal with keys and values, in a dictionary 

# 1 -> The first method is keys(). This method is used to obtain a list having the keys in a dictionary as elemenents. 
print(list(dict1.keys()))

# 2 -> The second is called values(), this method is used to obtain a list having the values in a dictionary as elements 
print(list(dict1.values())) 

# 3 -> The third is item(), returns a list of tuples, each tuple containing the key and value of each dictionary pair. Lets check this out 
print(list(dict1.items()))

# Challenge time 

# 1. Create a list of "person" dictionaries with a name, age and a list of hobbies for each person. Fill in any data you want 

person = [
    {'Name': 'Fred', 'Age': 17, 'Hobbies': ['Swimming', 'Cycling']}, 
    {'Name': 'George', 'Age': 19, 'Hobbies': ['Dancing', 'Hiking']}, 
    {'Name': 'William', 'Age': 22, 'Hobbies': ['Fishing', 'Reading']}, 
    {'Name': 'Alex', 'Age': 19, 'Hobbies': ['Reading', 'Basketball']}]
print(person)
print(f"{person[0]['Name']} likes {person[0]['Hobbies'][0]}.")
print(f"{person[3]['Name']} likes {person[3]['Hobbies'][1]} and {person[3]['Hobbies'][0]} and is {person[3]['Age']} years old.")


# 2. a. Create a Python dictionary with keys a, b and c having lists as values of the keys, 1-10, 11-20 and 21-20 respectively. 
dictionary = {'a': list(range(1, 11)), 'b': list(range(11, 21)), 'c': list(range(21, 31))}
print(dictionary)

# 2. b. Then from the above dictionary access element 13 and output it
print(dictionary['b'][2]) 

# Create a Python script that captures the names and a list of marks of students and then stores that information to a dictionary. The program then outputs the average score of the student. 

# Marks = {
#     'Name': input("What is your name? "),
#     'Marks': [int(input("Maths? ")), int(input("English? ")), int(input("Kiswahili? ")), int(input("Physics? ")), int(input("Geography? "))]
# }
# print(((Marks['Marks'][0]) + (Marks['Marks'][1]) + (Marks['Marks'][2]) + (Marks['Marks'][3]) + (Marks['Marks'][4])) / 5)

student_name = input("Enter Student Name: ")

maths = int(input("Enter your score for Maths: "))
english = int(input("Enter your score for English: "))
kiswahili = int(input("Enter your score for Kiswahili: "))
physics = int(input("Enter your score for Physics: "))
geography = int(input("Enter your score for Geography: "))

# Store them in a variable 
students = {
    'name': student_name,
    'math': maths,
    'english': english,
    'kiswahili': kiswahili,
    'physics': physics,
    'geography': geography
}

# compute the average score
# average = (students['math'] + students['english'] + students['kiswahili'] + students['physics'] + students['geography']) / 5
# scores = []
# scores.append(maths)
# scores.append(english)
# scores.append(kiswahili)
# scores.append(physics)
# scores.append(geography)
# average = sum(scores) / len(scores)
 
#  output the average score 
# print(students) 
# print(average)

# average = [students['math'], students['english'], students['kiswahili'], students['physics'], students['geography']]
scores = list(students.values()) # ['Elvis', 89, 90, 92, 67, 67]

scores_without_name = scores[1:] #[89, 90, 92, 67, 67]

score_average = sum(scores_without_name) / len(scores_without_name)
print(score_average)


# for later in the course
students_info = [
    {
        'name': student_name,
        'marks': []
    }
]