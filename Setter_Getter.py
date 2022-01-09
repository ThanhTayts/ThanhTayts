# # Setter : thiết lập giá trị
# # Getter : lấy giá trị
# #đây là cách thiết lập giá trị và lấy giá trị các thuộc tính của class mà không vi phạm đến tính an toàn của chúng


# #1. Getter là phương thức dùng để lấy dữ liệu thuộc tính của một lớp
# # Setter là phương thức dùng để thiết lập giá trị cho thuộc tính.


# #2. Tạo getter và setter theo cách thông thường
# # Cách tạo thông thường
# class className:
 
#     # Thuộc tính name
#     __name = ''
 
#     # Setter cho name
#     def setName(self, name):
#         self.__name = name
 
#     # Getter cho name
#     def getName(self):
#         return self.__name
 
# # Sử dụng
# c = className()
# c.setName("Cường")
# print(c.getName())
# #Thuộc tính __name đang ở cấp độ private, đây cũng chính là cấp độ nên sử dụng khi khai báo các thuộc tính trong lập trình hướng đối tượng.

# #3. Cú pháp getter và setter trong Python
# #Để khai báo một hàm là setter thì ta sử dụng từ khóa @name.setter, 
# # còn getter thì sử dụng từ khóa @property, cả hai đều được đặt phía trước khai báo hàm (phương thức).

class Freetuts:
 
    # Thuộc tính name
    __domain = ''
 
    # Getter
    @property
    def domain(self):
        print("Getter được gọi")
        return self.__domain
 
    # Setter
    @domain.setter
    def domain(self, domain):
        print("Setter được gọi")
        self.__domain = domain

# Sử dụng
c = Freetuts()
c.domain = "https://freetuts.net"
print(c.domain)        

#tên của thuộc tính là __domain và nó ở dạng private. 
# Nhưng khi sử dụng thì bạn có thể đổi thành domain vì mình đã khai báo đó là những setter và getter