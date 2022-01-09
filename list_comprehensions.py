# List Comprehensions
# giúp viết code ngắn gọn hơn
# cấu trúc  [<action> for <item> in <iterator> if <some condition>]
word = 'hello word'
# for char in word:
#     print(char)

print([char for char in word])    


number = [i for i in range(0,10) if i%2==0]
print(number)


hoa_don = [100,200,300,400]
thue = 0.08
tips = 0.07

def tongtien (bill):
    return bill*(1+thue+tips)

total = [tongtien(bill) for bill in hoa_don]
print(f'Tổng bill của hóa đơn là {total}')


# hàm nâng cao
#1 chuyển chuỗi sang list
a = list()# tạo list rỗng
print(a)
my_string = 'welcome to my channel'
list_of_char = list(my_string)
print(list_of_char)


#2 hàm sum() cộng tất cả giá trị của list 
#3 hàm zip() dùng lặp 2 list cùng lúc
name = ['adam','amin','maca']
layer = ['cnn','lstm','rnn']

for i,j in zip(name,layer):
    print(f'Hàm tối ưu {i} của mạng {j}')

for index,(i,j) in enumerate(zip(name,layer)):
    print(f'Tại vị trí {index+1} Hàm tối ưu {i} của mạng {j}')


#4. sorted sắp xếp theo chữ cái
sorted_by_fist = sorted(name, key=lambda el:el[1])
print(sorted_by_fist)    # sort theo kí tự thứ 1 

my_string = [{'ten':'bhanhtay','age':23},{'ten':'chanloi','age':22},{'ten':'ainh','age':20}]
sorted_by_key =sorted(my_string,key=lambda el:el['ten'])
print(sorted_by_key)
sorted_by_key =sorted(my_string,key=lambda el:el['age'])

print(sorted_by_key)

# Mảng 2 chiều
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(matrix[2][1])          

# for row in range(len(matrix)):
#     for colum in range(len(matrix)):
#         print(matrix[row][colum])


# tranform matrix to list

print([matrix[row][col]  for row in range(len(matrix)) for col in range(len(matrix))])   # đưa ra 1 list    

# tách ra thành 3 cột riêng lẻ
print([x for x in zip(*matrix)])




# List comprehension
# cấu trúc [action, for value in list ,condition]
# hàm zip() duyệt 2 mảng 1 lần
# sordted dùng với hàm lamba để sắp xếp theo key=
# mảng 2D tạo từ list ta có thể tham chiếu đề từng giá trị hoặc
# duyệt qua từng giá trị dùng 2 vòng for hoặc list comprehension
# thủ thuật zip(*list) để tach ra thành các phần tử riêng lẻ