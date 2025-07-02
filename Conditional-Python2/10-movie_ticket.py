age = int(input("Enter your age: "))
day = int(input("Enter the day of the week (1-7): "))
if age >= 60: # Check if the age is 60 or older
    ticket_price = 120
elif age >= 13 and age < 60: # Check if the age is between 13 and 59
    ticket_price = 180
else:
    ticket_price = 100
if day == 6 or day == 7: # Check if the day is Saturday (6) or Sunday (7)
    ticket_price += 50
print(f"Your ticket price is: {ticket_price} baht")
# This code calculates the movie ticket price based on age and day of the week.