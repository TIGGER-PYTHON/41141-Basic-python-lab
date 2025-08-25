inputnumber = int(input(" "))#input amout of input number
num = []#make a list
for i in range (inputnumber):#loop number in range
    number = int(input())
    num.append(number)#put the number in list
    more50 =[]#make a list that number more than 50
for n in num:#loop to find the number that more than 50
    if n >50:
        more50.append(n)#add number to list

print(f"จำนวนที่มากกว่า 50:",len(more50))#print amount number in list
    