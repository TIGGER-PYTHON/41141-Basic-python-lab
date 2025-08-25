inputnumber = int(input(""))#input amout of input number
num = []#make a list
for i in range (inputnumber):
    number = int(input())
    num.append(number)#put the number in list 
print(num)

num.sort()#sort the number from low to high

print(num)#print the number from low to high in list