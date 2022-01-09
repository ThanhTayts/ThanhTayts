#Trong Python, kiểu dữ liệu Tuple tương tự như mảng,
# sự khác biệt giữa chúng là ta không thể thay đổi các phần tử của một tuple, 
# trừ khi phần tử đó là một mảng
# uple có thể được sử dụng làm khóa cho Dictionary
# Một tuple được tạo bằng cách đặt tất cả các mục (phần tử) bên trong dấu ngoặc đơn ()
# được phân tách bằng dấu phẩy.

# có thể chứa được nhiều loại dữ liệu
my_tuple = ("freetuts", [8, 4, 6], (1, 2, 3))
print(my_tuple)

# tuple có thể được tạo bằng cách bỏ đi cặp ngoặc đơn
my_tuple = 3, 4.6, "blog"
print(my_tuple)
# Kết quả: 3, 4.6, "blog"

# Bạn có thể tách các phần tử tuple thành nhiều biến nhỏ
a, b, c = my_tuple
print(a)
print(b)
print(c)

#Việc tạo một Tuple chỉ có một phần tử sẽ phức tạp hơn một xíu,
#bởi vì trường hợp này thì Python sẽ dễ bị nhầm lẫn sang kiểu string, vì vậy ta phải bổ sung thêm dấu phẩy ở cuối để trình biên dịch Python nhận biết đó là một Tuple.
# Bạn thêm dấu phẩy để Python biết đây là 1 tuple
my_tuple = ("hello",)
print(type(my_tuple))
my_tuple = "hello",
print(type(my_tuple))
# Kết quả: <class 'tuple'>

# access element
# Danh sách Tuple
my_tuple = ('p','e','r','m','i','t')
 
# Lấy phần tử đầu tiên trong tuple
print(my_tuple[0])
# Output: 'p'
 
# Lấy phần tử thứ 6 trong tuple
print(my_tuple[5])
# Output: 't'
 
# Mỗi phần tử của tuple là một mảng hoặc 1 tuple khác
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
 
# Lấy phần tử thứ 4 của phần tử thứ nhất
print(n_tuple[0][3])
# Output: 's'
 
# Lấy phần tử thứ 2 của phần tử thứ 2
print(n_tuple[1][1])
# Output: 4

# Slicing
# Lấy phần tử thứ 2 đến thứ 4
print(my_tuple[1:4])
# Output: ('r', 'o', 'g')
 
# Phần tử đầu tiên đến thứ hai (tức thứ 7 tính từ sau tới)
print(my_tuple[:-7])
# Output: ('p', 'r')
 
# Phần tử thứ 8 đến cuối
print(my_tuple[7:])
# Output: ('i', 'z')
 
# Lấy toàn bộ phần tử
print(my_tuple[:])
# Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')


# không thể thay đổi giá trị của tuple vì tuple là 1 imutable

# Xóa tuple dùng lệnh del
my_tuple = ('p','r','o','g','r','a','m','i','z')
 
# Xóa biến my_tuple
# del my_tuple
 
# các hàm cơ bản của tuple
print(my_tuple.count('a'))
print(my_tuple.index('r'))

# check xem phần tử có xuất hiện trong tuple hay không
if 'p' in my_tuple:
    print('yes')
else:
    print('no')  

if 'b' not in my_tuple:
    print('Yes')
else:
    print('no') 

# duyệt qua các phần tử của tuple
for value in my_tuple:
    print(value)             