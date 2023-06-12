
try:
    import json
except ImportError:
    pass
from tabulate import *
from modules.user import *
from modules.data import *
from modules.validate_input import *


class Auth():
    def __init__(self) -> None:
        self.id = None
        self.session_user = {}
        self.dict_user = get_dict_user_from_json()
        self.get_all_user = self.dict_user["list_admin"] + self.dict_user["list_client"]

    # Đẩy 1 user từ "list_client" lên thành admin trong "list_admin" và xóa user đó trong "list_client"
    def add_admin_to_json(self,order_user, filename='./data/client/entries.json'):
        with open(filename, 'w') as file:
            tmp = self.dict_user['list_client'][order_user-1]
            del self.dict_user['list_client'][order_user-1]
            self.dict_user['list_admin'].append(tmp)
            file.seek(0)
            json.dump(self.dict_user, file, indent=4)
        print("Đã cấp quyền admin thành công!")

    # Form đăng nhập tài khoản
    def login_form(self):
        print('Chào mừng đến với trang quản trị')
        print('Vui lòng đăng nhập để truy cập!')
        dict_account = {}
        for user in self.get_all_user:
            dict_account[user['username']] = user['password']

        while True:
            username = input('Nhập tài khoản: ')
            print('Vui lòng nhập mật khẩu của bạn.')
            password = input('Nhập mật khẩu: ')
            try:
                user_password = dict_account[username]
                login_attempt = 0
                while True:
                    if password == user_password:
                        print(f'Đăng nhập thành công!')
                        #Todo...
                        self.session_user = user_password
                        return True
                    else:
                        login_attempt += 1
                        if(login_attempt > 3):
                            print('Dang nhap that bai! Thoat dang nhap.')
                            return False
                        print('Sai mật khẩu.')
                        password = input(f'Nhập lại mật khẩu (lần {login_attempt}/3): ')
            except Exception:
                print("Tai khoan chua duoc dang ky!")
                return False

    # Form đăng ký tài khoản     
    def register(self):
        print('Tài khoản của bạn không có trong dữ liệu hệ thống.')
        print('Bạn cần đăng ký tài khoản.')
        tmp_user = User()
        tmp_user.set_id(len(self.get_all_user) + 1)
        while True:
            Not_Exist_2 = False
            tmp_user.username = input('Vui lòng nhập tên tài khoản của bạn: ')
            for x in self.get_all_user:
                if tmp_user.username == x['username']:
                    Not_Exist_2 = True
                    print("Tài khoản này đã tồn tại!")
                    break
            if Not_Exist_2 == True:
                continue
            while True:
                tmp_user.password = input('Vui lòng nhập mật khẩu của bạn: ')
                if check_password(tmp_user.password):
                    print("Mat khau co it nhat 8 ky tu, bat dau bang chu in hoa va co it nhat 1 ky tu dac biet (@,#,&,_)")
                    continue
                password_again = input('Nhập lại mật khẩu của bạn: ')
                if (tmp_user.password == password_again):
                    break
                else:
                    print("Mật khẩu không giống nhau!")
                    continue    
            while True :
                tmp_user.name = input("Nhập tên của bạn: ")
                if check_name(tmp_user.name):
                    print('Tên không hợp lệ')
                    continue
                else:
                    break
            while True:
                tmp_user.mail = input("Nhập email của bạn: ")
                if check_email(tmp_user.mail):
                    print('Email không hợp lệ')
                    continue
                else:
                    break
            while True:
                tmp_user.phone_num = input("Nhập số điện thoại của bạn: ")
                if check_phone_number(tmp_user.phone_num):
                    print('Số điện thoại không hợp lệ')
                    continue
                else:
                    break
            while True:
                tmp_user.gender = input(
                    "Chọn giới tính của mình (1: Nữ / 2: Nam): ")
                if tmp_user.gender == '1' or tmp_user.gender == '2':
                    break
                else:
                    print('Lựa chọn giới tính không hợp lệ')
                    continue    
            save_product_to_json_file(tmp_user.get_dict_tt_user())
            print('Tài khoản của bạn đã được thêm vào hệ thống!')
            break

    # Check xem tài khoản có phải admin hay không
    def is_admin(self) :
        # for x in self.dict_user["list_admin"] :
        #     if x == self.session_user :
        #         return True
        # return False
        return False

    # Cấp quyền admin
    def set_admin_role (self) : 
        print("Bạn muốn cấp quyền cho ai?")
        self.info_user()
        choice_id = int(input("Nhập STT của người được cấp quyền admin: "))
        while (choice_id <= 0 or choice_id > len(self.dict_user["list_client"])) :
            choice_id = int(input("Nhập lại STT của người được cấp quyền admin: "))
            self.add_admin_to_json(choice_id)
                
    def admin_menu (self) :
        print("Xin chào quản trị viên!")
        while True :
            print("1. Xem danh sách admin")
            print("2. Xem danh sách khách hàng")
            print("3. Cấp quyền cho tài khoản khách")
            print("0. Thoát")
            choice = int(input("Vui lòng nhập lựa chọn của bạn: "))
            if choice == 1 :
                self.info_user("list_admin")
            elif choice == 2 :
                self.info_user("list_client")
            elif choice == 3 :
                self.set_admin_role()
            else :
                print("=== Thoát trang quản trị ===")
                break
                
    def auth_run(self) : # Giao diện đăng nhập lúc đầu
        while True :
            print("===== Welcome =====")
            if self.login_form() :
                print("Bạn không có tài khoản bạn có muốn đăng ký không?")
                print("1. Tôi muốn đăng ký")
                print("2. Tôi không muốn đăng ký")
                choice_reg = int(input("Vui lòng nhập lựa chọn :"))
                while choice_reg != 1 and choice_reg != 2 :
                    choice_reg = int(input("Vui lòng nhập lại lựa chọn :"))
                if choice_reg == 1:
                    self.register()
                else :
                    print("Kết thức chương trình")
                    break
            else :
                if self.is_admin() :
                    self.admin_menu()
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
