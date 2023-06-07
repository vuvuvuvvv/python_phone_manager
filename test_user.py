import json
import re

class User:
    role = 0 # 0 là khách 1 là admin
    def __init__(self):
        pass
    
    def get_role (self) :
        return self.role
    
    def set_id (self, id):
        self.id = id
        
    def get_id (self) :
        return self.id
    
    def set_name (self, name):
        self.name = name
        
    def get_name (self) :
        return self.name
    
    def set_phone_num (self, phone_num):
        self.phone_num = phone_num
        
    def get_phone_num (self) :
        return self.phone_num
    
    def set_mail (self, mail):
        self.mail = mail
        
    def get_mail (self) :
        return self.mail
    
    def set_gender (self, gender):
        self.gender = gender
        
    def get_gender (self) :
        return self.gender

# Chèn thêm 1 user vào file lưu data User
def write_json(new_data, filename='./data/client/entries.json'):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        content['List_Admin'].append(new_data)
        file_data.update(content)
        file.seek(0)
        json.dump(file_data, file, indent=4)

f = open('./data/client/entries.json', 'r+')
content = json.load(f)

def check_password(password):
    pattern = r"[A-Za-z0-9@#$%^&+=]{8,}"
    if re.fullmatch(pattern, password):
        return True
    else:
        return False
    
def check_phone_number (phone):
    pattern = r"\d{10}"
    if re.fullmatch(pattern, phone):
        return True
    else:
        return False

def check_email(email):
    pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?" 
    if re.fullmatch(pattern, email):
        return True
    else:
        return False
    
def check_name(name):
    pattern = r"^[a-zA-Z\s]+$"
    if re.fullmatch(pattern, name):
        return True
    else:
        return False

def Info_User () :
    print('|_________________________________________________________|')
    print('|  ID  |     Tài khoản    |      Tên      | Số điện thoại |')
    for row in content['List_Admin'] :
        print("{: <10} {: <10} {: <10}".format(*row))
    print('|_________________________________________________________|')

def set_role (role) :
    if content['List_Admin']['Role'] == 1 :
        pass

def login_form () :
    print('Chào mừng đến với trang quản trị')
    print('Vui lòng đăng nhập để truy cập!')
    name = input('Nhập tài khoản: ')
    for e in content['List_Admin']:
        if name == e['User_name']:
            print('Vui lòng nhập mật khẩu của bạn.')
            password = input('Nhập mật khẩu: ')
            for i in range(1,5) :
                if password == e['Password']:
                    print(f'Chào {name}, bạn đã đăng nhập thành công!')
                    return True
                else :
                    if i < 4 :
                        print('Sai mật khẩu.')
                        password = input(f'Nhập lại mật khẩu (lần {i}/3): ')
                    else :
                        print("Bạn không thể truy cập vào tài khoản!")
    return False
            
def register () :
    print('Tài khoản của bạn không có trong dữ liệu hệ thống.')
    print('Bạn cần đăng ký tài khoản.')
    tmp_user = User()
    while True :
        Not_Exist_2 = False
        tmp_user.name = input('Vui lòng nhập tên tài khoản của bạn: ')
        for x in content['List_Admin'] :
            if tmp_user.name == x['User_name']:
                Not_Exist_2 = True
                print("Tài khoản này đã tồn tại!")
                break
        if Not_Exist_2 == True :
            continue
        while True :
            tmp_user.password = input('Vui lòng nhập mật khẩu của bạn: ')
            if check_password(tmp_user.password) == False:
                print('Mật khẩu không hợp lệ')
                continue
            password_again = input('Nhập lại mật khẩu của bạn: ')
            if (tmp_user.password == password_again):
                break
            else :
                print("Mật khẩu không giống nhau!")
                continue    
        tmp_user.id = len(content['List_Admin'])
        while True :
            tmp_user.name = input("Nhập tên của bạn: ")
            if check_name(tmp_user.name) == False :
                print('Tên không hợp lệ')
                continue
            else :
                break
        while True :
            tmp_user.mail = input("Nhập email của bạn: ")
            if check_email(tmp_user.mail) == False :
                print('Email không hợp lệ')
                continue
            else :
                break
        while True :
            tmp_user.phone_num = input("Nhập số điện thoại của bạn: ")
            if check_phone_number(tmp_user.phone_num) == False :
                print('Số điện thoại không hợp lệ')
                continue
            else :
                break
        while True :
            tmp_user.gender = input("Chọn giới tính của mình (0: Nữ / 1: Nam): ")
            if tmp_user.gender == '0' or tmp_user.gender == '1' :
                break
            else :
                print('Lựa chọn giới tính không hợp lệ')
                continue
                
        new_full = {"User_name": f"{tmp_user.name}","Password": f"{tmp_user.password}", "ID": f"{tmp_user.id + 1}", 
                "Name": f"{tmp_user.name}", "Email": f"{tmp_user.mail}", 
                "Phone_number": f"{tmp_user.phone_num}", "Gender": f"{tmp_user.gender}"}
        write_json(new_full)
        print('Tài khoản của bạn đã được thêm vào hệ thống!')
        break
        
# if login_form() == False:
#     register()
    
Info_User()
