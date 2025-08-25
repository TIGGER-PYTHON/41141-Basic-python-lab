def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b

while True:
    c = input("")
    if c=="4":
        print("จบโปรแกรม")
        break
    a = int(input(""))
    b = int(input(""))
    if c=="1": print("ผลลัพธ์: =",add(a,b))
    elif c=="2": print("ผลลัพธ์ =",sub(a,b))
    elif c=="3": print("ผลลัพธ์ =",mul(a,b))
