point = int(input("Enter your score: "))
midterm = int(input("Enter your mid-term score: "))
finalterm = int(input("Enter your final score: "))
if point > 30 or midterm > 30 or finalterm > 40:
    print("error")
sum_score = point + midterm + finalterm
if sum_score >= 80:
    print("A")
elif sum_score >= 75:
    print("B+")
elif sum_score >= 70:
    print("B")
elif sum_score >= 65:
    print("C+")
elif sum_score >= 60:
    print("C")
elif sum_score >= 55:
    print("D+")
elif sum_score >= 50:
    print("D")
else:
    print("F")
