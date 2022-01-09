# for loop
my_list= [1,2,3] 
my_dict = {'tên':'thanh tây', 'tuổi': 22}
for num in my_list:
    print(num) 

for key,value in my_dict.items():
    print(key,value)

# while loop sẽ thực hiện cho đến khi điều kiện không còn đúng
msg = '' # string rỗng
while msg!= ' quite':
    msg = input('please enter input')
    print(msg)

# break dùng để thoát khỏi vòng lặp
# continue dùng để tiếp tục vòng lặp đầu và bỏ qua câu lệnh phía dưới    