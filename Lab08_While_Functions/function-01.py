def show_table (n,limit):
    number = 1
    while number <= limit:
        print(f'{n} x {number} =',n*number)
        number += 1
        
n = int(input(""))
limit = int(input(""))
show_table(n,limit)