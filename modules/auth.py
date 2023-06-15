from tabulate import *
import modules.user as auth_user 
import modules.data as auth_data
import modules.validate_input as au_vi
import modules.system_function as stf
from datetime import *
import modules.program as auth_program
import time
class Auth:
    def __init__(self) -> None:
        self.id = None

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
                try:
                    user_password = dict_account[username]
                except Exception:
                    print("Tài khoản chưa được đăng ký!")
                    print("1. Đăng ký")
                    print("2. Đăng nhập lại")
                    print("3. Thoát")
                    lable = "Vui lòng nhập lựa chọn : "
                    select = input(lable)
                    select = au_vi.validate_amout_input_field(select, lable, 1, 3)
                    if select == 1:
                        self.register()
                    if select == 2:
                        stf.clear_screen()
                        continue
                    else:
                        return False

                password = input('Nhập mật khẩu: ')
                login_attempt = 0
                while True:
                    if password == user_password:
                        auth_data.save_session_to_json(auth_user.User().find_user_by_id_or_username(str(username)))
                        return True
                    else:
                        login_attempt += 1
                        if(login_attempt > 3):
                            print('Đăng nhập thất bại! Thoát đăng nhập.')
                            return False
                        print('Sai mật khẩu.')
                        password = input(f'Nhập lại mật khẩu (lần {login_attempt}/3): ')
        else:
            auth_data.save_session_to_json(dict_user)

    # Form đăng ký tài khoản     
    def register(self):
        tmp_user = auth_user.User()
        tmp_user.set_id(len(auth_data.get_dict_user_from_json()["list_admin"] + auth_data.get_dict_user_from_json()["list_client"]) + 1)
        while True:
            is_username_exists = False
            tmp_user.username = input('Nhập tên đăng nhập: ')
            if au_vi.check_username(tmp_user.username):
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
            if not au_vi.check_password(tmp_password):
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
            if not au_vi.check_name(tmp_user.name):
                print('Tên không hợp lệ')
                continue
            else:
                break
        while True:
            tmp_user.mail = input("Nhập email: ")
            if not au_vi.check_email(tmp_user.mail):
                print('Email không hợp lệ')
                continue
            else:
                break
        while True:
            tmp_user.phone_num = input("Nhập số điện thoại: ")
            if not au_vi.check_phone_number(tmp_user.phone_num):
                print('Số điện thoại phải có 10 chữ số bắt đầu bằng 0 hoặc 84')
                continue
            else:
                break
        lable = "Giới tính (1: Nữ / 2: Nam): "
        tmp_user.gender = input(lable)
        tmp_user.gender = au_vi.validate_amout_input_field(tmp_user.gender,lable,1,2)  

        tmp_user.ngay_khoi_tao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        auth_data.save_product_to_json_file(tmp_user.get_dict_tt_user())
        print('Đăng ký thành công!')
        self.login_form(tmp_user.get_dict_tt_user())

    # Check xem tài khoản có phải admin hay không
    def is_admin(self):
        for x in auth_data.get_dict_user_from_json()["list_admin"] :
            if x == auth_data.get_session() :
                return True
        return False
                
    def logout(self):
        program = auth_program.Program()
        auth_data.delete_session()
        program.run()