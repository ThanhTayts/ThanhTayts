import math # thư viện toán học
print(dir(math))
# một số hàm toán học cơ bản như là:
print(math.pow(2,3)) # hàm mũ
print(math.sqrt(25)) # hàm căn bậc 2
print(math.floor(2.4)) # hàm làm tròn xuống
print(math.ceil(2.4)) # hàm làm tròn lên
print(math.log10(10)) # hàm log




import calendar # thư viện lịch(ngày tháng năm)
# một số hàm cơ bản
cal = calendar.month(2021,10)  # tháng trong 1 năm
print(cal)
print(calendar.isleap(2016)) # 2016 có phải là năm nhuận hay không
print(calendar.isleap(2015))# 2015 có phải năm nhuận hay không
print(dir(calendar))



