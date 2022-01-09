#Constructors method
#hàm khởi tạo sẽ tự động được gọi mỗi khi bạn tạo mới một instance object của class.
#có tên là __init__ 

class Xe:
    def __init__(self):
        print("Object Xe được khởi tạo")
 
x1 = Xe()
x2 = Xe()


#Hàm khởi tạo cũng là một phương thức bình thường nên bạn cũng có thể truyền tham số cho nó
class Student:
    name = ''
    age = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
c = Student("Nguyễn Văn Cường", 32)
 
print(c.name)
print(c.age)


#Bạn nên sử dụng hàm khởi tạo trong trường hợp muốn chạy một đoạn code nào đó mỗi khi khởi tạo một object, 
# đó có thể là đoạn code cấu hình quan trọng cho đối tượng.