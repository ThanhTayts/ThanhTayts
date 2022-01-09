#Set trong Python là tập các phần tử dữ liệu không có thứ tự, mỗi phần tử là duy nhất (không trùng lặp) 
# và phải bất biến (không thể thay đổi)
# Tuy nhiên chúng ta có thể thêm hoặc xóa các phần tử ra khỏi Set một cách dễ dàng.
 #Vì các phần tử không thể thay đổi giá trị nên Set không cho phép lưu trữ kiểu List hoặc Dictionary.

 # khởi tạo
# Tập hợp set kiểu int
my_set = {1, 2, 3}
print(my_set)
 
# Tập hợp set đa dạng kiểu khác
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

# Set không chứa dữ liệu trùng nhau
# Như trong tập hợp này mình cố tình cho trùng giá trị 3
# Nhưng khi in ra thì nó chỉ lấy 1 số 3 mà thôi
my_set = {1,2,3,4,3,2}
print(my_set)
# Output: {1, 2, 3, 4}
 
# Set không thể chứa tập hợp có thể thay đổi như Dictionary và List
# Ta có thể khởi tạo giá trị của set qua ...
# đối tượng Set() trong Python
# bằng cách truyền vào một list (array)
my_set = set([1,2,3,2])
print(my_set)
a = set() # khởi tạo set rỗng

# Thêm một phần tử vào set
my_set.add(2)
print(my_set)
# Output: {1, 2, 3}
 
# Thêm nhiều phần tử vào Set, ta dùng mảng để chứa các phần tử đó
my_set.update([2,3,4])
print(my_set)
# Output: {1, 2, 3, 4}
 
# Cập nhật set bằng một list và set mới
# Nó sẽ duyệt và loại bỏ bớt giá trị trùng nhau
my_set.update([4,5], {1,6,8})
print(my_set)
# Output: {1, 2, 3, 4, 5, 6, 8}

# Khởi tạo my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)

# Xóa phần tử có giá trị 4
my_set.discard(4)
print(my_set)
# Output: {1, 3, 5, 6}
 
# Xóa phần tử có giá trị 6
my_set.remove(6)
print(my_set)
# Output: {1, 3, 5}
 
# Xóa phần tử
# không tồn tại trong my_set
my_set.discard(2)
print(my_set)
# Output: {1, 3, 5} => Không bị lỗi




# Khởi tạo my_set
my_set = set("HelloWorld")
print(my_set)
# Output: {'r', 'd', 'o', 'e', 'W', 'H', 'l'}
 
# pop một phần tử ngẫu nhiên
print(my_set.pop())
# Output: Tùy thuộc vào giá trị mà nó xóa mà in kết quả khác nhau
 
# pop thêm một phần tử ngẫu nhiên khác
my_set.pop()
print(my_set)
# Output: Cũng là random
 
# clear my_set, kết quả trả về Set rỗng
my_set.clear()
print(my_set)
#Output: set()