num = int(input(""))#input number
total = 0#make variable to collect sum
for i in range (1, num + 1):#loop from 1 to input number
    if i % 2 == 0:#check if number is even
        total += i #add even number to total
print(total)#print total of even numbers

