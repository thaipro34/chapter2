total = 0
count = 0

while True:
    inp = input("Nhập một số (gõ 'done' để kết thúc): ")
    if inp == "done":
        break
    value = float(inp)
    total = total + value
    count = count + 1

if count > 0:
    average = total / count
    print("Giá trị trung bình là:", average)
else:
    print("Không có số nào được nhập!")
