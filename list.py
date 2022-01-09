# List cũng giống như mảng
#1. create a list
# list chứa mọi loại dữ liệu
list_2 = list() # empty list
list_1 = ['banna',333,'pepsi',333,'cola',333]
print(list_1)

#2. Access element
print(len(list_1)) # số lượng giá trị
print(list_1[2])

#3 tìm vị trí của phần tử trong list ta cũng có index()
print(list_1.index(333))

#4 đếm phần tử trong list lặp bao nhiu lần
print(list_1.count(333))

#5 duyệt qua các giá trị trong list
for value in list_1:
    print(value)

#6 in ra giá trị và vị trí các phần tử trong list
for id,value in enumerate(list_1):
    print(f'tại vị trí {id+1}, giá trị là {value}')   
# for id,value in enumerate(list_1,start=1):
#     print(f'tại vị trí {id}, giá trị là {value}')    

#7 slicing cắt các phần tử [start:end:step]

print(list_1[1:])
print(list_1[1:2])
print(list_1[-1])
print(list_1[1::2])
print(list_1[::-1]) # đảo ngược list


# các hàm cơ bản
#1. add to list
print(list_1*2)
print(list_1+[100,'thantay']) # tạo 1 list mới

#2. thêm 1 giá trị dùng hàm append
list_1.append(100) # chỉ có thể thêm 1 gtri
print(list_1)

#3 thêm nhiều giá trị dùng extend
list_1.extend([130,'thanhtayts']) # chỉ có thể thêm 1 gtri
print(list_1)

#4 thêm 1 giá trị tại 1 index trong list
list_1.insert(3,'alabatrap') #(index, value)
print(list_1)

#5 xóa phần tử theo index trong list, mặc định là xóa phần tử cuối
print(list_1.pop(1))
print(list_1.pop())
print(list_1)

#6 Remove giá trị trong list
list_1.remove(333) # chỉ xóa gia trị đầu tiên khi nó gặp
print(list_1)

#7 xóa gia tri theo index
del list_1[3]
print(list_1)

#8 sắp xếp các phần tử trong list
list_3 = [1,2,8,5,7,9,3]
list_3.sort() # sắp xếp theo thứ tự tăng dần 
print(list_3)
list_3.sort(reverse=True) # sắp xếp theo thứ tự giảm dần 
print(list_3)

#9 đảo chỗ các phần tử trong list
list_1.reverse()
print(list_1)

# 10 sắp xếp và đảo phần tử trên 1 list mới
#sorted(), reversed()
print(sorted(list_3))
print(list(reversed(list_3)))

#11 tìm max min trong list
print(max(list_3))
print(min(list_3))
print(sum(list_3))


#13 copy a new list
list_4 = list_3.copy()
print(list_4)

#14 Clear all element in list
list_3.clear()
print(list_3)


# List hay còn đc gọi là array
# trong list ta cũng xử lý đc slicing giống như String
# các hàm cơ bản
#1 thêm 1 phần tử bằng append
#2 thêm nhiều phần tử bằng extend
# thêm phần tử bằng cách cho list + giá trị 
# thêm giá trị vào 1 index cụ thể ta dùng insert
#3 xóa phần tử bằng pop
#4 xóa các phần tử bằng remove
#5 xóa các phần tử theo index dùng hàm del
#6 sắp xếp các phần tử theo thứ tủ tăng và giảm dùng sort
#7 đảo list ta dùng hàm reverse
#8 duyệt mảng dùng for
#9 duyệt  nếu trả về cả index và value thì dùng enumurate
# duyệt 2 list cùng lúc ta dùng hàm zip
# sorted và reversed ta sẽ tạo ra 1 list mới và thực hiện trên đó
# các tính toán cơ bản như
# min(list) giá trị nhỏ nhất của chuỗi
# max(list) giá trị lớn nhất của chuỗi
# count() số lượng phần tử trong list
# sum() tổng đai số trong list
# len() độ dài của list