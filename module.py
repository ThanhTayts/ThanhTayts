# Module trong python là 1 file python bên ngoài cái đuôi py ta sử dụng để gọi hàm trong 1 file khác
# import module
# from module import function


# có thể import nhiều module cách nhau bởi dấu phẩy
# from import cũng có thể import nhiều function 
# cách viết import module hay function ngắn gọn ta sử dụng từ as
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# có thể xem các thuộc tính và phương thức của module bằng hàm dir

# import math
# properties = dir(math)
# print(properties)


# Reload lại module để sử dụng cho các tính toán mới bằng hàm reload
#reload(calculation)


# phạm vi biến của module trong python
#1. biến toàn cục sử dụng ở tất cả các vị trí trong chương trình trừ hàm
#2. biến cục bộ sử dụng trong phạm vi nhất định, dùng trong hàm



# xem các module có sẵn trong python
print (help('modules') )
