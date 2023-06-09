import json
import re
from tabulate import *


class User:
    def set_id (self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_phone_num(self, phone_num):
        self.phone_num = phone_num

    def get_phone_num(self):
        return self.phone_num

    def set_mail(self, mail):
        self.mail = mail

    def get_mail(self):
        return self.mail

    def set_gender(self, gender):
        self.gender = gender

    def get_gender(self):
        return self.gender

session_user = {}

f = open('./data/client/entries.json', 'r+')
content = json.load(f)

# Chèn thêm 1 user vào file lưu data json
def save_user_to_json(new_data, filename='./data/client/entries.json'):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        content['List_Client'].append(new_data)
        file_data.update(content)
        file.seek(0)
        json.dump(file_data, file, indent=4)


# Đẩy 1 user từ "List_Client" lên thành admin trong "List_Admin" và xóa user đó trong "List_Client"
def add_admin_to_json(order_user, filename='./data/client/entries.json'):
    with open(filename, 'w') as file:
        tmp = content['List_Client'][order_user-1]
        del content['List_Client'][order_user-1]
        content['List_Admin'].append(tmp)
        file.seek(0)
        json.dump(content, file, indent=4)
    print("Đã cấp quyền admin thành công!")

def check_password(password):
    pattern = r"[A-Za-z0-9@#$%^&+=]{8,}"
    if re.fullmatch(pattern, password):
        return True
    else:
        return False


def check_phone_number(phone):
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

# Xuất thông tin tài khoản
def Info_User (name_list) :
    data = [["STT","ID","Tài khoản","Tên"]]
    i = 1
    for x in content[name_list] :
        tmp = []
        tmp.append(i)
        tmp.append(x["ID"])
        tmp.append(x["User_name"])
        tmp.append(x["Name"])
        data.append(tmp)
        i += 1
    print(tabulate(data, headers='firstrow', tablefmt='grid'))

def merge_Client_Admin_lists () :
    merge = content["List_Admin"] + content["List_Client"]
    return merge

# Form đăng nhập tài khoản
def login_form():
    print('Chào mừng đến với trang quản trị')
    print('Vui lòng đăng nhập để truy cập!')
    name = input('Nhập tài khoản: ')
    for e in merge_Client_Admin_lists():
        if name == e['User_name']:
            print('Vui lòng nhập mật khẩu của bạn.')
            password = input('Nhập mật khẩu: ')
            for i in range(1, 5):
                if password == e['Password']:
                    print(f'Chào {name}, bạn đã đăng nhập thành công!')
                    session_user = e.copy()
                    return True
                else:
                    if i < 4:
                        print('Sai mật khẩu.')
                        password = input(f'Nhập lại mật khẩu (lần {i}/3): ')
                    else:
                        print("Bạn không thể truy cập vào tài khoản!")
    return False


# Form đăng ký tài khoản     
def register():
    print('Tài khoản của bạn không có trong dữ liệu hệ thống.')
    print('Bạn cần đăng ký tài khoản.')
    tmp_user = User()
    while True:
        Not_Exist_2 = False
        tmp_user.user_name = input('Vui lòng nhập tên tài khoản của bạn: ')
        merge_AC_list = merge_Client_Admin_lists()
        for x in merge_AC_list:
            if tmp_user.user_name == x['User_name']:
                Not_Exist_2 = True
                print("Tài khoản này đã tồn tại!")
                break
        if Not_Exist_2 == True:
            continue
        while True:
            tmp_user.password = input('Vui lòng nhập mật khẩu của bạn: ')
            if check_password(tmp_user.password) == False:
                print('Mật khẩu không hợp lệ')
                continue
            password_again = input('Nhập lại mật khẩu của bạn: ')
            if (tmp_user.password == password_again):
                break
            else:
                print("Mật khẩu không giống nhau!")
                continue    
        tmp_user.id = len(merge_AC_list)
        while True :
            tmp_user.name = input("Nhập tên của bạn: ")
            if check_name(tmp_user.name) == False:
                print('Tên không hợp lệ')
                continue
            else:
                break
        while True:
            tmp_user.mail = input("Nhập email của bạn: ")
            if check_email(tmp_user.mail) == False:
                print('Email không hợp lệ')
                continue
            else:
                break
        while True:
            tmp_user.phone_num = input("Nhập số điện thoại của bạn: ")
            if check_phone_number(tmp_user.phone_num) == False:
                print('Số điện thoại không hợp lệ')
                continue
            else:
                break
        while True:
            tmp_user.gender = input(
                "Chọn giới tính của mình (0: Nữ / 1: Nam): ")
            if tmp_user.gender == '0' or tmp_user.gender == '1':
                break
            else:
                print('Lựa chọn giới tính không hợp lệ')
                continue             
        new_full = {"User_name": f"{tmp_user.user_name}","Password": f"{tmp_user.password}", "ID": f"{tmp_user.id + 1}", 
                "Name": f"{tmp_user.name}", "Email": f"{tmp_user.mail}", 
                "Phone_number": f"{tmp_user.phone_num}", "Gender": f"{tmp_user.gender}"}
        save_user_to_json(new_full)
        print('Tài khoản của bạn đã được thêm vào hệ thống!')
        break

# Check xem tài khoản có phải admin hay không
def If_Admin() :
    for x in content["List_Admin"] :
        if x == session_user :
            return True
    return False

# Cấp quyền admin
def set_admin_role () : 
    print("Bạn muốn cấp quyền cho ai?")
    Info_User()
    choice_id = int(input("Nhập STT của người được cấp quyền admin: "))
    while (choice_id <= 0 or choice_id > len(content["List_Client"])) :
        choice_id = int(input("Nhập lại STT của người được cấp quyền admin: "))
        add_admin_to_json(choice_id)
            
def Admin_Site () :
    print("Xin chào quản trị viên!")
    while True :
        print("1. Xem danh sách admin")
        print("2. Xem danh sách khách hàng")
        print("3. Cấp quyền cho tài khoản khách")
        print("0. Thoát")
        choice = int(input("Vui lòng nhập lựa chọn của bạn: "))
        if choice == 1 :
            Info_User("List_Admin")
        elif choice == 2 :
            Info_User("List_Client")
        elif choice == 3 :
            set_admin_role()
        else :
            print("=== Thoát trang quản trị ===")
            break
            
def menu_test() : # Giao diện đăng nhập lúc đầu
    while True :
        print("===== Welcome =====")
        if login_form() == False :
            print("Bạn không có tài khoản bạn có muốn đăng ký không?")
            print("1. Tôi muốn đăng ký")
            print("2. Tôi không muốn đăng ký")
            choice_reg = int(input("Vui lòng nhập lựa chọn :"))
            while choice_reg != 1 and choice_reg != 2 :
                choice_reg = int(input("Vui lòng nhập lại lựa chọn :"))
            if choice_reg == 1:
                register()
            else :
                print("Kết thức chương trình")
                break
        else :
            if If_Admin() :
                Admin_Site()
                print("Bạn có muốn truy cập vào trang mua sắm không?")
                print("1. Truy cập vào trang mua sắm")
                print("2. Thoát chương trình")
                choice_ad = int(input("Nhập lựa chọn của bạn: "))
                while choice_ad != 1 and choice_ad != 2 :
                    choice_ad = int(input("Vui lòng nhập lại lựa chọn :"))
                if choice_ad == 1:
                    print("Tiếp tục trang khách!")
                else :
                    print("Kết thức chương trình")
                    break
            print("Đây là trang mua sắm của chúng tôi")
            break
            # Code từ đây

menu_test()