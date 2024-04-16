import math 

# Scientific Calculator 

# Display the menu to the user for them to enter their choice 

while True:

    print("\n\t\t\t\tCPL Scientific Calculator")

    print("\nChoose an Operation From the Menu\n\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulus\n6. Power of a Number\n7. Square Root of a Number\n8. Logarithm\n9. Sine\n10, Cosine\n11. Tangent\n")

    # ask the user for their choice 
    operation = int(input("Enter Your Choice: "))

    # check the user choice and perform the operation that maps to that choice 
    # 1. Addition 
    if operation == 1: 
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The sum of {num1} and {num2} is {num1 + num2}") 

        # Ask the user to go back to the main menu  
        back = input("Go back to the main menu? (Y/N): ") 
        
        if back == "Y":
            continue
        else:
            break 
    
    # 2. Subtraction 
    elif operation == 2:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The difference between {num1} and {num2} is {num1 - num2}") 

        back = input("Return to the main menu? (Y/N): ") 
        
        if back == "Y":
            continue
        else:
            break 
    
    # 3. Multiplication 
    elif operation == 3:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The product of {num1} and {num2} is {num1 * num2}") 
        
        back = input("Return to the main menu? (Y/N): ")

        if back == "Y":
            continue
        else: 
            break 

    # 4. Division 
    elif operation == 4:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The quotient of {num1} and {num2} is {num1 / num2}") 
        
        back = input("Return to the main menu? (Y/N): ")

        if back == "Y":
            continue
        else: 
            break 
    
    # 5. Modulus 
    elif operation == 5:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The modulus of {num1} and {num2} is {num1 % num2}") 
        
        back = input("Return to the main menu? (Y/N): ")

        if back == "Y":
            continue
        else: 
            break 
    
    # 6. Power of a Number
    elif operation == 6: 
        base = float(input("Enter the first number: "))
        power = float(input("Enter the exponent: "))
        print(f"{num1} to the power of {num2} is {pow(base, power)}") 
        
        back = input("Return to the main menu? (Y/N): ")

        if back == "Y":
            continue
        else: 
            break 

    # 7. Square root of a Number 
    elif operation == 7:
        number = float(input("Enter the number you wish to find its square root: "))
        print(f"the square root of {number} is {math.sqrt(number)}")

        back = input("Return to the main menu? (Y/N): ")

        if back == "Y":
            continue
        else: 
            break 
    
    # 8. Logarithm 
    elif operation == 8: 
        number = float(input("Enter the number: "))
        print(f"the logarithm of {number} is {math.log(number, 2)}")
        
        back = input("Return to the main menu? (Y/N): ")

        if back == "Y":
            continue
        else: 
            break 
    
    # 9. Sine
    elif operation == 9: 
        number = float(input("Enter the angle in degrees you wish to find its sine: "))
        number_in_rad = math.radians(number)
        print(f"the sine of {number}\u00b0 is {math.sin(number_in_rad)}")

        back = input("Return to the main menu? (Y/N): ")

        if back == "Y":
            continue
        else: 
            break 
    
    # 10. Cosine
    elif operation == 10: 
        number = float(input("Enter the angle in degrees you wish to find its cosine: "))
        print(f"the cosine of {number}\u00b0 is {math.cos(math.radians(number))}")

        back = input("Return to the main menu? (Y/N): ")

        if back == "Y":
            continue
        else: 
            break 
     
    # 11. Tangent 
    elif operation == 11:
        number = float(input("Enter the angle in degrees you wish to find its tangent: "))
        print(f"the tangent of {number}\u00b0 is {math.tan(math.radians(number))}")

        back = input("Return to the main menu? (Y/N): ")

        if back == "Y":
            continue
        else: 
            break 



