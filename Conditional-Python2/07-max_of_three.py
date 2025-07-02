number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))
if number1 >= number2 and number1 >= number3: # Check if number1 is greater than or equal to both number2 and number3
    print("Maximum is:", number1)
elif number2 >= number1 and number2 >= number3: # Check if number2 is greater than or equal to both number1 and number3
    print("Maximum is:", number2)
else:
    print("Maximum is:", number3)
# This code compares three numbers and prints the maximum of the three.