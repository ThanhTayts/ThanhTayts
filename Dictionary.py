# Dict là tập hợp key và value
# mỗi cặp key , value đc gọi là 1 item, key là duy nhất trong dict
# dict được khởi tạo bằng dấu {}
dict_1 = {'name':'thanhtay','age':13,'student':'utc2'}
print(dict_1)
# khởi tạo dictinary bằng hàm dict()
dict_2 = dict(name='thanhtay',age=13,city = 'quynhon')
print(dict_2)
# access item bằng ['key']
content_in_dict = dict_2['name']
print(content_in_dict)
# kiểm tra key có trong dict hay không
if 'age' in dict_2:
    print(dict_2['age'])
else:
    print('No')    

# dùng try và except
try:
    print(dict_2['alaba'])
except KeyError:
    print('no key found')    

# thêm và thay đổi giá trị các item
#1. add thêm item
dict_2['email'] = 'thanhtay@gmail.com'
print(dict_2)   
#2. thay đổi giá trị trên key, ta sẽ ghi đè gia trị lên
dict_2['email'] = 'thanhtay@yahoo.app'
print(dict_2)
#3 xóa các item 
del dict_2['email']
print(dict_2)
#4 hàm pop() remove value khi truyền cào key
print('pop values : ' + dict_2.pop('city'))
print(dict_2)
#5 popitem sẽ remove giá trị cuối cùng của dict
print(dict_1)
dict_1.popitem()
print(dict_1)
#6 duyệt qua các key trong dict dùng hàm keys
# for key in dict_1:
#     print(key, dict_1[key])
# for key in dict_1.keys():
#     print(key, dict_1[key])

#7 duyệt qua các value trong dict dùng hàm values
for value in dict_1.values():
    print(value)
#8 duyệt qua cả key và value bằng hàm items    
for key,value in dict_1.items():
    print(key,  value)


# về string có 2 bộ mã là Ascii và Unicode  
# Ascii(7-bit) không có tiếng việt
# Unicode là bộ mã mới hỗ trợ nhiều thứ tiếng
# Unicode có 3 bộ thông dụng UTF-8, UTF-16, UTF-32   