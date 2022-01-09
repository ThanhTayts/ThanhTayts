#################################################################
#                             _`				#
#                          _ooOoo_				#
#                         o8888888o				#
#                         88" . "88				#
#                         (| -_- |)				#
#                         O\  =  /O				#
#                      ____/`---'\____				#
#                    .'  \\|     |//  `.			#
#                   /  \\|||  :  |||//  \			#
#                  /  _||||| -:- |||||_  \			#
#                  |   | \\\  -  /'| |   |			#
#                  | \_|  `\`---'//  |_/ |			#
#                  \  .-\__ `-. -'__/-.  /			#
#                ___`. .'  /--.--\  `. .'___			#
#             ."" '<  `.___\_<|>_/___.' _> \"".			#
#            | | :  `- \`. ;`. _/; .'/ /  .' ; |		#
#            \  \ `-.   \_\_`. _.'_/_/  -' _.' /		#
#=============`-.`___`-.__\ \___  /__.-'_.'_.-'=================#
#                           `=--=-'                             #


'''
          _.-/`)
         // / / )
      .=// / / / )
     //`/ / / / /
    // /     ` /
   ||         /
    \\       /
     ))    .'
    //    /
         /
'''





# Json là 1 định dạng dữ liệu (chuỗi)
# Json : JavaScript Object Notation
# Json thể hiện các kiểu dữ liệu về số, bool, null, array, String
# Stringify/ Parse
# chuyển đổi sang json/ và trả lại kiểu dữ liệu ban đầu


import json
# tạo 1 dictionary object trong python
book = {}
book['tom'] = {'name':'tom','address':'tây sơn','phone': '0393781734'}
book['bob'] = {'name':'bob','address':'quy nhơn','phone': '3043781734'}

# chuyển từ object python sang object Json bằng hàm dumps
s = json.dumps(book)
print(s)


with open('D://Data_science//data//book.txt','w') as f: # lưu file dạng txt
    f.write(s) # ghi dữ liệu s vào file lưu

# chuyển từ object Json về object python bằng hàm load 
f = open('D://Data_science//data//book.txt','r') 
s = f.read()
print(s)

book = json.loads(s)
# print(book)

# print(type(book))

print(book['bob'])
print(book['bob']['address'])

