num = int(input("Nhập một số: "))
level = int(input("Nhập bậc: "))
tong = 0
temp = num

while temp > 0:
    digit = temp % 10
    tong += digit ** level
    temp //= 10

if num == tong:
    print(num, "là số Armstrong, bậc:", level)
else:
    print(num, "không phải là số Armstrong")
