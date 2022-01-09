# #Override trong Python (Ghi đè trong kế thừa)
# #Ghi đè cho phép một lớp con có thể viết lại các phương thức của lớp cha, 
# # tức là tạo một phương thức ở lớp con trùng tên với phương thức của lớp cha.

# #1 Override là cách viết lại các method ở lớp cha trong lớp con

# # class Animal:
# #     name : ""
 
# #     def move(self):
# #         pass
 
# #     def eat(self):
# #         pass

# # class Dog(Animal):
# #     def move(self):
# #         print('Con chó đi bốn chân')

# # class Duck(Animal):
# #     def move(self):
# #         print('Con vịt đi hai chân')      


# class Animal:
#     name : ""
 
#     def move(self):
#         print('Động vật chuẩn bị đi')
 
#     def eat(self):
#         pass
 
# class Dog(Animal):
#     def move(self):
#         Animal.move(self) # Gọi đến method move của lớp cha
#         print('Con chó đi bốn chân')
 
# # Cách dùng
# t = Dog()
# t.move()


# #3. Override trong kế thừa nhiều lớp
# class Parent():
 
#     def show(self):
#         print("Cha")
 
# class Child(Parent):
#     def show(self):
#         print("Con")
 
# class GrandChild(Child):
#     def show(self):
#         Parent.show(self)
#         print("Cháu")
 
# # Chương trình chính
# g = GrandChild()
# g.show()
