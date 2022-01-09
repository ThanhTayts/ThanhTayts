# hàm lambda là 1 hàm ẩn danh
# cú pháp lambda arg:expressin
# lambda tạo hàm ngắn gọn và không có tên hàm
#lambda là từ khóa khai báo hàm lambda
#arguments là danh sách các tham số truyền vào hàm
#expression là biểu thức tính toán của hàm

from agrs_kwargs import codeexplore


code = lambda so : so + 69 # cú pháp đơn giản
print(code(1))

# hàm lambda trên tương tự
def code(so):
    return so + 69

# hàm lambda nhận nhiều tham số    
codes = lambda x,y,z : x+y-z # cú pháp đơn giản
print(codes(6,9,3))

# ứng dụng của hàm lambda
# hàm lambda kết hợp với hàm sord
coordinate2D = [(6,9),(9,6),(-1,2),(2,10)]
print(sorted(coordinate2D)) # mặc định là sẽ sort lớn dần theo giá trị đầu tiên 
print(sorted(coordinate2D,reverse=True)) # sort nhỏ dần theo giá trị đầu tiên 
print(sorted(coordinate2D, key=lambda i : i[1])) # sort lớn dần theo vị trí số 2
print(sorted(coordinate2D, reverse=True ,key=lambda i : i[1])) # sort nhỏ dần theo vị trí số 2


my_list = [1,2,-3,-1,3,-2]
print(sorted(my_list))
print(sorted(my_list, key=lambda x : abs(x)))

# hàm lambda với hàm map
# hàm map cho phép chuyển đổi các thành phần của list theo 1 hàm nào đó
# map(func, sequenc)
list_key = ['code','wellcome','các bạn']
print(map(lambda x : x.title(), list_key))
print(list(map(lambda x : x.title(), list_key)))
# tương tự với list comprehension

# hàm lambda với hàm filter()
# filter(func,sequenc) return các element khi hàm func trả về true
number_list = [1,2,3,4,5,6,7,8,9,10]
print(filter(lambda i : i%2 ==0, number_list))
print(list(filter(lambda i : i%2 ==0, number_list)))
# trả về các giá trị khi hàm function trả về True

# hàm lambda với hàm reduce()
#reduce(func,seq) trả vè 1 giá trị duy nhất khi áp dụng func vào seq
from functools import reduce
sequence = [1,2,3,5,6,7,8]
print(reduce(lambda a,b:a+b, sequence))
# 1+2 =3 , 3+2 = 5
print(reduce(lambda a,b : a if a>b else b,  sequence))
# trả về a nếu a >b ngược lại trả về b
