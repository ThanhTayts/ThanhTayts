# argument and keyword argument
# function
# def print_name(name): # name dc goi la parameter
#     print(name)

# def print_name(name,greeting): # name va greeting la tham so bat buoc
#     print(f'{name},{greeting}')

# def print_name(name,greeting='xin chao'): # name la tham so bat buoc, greeting la tham so defaut
#     print(f'{name},{greeting}')


# arg : argument: input cua function

def codeexplore(a,b,c):
    print(a,b,c)

# def main():
    # codeexplore(1,2,3)  #positinal arg : theo vi tri
    # codeexplore(a=12, c='ad',b='thanh')  #keyword arg : theo keyword
   

 

# variable length Parameters : tham so vo do dai thay doi
#*args va **kwargs

# với *args ta có thể paste vào trong hàm bất kì số nào hoặc bất kì positinal arg
# *args trả về dưới dạng list

# với **kwargs ta có thể paste bất kì biến từ khóa vào trong hàm
# **kwargs return về dictionary

#*args và **kwargs có truyền vào hay không thì hàm vẫn chạy
def variablelenghtArg(a,b,*args,**kwargs):
    print(a,b)
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(key,value)  

def main():
    variablelenghtArg("a","b","hello word",1, size = 'up',age = 13 )


if __name__ == "__main__":
    main()   