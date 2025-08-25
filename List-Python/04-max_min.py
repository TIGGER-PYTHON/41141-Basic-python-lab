inputnumber = int(input(""))#input amout of input number
num = []#make a list
for i in range (inputnumber):#loop number in range
    number = int(input())
    num.append(number)#put the number in list
    maximum = max(num)#find max number in list
    minimum = min(num)#find min number in list
print(f"มากที่สุด:{maximum}")#print max number in list
print(f"น้อยที่สุด:{minimum}")#print min number in list
    