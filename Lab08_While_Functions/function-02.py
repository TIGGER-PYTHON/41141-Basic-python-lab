def factorial(n):
    new = 1
    sum = 0
    answer = 0
    while n >= 0 and n <= 20:
        answer = 1
        for i in range(1, n + 1):
            answer *= i
        print(f'{n}! = {answer}')
        sum += answer
        break
n = int(input("")) 
factorial(n)