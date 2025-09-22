st = input("Nhập một câu: ")
so_chu_hoa = 0
so_chu_thuong = 0

for c in st:
    if c.isupper():
        so_chu_hoa += 1
    elif c.islower():
        so_chu_thuong += 1
    else:
        pass      

print("Số ký tự in hoa:", so_chu_hoa)
print("Số ký tự in thường:", so_chu_thuong)
