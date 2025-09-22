n = int(input("Nhập một số nguyên lớn hơn 0: "))
total = 0.0
for i in range(1, n+1):
    total += i / (i + 1)
print(total)
