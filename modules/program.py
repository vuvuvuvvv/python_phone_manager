import modules.system_function as stf
import modules.validate_input as vi
import modules.product as prd
import modules.user as u
import modules.auth as au
import time
import sys


class Program:
    def __init__(self) -> None:
        self.product = prd.Product()
        self.user = u.User()
        self.auth = au.Auth()
        self.list_product = prd.Product().list_product
        self.sorted = False
        self.searched = False

    def run(self):
        stf.clear_screen()
        print(
            "+---------------------------------------------------------------------------+")
        print(
            "|                         WOEOCOĂM TU MAI PHÔN SHOP                         |")
        print(
            "+---------------------------------------------------------------------------+")
        print(
            "|     Để sử dụng dịch vụ của chúng tôi mượt-smà, bạn cần phải đăng nhập     |")
        print(
            "+---------------------------------------------------------------------------+")
        print("Mời lựa chọn: ")
        print("1. Đăng nhập")
        print("2. Đăng ký")
        print("3. Thoát")
        lable = "Vui lòng nhập lựa chọn :"
        select = input(lable)
        select = vi.validate_amout_input_field(select, lable, 1, 3)
        if select == 1:
            user_logged = self.auth.login_form()
            if not user_logged:
                # self.run()
                print('vcl')
            else:
                print(self.auth.session_user)
                # if self.auth.is_admin():
                #     self.admin_menu()
                # else:
                #     self.user_menu()
                # print('deo')
                
        elif select == 2:
            self.auth.register()
        else:
            self.kill_program()


    def product_menu(self):
        self.product.xuat_dien_thoai(list_product=self.list_product, title=(
            "KẾT QUẢ TÌM KIẾM" if self.searched else None))
        if self.searched and len(self.list_product) ==0:
            print("1. Xóa tìm kiếm")
            print("2. Quay lại")
            lable = "Vui lòng nhập lựa chọn : "
            select = input(lable)
            select = vi.validate_amout_input_field(select, lable, 1, 5)
            if select == 1:
                self.list_product = prd.Product().list_product
                self.searched = False
                self.product_menu()
            else:
                self.user_menu()
        else:
            print("Mời lựa chọn dịch vụ: ")
            print("1. Mua ngay")
            print("2. Thêm vào giỏ hàng")
            print(f"3. {'Tìm kiếm sản phẩm' if not self.searched else 'Xóa tìm kiếm'}")
            print(f"4. {'Sắp xếp' if not self.sorted else 'Xóa sắp xếp'}")
            print("5. Quay lại")
            lable = "Vui lòng nhập lựa chọn : "
            select = input(lable)
            select = vi.validate_amout_input_field(select, lable, 1, 5)
            if select == 1:
                self.product.buy_now(list_product=self.list_product)
                self.product_menu()
            elif select == 2:
                self.product.add_to_cart()
                self.product_menu()
            elif select == 3:
                if not self.searched:
                    self.list_product = self.product.find_product_by_condition()
                    self.searched = True
                    self.product_menu()
                else:
                    self.list_product = prd.Product().list_product
                    self.searched = False
                    self.product_menu()
            elif select == 4:
                #TODO
                self.list_product = self.product.sap_xep_danh_sach_dien_thoai()
                self.product_menu()
            else:
                self.user_menu()
        return
            

    def user_menu(self):
        # print(
        #     f"Xin chào {'quản trị viên' if self.auth.is_admin() else 'khách hàng'} {self.auth.session_user['name']}")
        print("Mời lựa chọn dịch vụ: ")
        print("1. Xem sản phẩm")
        print("2. Xem giỏ hàng")
        print("3. Xem đơn hàng của bạn")
        print("4. Chỉnh sửa thông tin tài khoản")
        print("5. Đăng xuất")
        lable = "Vui lòng nhập lựa chọn : "
        select = input(lable)
        select = vi.validate_amout_input_field(select, lable, 1, 5)
        if select == 1:
            self.product_menu()
        elif select == 2:
            self.user_menu()
            pass
        elif select == 3:
            self.user_menu()
            pass
        elif select == 4:
            self.user_menu()
            pass
        else:
            au.Auth().logout()
            self.admin_menu()
        return

    def admin_menu(self):
        print(f"Xin chào quản trị viên {self.auth.session_user['name']}")
        print("Mời lựa chọn dịch vụ: ")
        print("1. Quản lý sản phẩm")
        print("2. Quản lý người dùng")
        print("3. Quản lý đơn hàng")
        print("4. Mua sắm")
        print("5. Chỉnh sửa thông tin tài khoản")
        print("6. Đăng xuất")
        lable = "Vui lòng nhập lựa chọn : "
        select = input(lable)
        select = vi.validate_amout_input_field(select, lable, 1, 6)
        if select == 1:
            pass
        elif select == 2:
            pass
        elif select == 3:
            pass
        elif select == 4:
            pass
        elif select == 5:
            pass
        else:
            self.kill_program()
        return

    def kill_program(self):
        print("-----------------------")
        print("Đếm ngược tự hủy trong:")
        for i in range(4, 0, -1):
            time.sleep(1)
            if i-1 == 0:
                continue
            print(i-1)
        print("BOOOMM BABE!")
        time.sleep(0.5)
        stf.clear_screen()
        sys.exit()
