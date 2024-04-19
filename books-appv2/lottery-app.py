import random 

# Lottery Application (List/Set/Dictionary Comprehension) 

# Functions for implementing this app 
# 1. -> Getting the user lucky numbers 
# 2. -> Generating the winning numbers 
# 3. -> Displaying the menu to the user 

# Function to generate the winning numbers 
def create_lottery_numbers():
    # Create a list for the random lucky numbers 
    # values = []
    # for value in range(6):
    #     values.append(random.randint(1, 50))
    # return values 
    # create an empty set for the random lucky numbers
    values = set() 
    # loop as long as the lenth of the values is less than 6 
    while len(values) < 6: 
        # add a random number to the set 
        values.add(random.randint(1, 50)) 
    # return values set 
    return values 

# print(create_lottery_numbers())

# A function to get user numbers for the lottery draw 
def get_player_numbers():
    # prompt the user for six numbers 
    numbers_csv = input("Enter six numbers separated by commas(no spaces): ")
    # create a list ofnumbers from the numbers_csv 
    numbers_list = numbers_csv.split(',')
    # create an empty list to store the numbers
    numbers_set = set() 
    # use a for loop to add the numbers in the set
    for number in numbers_list:
        numbers_set.add(int(number))
    return numbers_set

# print(get_player_numbers())

# A function to display the menu to the player 
def lottery(): 
    # ask the user for the lucky numbers
    user_lucky_numbers = get_player_numbers()  
    # generate the lottery winning numbers 
    lottery_numbers = create_lottery_numbers()
    # print out the winning numbers 
    matched_numbers = user_lucky_numbers.intersection(lottery_numbers)
    # create the prize 
    prize = 100 ** len(matched_numbers)
    print(f"The winning numbers were: {lottery_numbers} ")
    print(f"You matched {matched_numbers} and wond Ksh {prize}") 
# call the 
lottery()