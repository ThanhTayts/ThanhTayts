# Class trong Python(lập trình hướng đối tượng)
# hàm khởi tạo
# - tính kế thừa 
# - các mực độ truy cập public / private và public.

# đối tượng sẽ có 2 thông tin chính, là các thuộc tính và các hành động
# Class là một lớp trong Python, dùng để khai báo cấu trúc thuộc tính và hành động cho một đối tượng nào đó

# khởi tạo class sinh viên
class Student:
    # khởi tạo các thuộc tính
    id = ''
    name = ''
    # khởi tạo các hành động
    def add(self,id,name):
       self.name = name # dùng seft để trỏ đến các thuộc tính
       self.id = id 
       print('đây là hàm add')

    def show(self):
        print('id: ', self.id)
        print('name: ',self.name)   
       


#self của class trong Python   
# Self là tham số ảo bắt buộc truyền vào khi khai báo phương thức, 
# nó không được tính là một tham số phải truyền vào khi sử dụng phương thức. 
# Self chính là biến trỏ đến chính đối tượng  
# class là 1 nhóm đối tượng vd như chó là nhóm đối tượng, chó cỏ là 1 đối tượng trong đó
# ta khởi tạo 1 đối tượng từ class Student
s = Student()
s.add(76, 'Thanh Tây')
s.show()

# tạo nhiều instance object
s1 = Student()
s1.add(77,'thanhtay')
s1.show()

s2 = Student()
s2.add(67,'thanhtayts')
s2.show()

s3 = Student()
s3.add(56,'tay')
s3.show()


#Các loại phương thức của class trong Python

#1. hàm khởi tạo def__init__
# hàm sẽ được tự động gọi khi bạn tạo mới một đối tượng (instance object).

# ví dụ ta tạo 1 class
class Dog:
    name = "",
    country = ""

    def __init__(self,name,country):
        self.name = name
        self.country = country
#khi khởi tạo đối tượng mới thì phải truyền luôn hai giá trị name và country 
# thì lúc này sẽ sử dụng hàm khởi tạo.    
# khởi tạo 1 đối tượng mới
dog = Dog('thanhtay','quinhon')
print(dog.name)   


#2. phương thức tĩnh staticmethod
#Phương thức tĩnh là loại phương thức có thể được gọi 
# mà không cần phải khởi tạo đối tượng class trong Python.
# class Mathematics:
#     def addNumbers(self, x, y):
#         return x + y
# m = Mathematics()
# print(m.addNumbers(12, 15))
# với cách trên ta cần tạo 1 opject

class Mathematics:
 
    @staticmethod
    def addNumbers(x, y):
        return x + y
 
# Cách dùng
print(Mathematics.addNumbers(12, 15))
# với cách này ta k cần tạo opject ta gọi trực tiếp trong Class luôn



#3. Kế thừa class trong python
#Một class A có thể được kế thừa từ một class B khác, 
# lúc này ta gọi A là lớp con và B là lớp cha
#Lớp con có thể kế thừa các thuộc tính và phương thức của lớp cha, 
# trừ trường hợp đó là một private method
# syntax : class classcon(classcha):
# sau khi đã kế thừa thì class con vẫn có thể thêm các hành động khác

# Animal
class Animal:
    ten = ''
    gioitinh = ''
 
    def an(self):
        print("Ăn")
    def chay(self):
        print("Chạy")
 
# Dog kế thừa từ Animal
class Dog(Animal):
 
    def sua(self): # thêm 1 hành động mới cho class Dig
        print("Con chó sủa Go Go!") # luxc này class dog có 3 hành động
 
# Cách dùng
d = Dog()
d.an()
d.chay()
d.sua()



#4. Mức độ truy cập public / protected và private
# Trong lập trình hướng đối tượng thì các thuộc tính và phương thức sẽ có 3 mức độ truy cập khác nhau
#Public: là câp độ phổ biến nhất, có thể sử dụng ở cả bên trong và ngoài lớp
#Protected: Là cấp độ được bảo vệ, chỉ dùng trong nội bộ của lớp đó và lớp con kế thừa.
#Private: Là cấp độ bảo mật nhất, nó chỉ được dùng bên trong chính lớp đó mà thôi.


#Sử dụng hai dấu gạch dưới (__) để khai báo cho mức private
#Sử dụng một dấu gạch dưới (_) để khai báo cho mức protected
#Không sử dụng dấu gạch dưới là public.

# Animal
class className:
 
    # Thuộc tính
    name = '' # public
    _name = '' # protected
    __name = '' # private
 
    # Phương thức
    def getName(self): # public
        return 0
 
    def _getName(self): # protected
        return 0
 
    def __getName(self): # private
        return 0

# ví dụ dễ hiểu nhất
class Dog:
    __name = ''
    name = ''
 
    def setName(self, name):
        # Đúng vì thuộc tính private có thể truy cập trong class
        self.__name = name
 
    def showName(self):
        print(self.__name)
 
d = Dog()
 
# Đoạn code này sai vì __name ở mức private
d.__name = 'Chó Bull'
 
# Đúng vì name là public
d.name = 'Chó Bull'
 
# Đúng vì hàm setName là public
d.setName("Chó Bull")
 
# Đúng vì showName là public
d.showName();        