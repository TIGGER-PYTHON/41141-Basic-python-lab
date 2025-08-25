max_val = None
min_val = None

while True:
    n = input()
    if n.lower() == "end":
        break
    num = float(n)
    if max_val is None or num > max_val:
        max_val = num
    if min_val is None or num < min_val:
        min_val = num

if max_val is None:
    print("ไม่มีข้อมูล")
else:
    print("ค่าสูงสุด:", int(max_val))
    print("ค่าต่ำสุด:", int(min_val))
