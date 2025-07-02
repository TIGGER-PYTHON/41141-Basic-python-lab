year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): 
    print("Leap Year") # Check if the year is divisible by 4 and not divisible by 100, or divisible by 400
else:
    print("Not a Leap Year") 
# This code checks if a year is a leap year or not