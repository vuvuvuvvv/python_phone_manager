from tabulate import *
import modules.user as auth_user 
import modules.data as auth_data
from modules.validate_input import *
import modules.system_function as stf
from datetime import *
import modules.program as auth_program

class Auth:
    def __init__(self) -> None:
        self.id = None
        self.session_user = None
        self.session_msg = None
        #TEST
        # self.session_user = auth_user.User().find_user_by_id_or_username(2)
        #END TEST

    # Form đăng nhập tài khoản
    def login_form(self, dict_user = None):
        stf.clear_screen()
        if dict_user is None:
            print('Vui lòng đăng nhập để truy cập!')
            dict_account = {}
            for user in auth_data.get_dict_user_from_json()["list_admin"] + auth_data.get_dict_user_from_json()["list_client"]:
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
                                print('Đăng nhập thất bại! Thoát đăng nhập.')
                                return False
                            print('Sai mật khẩu.')
                            password = input(f'Nhập lại mật khẩu (lần {login_attempt}/3): ')
                except Exception:
                    print("Tài khoản chưa được đăng ký!")
                    return False
        else:
            self.session_user = dict_user

    # Form đăng ký tài khoản     
    def register(self):
        tmp_user = auth_user.User()
        tmp_user.set_id(len(auth_data.get_dict_user_from_json()["list_admin"] + auth_data.get_dict_user_from_json()["list_client"]) + 1)
        while True:
            is_username_exists = False
            tmp_user.username = input('Nhập tên đăng nhập: ')
            if check_username(tmp_user.username):
                for x in (auth_data.get_dict_user_from_json()["list_admin"] + auth_data.get_dict_user_from_json()["list_client"]):
                    if tmp_user.username == x['username']:
                        is_username_exists = True
                        print("Tên đăng nhập đã được sử dụng!")
                        break
                if is_username_exists == True:
                    continue
                else:
                    break
            else:
                print("Tên đăng nhập phải có 8 ký tự bao gồm chữ thường, chữ in hoa hoặc chữ số")
                continue
        while True:
            tmp_password = input('Vui lòng nhập mật khẩu: ')
            if not check_password(tmp_password):
                print("Mật khẩu có ít nhất 8 ký tự, bắt đầu bằng chữ in hoa")
                continue
            else:
                break
        while True:
            password_again = input('Nhập lại mật khẩu: ')
            if (tmp_password == password_again):
                tmp_user.password = tmp_password
                break
            else:
                print("Mật khẩu không giống!")
                continue 

        while True :
            tmp_user.name = input("Nhập họ tên: ")
            if not check_name(tmp_user.name):
                print('Tên không hợp lệ')
                continue
            else:
                break
        while True:
            tmp_user.mail = input("Nhập email: ")
            if not check_email(tmp_user.mail):
                print('Email không hợp lệ')
                continue
            else:
                break
        while True:
            tmp_user.phone_num = input("Nhập số điện thoại: ")
            if not check_phone_number(tmp_user.phone_num):
                print('Số điện thoại phải có 10 chữ số bắt đầu bằng 0 hoặc 84')
                continue
            else:
                break
        lable = "Giới tính (1: Nữ / 2: Nam): "
        tmp_user.gender = input(lable)
        tmp_user.gender = validate_amout_input_field(tmp_user.gender,lable,1,2)  

        tmp_user.ngay_khoi_tao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        auth_data.save_product_to_json_file(tmp_user.get_dict_tt_user())
        print('Đăng ký thành công!')
        self.login_form(tmp_user.get_dict_tt_user())

    # Check xem tài khoản có phải admin hay không
    def is_admin(self):
        if self.session_user is not None:
            for x in auth_data.get_dict_user_from_json()["list_admin"] :
                if x == self.session_user :
                    return True
        return False
                
    def logout(self):
        program = auth_program.Program()
        self.session_user = None
        program.run()