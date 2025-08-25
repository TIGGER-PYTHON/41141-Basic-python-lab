inputnumber = int(input(""))#input amout of input number
num = []#make a list
for i in range (inputnumber):#loop number in range
    number = int(input())
    num.append(number)#put the number in list
    total=sum(num)#sum the number in list
print(total)#print out total 
    