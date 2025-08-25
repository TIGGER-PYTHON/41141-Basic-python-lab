inputnumber = int(input(""))#input amout of input number
num = []#make a list
for i in range (inputnumber):#loop number in range
    number = int(input())
    num.append(number)#put the number in list
    more50low10 = []#make a list that number more than 50 and lower than 10
for n in num:
    if n <= 50 and n >= 10:#loop to find the number that more than 50 and lower than 10
        more50low10.append(n)#add number to list
print(f"ค่าที่อยู่ในช่วง10-50:{more50low10}")#print the number that more than or equal 50 and lower than or equal 10
    