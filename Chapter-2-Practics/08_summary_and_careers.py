bill = float(input(""))
tip = int(input(""))
person = int(input(""))
tip_amount = bill * (tip / 100)
total = bill + tip_amount
per_person = total / person
print("each person pays:",per_person)
#calculate per person amount and it useful in restaurants