st = input("Nhập vào chuỗi của bạn: ")
st_search = input("Nhập chuỗi cần tìm: ")

if st_search in st:
    print("Chuỗi cần tìm đã được tìm thấy, tại vị trí: " + str(st.find(st_search)))
else:
    print("Không tìm thấy")
