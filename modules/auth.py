
try:
    import json
    from tabulate import *
    from modules.user import *
    from modules.data import *
    from modules.validate_input import *
    from datetime import *
except ImportError:
    pass


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
    def login_form(self, dict_user = None):
        if dict_user is None:
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
        else:
            self.session_user = dict_user

    # Form đăng ký tài khoản     
    def register(self):
        tmp_user = User()
        tmp_user.set_id(len(self.get_all_user) + 1)
        while True:
            is_username_exists = False
            tmp_user.username = input('Nhap ten dang nhap: ')
            if check_username(tmp_user.username):
                for x in self.get_all_user:
                    if tmp_user.username == x['username']:
                        is_username_exists = True
                        print("Ten dang nhap da duoc su dung!")
                        break
                if is_username_exists == True:
                    continue
                else:
                    break
            else:
                print("Ten dang nhap co it nhat 8 ky tu bao gom chu in hoa, chu thuong va so")
                continue

        while True:
            tmp_password = input('Vui long nhap mat khau: ')
            if not check_password(tmp_password):
                print("Mat khau co it nhat 8 ky tu, bat dau bang chu in hoa")
                continue
            else:
                break
        while True:
            password_again = input('Nhap lai mat khau: ')
            if (tmp_password == password_again):
                tmp_user.password = tmp_password
                break
            else:
                print("Mat khau khong giong nhau!")
                continue 

        while True :
            tmp_user.name = input("Nhap ho ten: ")
            if not check_name(tmp_user.name):
                print('Ten khong hop le')
                continue
            else:
                break
        while True:
            tmp_user.mail = input("Nhap email: ")
            if not check_email(tmp_user.mail):
                print('Email Khong hop le')
                continue
            else:
                break
        while True:
            tmp_user.phone_num = input("Nhap so dien thoai: ")
            if not check_phone_number(tmp_user.phone_num):
                print('So dien thoai khong hop le')
                continue
            else:
                break
        lable = "Gioi tinh (1: Nu / 2: Nam): "
        tmp_user.gender = input(lable)
        tmp_user.gender = checkSelect([1,2])  

        tmp_user.ngay_khoi_tao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_product_to_json_file(tmp_user.get_dict_tt_user())
        print('Tai khoan da duoc them vao he thong!')
        self.login_form(tmp_user.get_dict_tt_user())

    # Check xem tài khoản có phải admin hay không
    def is_admin(self) :
        for x in self.dict_user["list_admin"] :
            if x == self.session_user :
                return True
        return False
                
    def admin_menu (self) :
        print(f"Xin chao QTV {self.session_user['name']}!")
        while True :
            print("1. Quan ly nguoi dung")
            print("2. Quan ly san pham")
            print("3. Quan ly don hang")
            # print("1. Danh sach nguoi dung")
            # print("2. Them nguoi dung")
            # print("3. Xoa nguoi dung")
            # print("---------------------------------")
            # print("5. Danh sach san pham")
            # print("6. Them san pham")
            # print("7. Xoa san pham")
            # print("---------------------------------")
            # print("8. Don hang")
            print("0. Dang xuat ")
            choice = int(input("Nhap lua chon: "))
            if choice == 1 :
                self.info_user("list_admin")
            elif choice == 2 :
                self.info_user("list_client")
            elif choice == 3 :
                self.set_admin_role()
            else :
                print("=== Thoat ===")
                break
                
    def auth_run(self) : # Giao diện đăng nhập lúc đầu
        while True :
            print("===== Welcome =====")
            if self.login_form() :
                print("Bạn không có tài khoản bạn có muốn đăng ký không?")
                print("1. Tôi muốn đăng ký")
                print("2. Tôi không muốn đăng ký")
                choice_reg = int(input("Vui lòng nhập lựa chọn :"))
                choice_reg = checkSelect([1,3])
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
