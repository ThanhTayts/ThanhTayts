# đa kế thừa
#class B kế thừa class A, class C kế thừa class B. 
#một class có thể kế thừa từ nhiều class khác.


#1. Class kế thừa nhiều lớp trong Python
# class Lop1:
#     # code
 
# class Lop2:
#     # code
 
# class Lopcon(Lop1, Lop2):
#lớp con sẽ có toàn bộ các tính năng của các lớp cha.

#2.Kế thừa đa cấp trong Python
#lớp con được kế thừa từ lớp cha, lớp cha kế thừa từ lớp ông nội, ... 
# A kế thừa B, B kế thừa C, C kế thừa D
# class LopOngNoi:
#     pass
#  
# class LopCha(LopOngNoi):
#     pass
#  
# class LopCon(LopCha):
#     pass
#lớp con sẽ kế thừa toàn bộ những tính năng của các lớp cha và ông nội.


#3. Thứ tự kế thừa trong đa kế thừa Python
#Trường hợp kế thừa đa cấp: Khi lớp con gọi đến một thuộc tính hoặc phương thức thì Python sẽ dò tìm trong lớp con trước, nếu không có thì sẽ dò tiếp lớp cha, nếu vẫn không có thì nó sẽ dò ở lớp ông nội ... cứ như vậy cho đến level cuối cùng.
#Trường hợp kế thừa từ nhiều lớp: Cách hoạt động vẫn như trên, nhưng nó sẽ duyệt từ trái qua phải theo thứ tự mà bạn liệt kê trong lúc kế thừa


#4. Cấp độ truy cập của đa kế thừa trong Python
#Như đơn kế thừa, một lớp chỉ có thể sử dụng tài nguyên ở cấp độ public hoặc protected. 
# Nếu ở ngoài lớp thì mỗi public là sử dụng được.