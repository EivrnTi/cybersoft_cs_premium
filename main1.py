# TODO: ÔN TẬP CÚ PHÁP PYTHON

''' 
Quy tắc đặt biến:
1. Đặt tiếng việt hết hoặc tiếng anh
2. Đặt tên theo kiểu snake_case
''' 

# Lệnh xuất
# print(2)
# print("Abc")
# print(ho_ten)

#? Cách để tạo ghi chú nhanh: Ctrl (Cmd) + /

''' 
Kiểu dữ liệu: 
1. str (string): chuỗi - bao gồm tất cả các kí tự được quy định trong bảng ASCII / Unicode
2. int (integer): số nguyên 
3. float: số thực / số hữu tỉ 
4. bool (boolean): giá trị dùng để so sánh (True, False) = (1, 0)
'''



# print("Bạn này có trên 18 không:", is_older_than_18)

#? Hàm (function)
'''
Các loại hàm:
1. Hàm không trả về giá trị (void)
2. Hàm trả về giá trị
'''

def in_ho_ten():
    ho_ten = "Duy"
    print(ho_ten)

# Tham số (argument): những cái giá trị mình truyền vào hàm
def kiem_tra_tuoi(num):
    is_older_than_18 = False
    
    if num > 18:
        is_older_than_18 = True
    else:
        is_older_than_18 = False
        
    return is_older_than_18

# Lệnh nhập => luôn trả về kiểu dữ liệu string
# tuoi = int(input("Nhập vào tuổi của bạn: ")) # "20" -> 20
# print("Bạn có trên 18 tuổi không:", kiem_tra_tuoi(tuoi))

#? Scope: phạm vi của biến
'''
Các loại scope:
1. Local (Function) scope: những biến chỉ tồn tại trong phạm vi hàm, vòng lặp
2. Global scope: biến này được sử dụng cho tất cả mọi nơi
'''

# x = 10

# def change_x(x):
#     x = 20
#     print("x:", x)

#? Vòng lặp
'''
Các loại vòng lặp:
1. Vòng lặp for
2. Vòng lặp while
'''

# Đặt 1 biến tạm -> biến này dùng để xác định dừng vòng lặp

#* range(a, b): a sẽ là giá trị bắt đầu, b - 1 là giá trị kết thúc
#* range(a, b, c): a với b giống ở trên, c là step (khoảng cách giữa các giá trị giữa vòng lặp) 
# for i in range(1, 11, 2):
#     print(i)
    
'''
Điều kiện while: 
1. trả về kiểu dữ liệu boolean
2. phải có dòng lệnh để thay đổi gía trị qui định kết thúc vòng lặp
'''
# i = 0
# while i < 10:
#     print(i)
#     i += 1
    
# i++, ++i -> đều tăng i lên 1 
# ++i -> tăng i trước rồi mới thực thi lệnh
# i++ -> thực thi lệnh trước rồi mới tăng i

# a = 5
# b = a++
# print(b)

#? CTDL trong python: set, tuples, list, dictionary

'''
primitive (tham trị): chứa giá trị, có thể thay đổi được
reference (tham số)


Các loại kiểu dữ liệu (nâng cao)
1. immutable - bất biến: str, int, float, boolean, tuples -> nó sẽ luôn tạo ra đối tượng mới khi gán lại giá trị của 1 biến cho biến khác
2. mutable - có biến: giá trị của biến này khi gán cho biến khác -> lưu địa chỉ cấp phát bộ nhớ chứ không lưu giá trị
'''
# a = 10
# b = a # b = 10

# a += 50 # a = 60

# print("a:",a)
# print("b:",b)

''' 
Đặc điểm của Set: 
1. Khai báo: {}
2. Không được sắp xếp -> mình không thể lấy giá trị của phần tử theo index
3. Không chứa dữ liệu trùng lặp -> bỏ hết dữ liệu trùng lặp nếu khai báo
4. Không thay đổi (tương tác) được với phần tử trong set
'''

# my_set = set({1, 2, 3, 4, 5})
my_set = {1, 2, 3, 4, 5, 6}
print(my_set)
print("Chiều dài set:", len(my_set))

''' 
Đặc điểm của Tuples: 
1. Khai báo: ()
2. Không được sắp xếp (mình vẫn lấy giá trị của phần tử theo index)
3. Không thay đổi (tương tác) được với phần tử trong tuples
4. Chứa được dữ liệu trùng lặp

VD: toạ độ của 1 vị trí (x, y), danh sách giá sản phẩm ($4, $5, ...)
'''
my_tuples = (100, 200, 300, 400, 100, 200)
print(my_tuples)

print("Chiều dài của tuples:", my_tuples)

'''
Đặc điểm của list:
1. Khai báo: []
2. Có thể được sắp xếp -> lấy giá trị của phần tử theo index
3. Tương tác được với phần tử trong list: thêm, xoá, sửa = CRUD
4. Chứa được dữ liệu trùng lặp
'''
# my_list = [2, 5, 6, 4, 9] 
# my_list.append(6)
# print("List được thêm vào: ", my_list) # [2, 5, 6, 4, 9, 6]

# my_list.pop() # Xoá giá trị cuối cùng (k có tham số), có tham số -> xoá theo index
# my_list.remove(2) # Remove: xoá hết giá trị truyền vào hàm remove

# print("List được xoá: ", my_list)

# my_list.sort() # Sắp xếp các giá trị tăng dần (mặc định) -> [2, 4, 5, 6, 6, 9]
# print("List được sắp xếp:", my_list)

# print("Chiều dài list:", len(my_list))

# for item in my_list:
#     print(item)

'''
Đặc điểm của dictionary = object / JSON:
1. Khai báo: {}, chứa các phần tử là 1 cặp key (bắt buộc là chuỗi) - value (kiểu dữ liệu nào cũng được)
2. Lấy gía trị (my_dict.values()), lấy key (my_dict.keys()), lấy cả 2 (my_dict.items())
3. Tương tác được với phần tử trong list: thêm, xoá, sửa = CRUD
4. Không được chứa key trùng lặp, giá trị của từng key thì không ảnh hướng
5. Không sắp xếp được
'''
my_dict = {
    "name": "Nguyen Duy", 
    "age": 18,
    "phone": 123456
}

# for key, value in my_dict.items():
#     print(key, value)
    
# my_dict["job"] = "Giang Vien"

# print("Dictionary được thêm: ", my_dict)

# my_dict["age"] = 20

# print("Dictionary được cập nhật: ", my_dict)

a = [1, 2, 3, 4, 5, 6] 
b = a # b = [1, 2, 3, 4, 5, 6]

a.append(7) # a = [1, 2, 3, 4, 5, 6, 7]

print("a:", a)
print("b:", b)




