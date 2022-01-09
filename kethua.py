#Kế thừa (Inheritance) là việc một lớp được khai báo kế thừa toàn bộ thuộc tính và phương thức của một lớp khác
#Lớp được kế thừa ta gọi là lớp con, và lớp kế thừa ta gọi là lớp cha
#Lớp con có thể sử dụng toàn bộ dữ liệu khai báo ở mức độ protected và public ở lớp cha.
#Riêng với private thì không được, vì đó là mức độ bảo mật cao nhất, chỉ sử dụng bên trong nội bộ của lớp cha.

# class Xe:
#     name = 'Đây là tên xe'
 
# class XeDap(Xe):
#     def showName(self):
#         # sử dụng thuộc tính name của lớp cha
#         print(self.name)
 
# # Cách dùng
# d = XeDap()
# d.showName()

# #Sử dụng phương thức của lớp cha
# class Xe:
#     name = ''
#     def setName(self, name):
#         self.name = name
 
# class XeDap(Xe):
#     def showName(self, name):
#         # Sử dụng phương thức của lớp cha
#         self.setName("Xe đạp")
 
#         # sử dụng thuộc tính name của lớp cha
#         print(self.name)
 
# # Cách dùng
# d = XeDap()
# d.showName("Xe đạp")


#Nếu cả lớp cha và lớp con đều có hàm khởi tạo thì Python sẽ chạy hàm khởi tạo ở lớp con 
# class Xe:
#     def __init__(self):
#         print("Hàm khởi tạo lớp cha")
 
# class XeDap(Xe):
#     def __init__(self):
#         print("Hàm khởi tạo lớp con")
 
# Cách dùng
# d = XeDap()

# nếu mún gọi hàm khởi tạo ở lớp cha thì dùng hàm supper()
class Xe:
    def __init__(self):
        print("Hàm khởi tạo lớp cha")
 
class XeDap(Xe):
    def __init__(self):
        # Gọi hàm khởi tạo lớp cha
        super().__init__()
 
        print("Hàm khởi tạo lớp con")
 
# Cách dùng
d = XeDap() # hàm khởi tạo lớp cha sẽ in ra trước rồi sau đó đến lớp con


# ta cũng có thể gọi hàm khởi tạo của lớp cha trong lớp con bằng cách
# gọi ra tên cảu lớp cha cùng với phần __init__
class Xe:
    def __init__(self):
        print("Hàm khởi tạo lớp cha")
 
class XeDap(Xe):
    def __init__(self):
        # Gọi hàm khởi tạo lớp cha
        Xe.__init__(self)
 
        print("Hàm khởi tạo lớp con")
 
# Cách dùng
d = XeDap()