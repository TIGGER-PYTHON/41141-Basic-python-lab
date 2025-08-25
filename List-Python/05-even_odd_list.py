inputnumber = int(input(" "))#input amout of input number
num = []#make a list
for i in range (inputnumber):#loop number in range
    number = int(input())
    num.append(number)#put the number in list
    even = []#make a even list
    odd = []#make a odd list

for n in num:#loop to find even or odd in list
    if n%2 ==0:
        even.append(n)#input even number
    else:
        odd.append(n)#input odd number  
print(f"เลขคู่:{even}")#print odd number in list
print(f"เลขคี่:{odd}")#print even number in list
    