Celcius = int(input("Enter temperature in Celcius: "))
if Celcius <= 0:
    print("Freezing")
elif Celcius <= 15:
    print("Cold")
elif Celcius <= 30:
    print("Warm")
else:
    print("Hot")
