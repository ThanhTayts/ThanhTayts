# Basic datatypes
''' các kiểu dữ liệu cơ bản trong python'''
#1. bool: True:False interget value True=1, False=0
# var_bool = True
# print(type(var_bool))
# a = 4 + True
# print(a)
# b = False
# if b == 0:
#     print(b)

#2. None phần tử không
# var_none = None
# print(type(var_none))   

# if var_none: # if else thì None = False
#     print("Yes")
# else:
#     print("None")   / 

#3. Interger and Float
# print(type(1))
# print(type(-10)) 
# print(type(1.24))  
# print(type(4e2), 4e2) 

#4. Các phép toán cơ bản
# + - * /
# chia lấy phần nguyên  //
# chia lấy dư %
# lũy thừa **

#5.Các hàm toán cơ bản
# hàm mũ pow()
# căn bậc 2 sqrt()
# trị tuyệt đối abs()
# hàm làm tròn round()
#round(5.4343, 2) làm tròn đến chữ số thập phân thứ 2
#chuyển đổi thành dạng binary bin()
# chuyển đổi thành hệ 16  hex()
# a = 10
# print("Giá trị của %d dưới dạng nhị phân là" %a ,format(a,"b"))


'''Viết chưng trình chuyển đổi nhiệt độ '''
def CToConvertF ():
    while True:
        cTemp = float(input('Please enter C degree: '))

        if cTemp:
            fTemp = round((cTemp*9/5)+32, 2)
            print(f"{cTemp} C is convert to  {fTemp} F" )
            break

        else:
            print('C temp input is empty')  
            continue  

def main():
    # print("hello word")
    CToConvertF()

if __name__ == '__main__':
    main()