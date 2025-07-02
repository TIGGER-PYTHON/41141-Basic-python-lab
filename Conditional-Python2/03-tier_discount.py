buying = float(input("Enter the amount of your purchase: "))
if buying >= 2000:
    discount = 0.15 # 15% discount for purchases of 2000 or more
elif buying >= 1000:
    discount = 0.10 # 10% discount for purchases of 1000 to 1999.99
elif buying > 500:
    discount = 0.05 # 5% discount for purchases of 500 to 999.99
else:
    discount = 0.0
discount_amount = buying * discount # Calculate the discount amount
total = buying - discount_amount # Calculate the total after discount
print(f"Your total after discount is: {total:.2f}")
# This code calculates the discount based on the purchase amount.