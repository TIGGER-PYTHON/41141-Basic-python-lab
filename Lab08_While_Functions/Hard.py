import random

secret = random.randint(1, 20)
count = 0

while True:
    guess = int(input(""))
    count += 1
    if guess < secret:
        print("น้อยไป")
    elif guess > secret:
        print("มากไป")
    else:
        print(f"ถูกต้อง! คุณทายทั้งหมด {count} ครั้ง")
        break
