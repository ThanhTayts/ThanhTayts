# String chuỗi ksi tự
# theo thứ tự, không thể thay đổi được, biểu diễn văn bản
# Mutable : có thể thay đổi được list, dict, set, bytearray
#Imutable : k thay đổi được giá trị string tuple range


my_string = "Hello word"
print(my_string, type(my_string))
my_name = "my name s' thanh tay"
# Escaping backslash \
my_string = 'I\'m "sinh vien giao thông"'
my_tring =  " I'm living sig \"singapo\""


# access characters and substrings
#Index
my_string = "hello word"
print(my_string[-1])
# String is immutable cannot be changed
# substring with slicing
sub_string = my_string[1:5]
sub_string = my_string[:-1]
sub_string = my_string[::-1] # đảo ngược chuỗi
sub_string = my_string[::2] # lấy cách 2 kí tự
print(sub_string)

# concat string with +
greeting = "chào các bạn"
channel = "đã đến cới channel của tớ"
sentence = greeting + "sinh viên" + channel
print(sentence)

# nối các chuỗi bằng .join()
my_list = ['12','a','c']
sentence = '*'.join(my_list)
print(sentence)
# Iterating
my_string = "hello xin chào các bạn"
for char in my_string:
    print(char)

if "h" in my_string:
    print("yes")
else:
    print("no")   

# basic and useful function
#1. Strip()  dùng để loại bỏ khoảng trống ở đầu và cuối chuỗi
print("     I am along    ".strip())
print("On the moon".strip('O')) # loại bỏ chữ O
#2.split() tách các ksi tự thành 1 array 
print("hello các bạn".split())
print("hello, các, bạn".split(',')) # split ra bằng dấu phẩy
#3 replace() thay thế các từ
print('help me'.replace('me','you'))
#4 hàm kiểm tra string có bắt đầu bằng kí tự hay k thì t dùng hàm startswith
my_string = 'Need your love'
print(my_string.startswith('Need'))
#5 hàm kiểm tra string có kết thúc với các kí tự endswith
my_string = 'I love you loi'
print(my_string.endswith('loi'))
#6 check vị trí của char trong string hàm index và hàm find()
my_string="baby i love you"
print(my_string.index('i'))
print(my_string.find('i'))
#7 chuyển string thành in hoa
print(my_string.upper())
#8 chuyển string thành in thường
my_string = 'I LOVE YOU BABY'
print(my_string.lower())
#9 in hoa tiêu đề
print(my_string.title())
#10 In hoa chữ cái đầu tiền của chuỗi
print(my_string.capitalize())
#11 đếm số lượng các phần tử trong string
print(my_string.count('O'))


# định dạng chuỗi
# %, .format(), f-Sting

#1. %
name = 'thanhtayts'
my_num = 810.456
my_string = "love loi than %s, %.2f " %(name,my_num)
print(my_string)

#2. format
age = 22
height = 170
my_string = " I'm {} years old {:.2f} cm ".format(age,height)
print(my_string)

#3. f-String
pi = 3.1433423
name = 'thanhtay'
age = 24
my_string = f'pi is {pi:.2f} and my name is {name} , {age}'
print(my_string)


# các hàm cơ bản như
# join nối các kí tự bằng 1 kí tự nào đó
# strip xóa các khoảng trắng đầu dòng và cuối dòng
# split cắt các kí tự ra thành 1 mảng
# index và find để tìm theo vị trí
# starswith tìm xem có bắt đầu bằng kí tự
# endswith có kết thúc bằng kí tự
# upper để in hoa các kí tự
# lower để in thường các kí tự
# titel để in hoa các chữ cái đầu
# Capitialize để in hoa chữ cái đầu tiên
# hàm count để đếm số lượng các kí tự lặp trong string
# hàm replace để thay thế 1 kí tự

# các kiểu định dạng tròn string
#1. định dạng theo kiểu %
#2. định dạng theo .format
#3. định dạng theo kiểu f-String
