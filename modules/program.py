import modules.system_function as stf
import modules.validate_input as vi
import modules.product as prd
import modules.cart as crt
import modules.order as od
import modules.checkout as cout
import modules.user as u
import modules.auth as au
import modules.data as dta
import time
import sys


class Program:
    def __init__(self) -> None:
        self.product = prd.Product()
        self.user = u.User()
        self.auth = au.Auth()
        self.cart = crt.Cart()
        self.order = od.Order()
        self.checkout = cout.Checkout()
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
        lable = "Vui lòng nhập lựa chọn: "
        select = input(lable)
        select = vi.validate_amout_input_field(select, lable, 1, 3)
        if select == 1:
            user_logged = self.auth.login_form()
            if user_logged:
                print('Đợi xíuu...')
                time.sleep(1)
                print(f'Đăng nhập thành công!')
                time.sleep(0.7)
                if self.auth.is_admin():
                    self.admin_menu()
                else:
                    self.user_menu()
        elif select == 2:
            self.auth.register()
        else:
            self.kill_program()
        return

    def product_menu(self):
        self.product.xuat_dien_thoai(list_product=self.list_product, title=(
            "KẾT QUẢ TÌM KIẾM" if self.searched else "DANH SACH SẢN PHẨM"))
        if self.searched and len(self.list_product) ==0:
            print("1. Xóa tìm kiếm")
            print("2. Quay lại")
            lable = "Vui lòng nhập lựa chọn : "
            select = input(lable)
            select = vi.validate_amout_input_field(select, lable, 1, 2)
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
            print(f"4. Sắp xếp")
            print("5. Quay lại")
            if self.sorted:
                print("5. Xóa sắp xếp")
                print("6. Quay lại")
            lable = "Vui lòng nhập lựa chọn : "
            select = input(lable)
            select = vi.validate_amout_input_field(select, lable, 1, (6 if self.sorted else 5))
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
                self.list_product = self.product.sap_xep_danh_sach_dien_thoai(list_product=(self.list_product if self.sorted else None))
                self.sorted = True
                self.product_menu()
            elif select == (6 if self.sorted else 5):
                self.user_menu()
            else:
                self.list_product = prd.Product().list_product
                self.sorted = False
                self.product_menu()
        return
                
    def user_menu(self):
        stf.clear_screen()
        print(
            f"Xin chào {'quản trị viên' if self.auth.is_admin() else 'khách hàng'} {dta.get_session()['name']}")
        print("Mời lựa chọn dịch vụ: ")
        print("1. Xem sản phẩm")
        print("2. Xem giỏ hàng")
        print("3. Xem đơn hàng của bạn")
        print("4. Chỉnh sửa thông tin cá nhân")
        print("5. Đăng xuất")
        lable = "Vui lòng nhập lựa chọn : "
        select = input(lable)
        select = vi.validate_amout_input_field(select, lable, 1, 5)
        if select == 1:
            self.product_menu()
        elif select == 2:
            get_cart = dta.get_cart_item_from_json()
            self.cart.show_cart(cart=get_cart)
            if len(get_cart) > 0:
                print("1. Thanh toán giỏ hàng")
                print("2. Quay lại")
                lable = "Vui lòng nhập lựa chọn : "
                select = input(lable)
                select = vi.validate_amout_input_field(select, lable, 1, 2)
                if select == 1:
                    self.checkout.checkout(get_cart)
                    self.user_menu()
                if select == 2:
                    self.user_menu()
            else:           
                print("1. Quay lại")
                lable = "Vui lòng nhập lựa chọn : "
                select = input(lable)
                select = vi.validate_amout_input_field(select, lable, 1, 1)
                if select == 1:
                    self.user_menu()
        elif select == 3:
            self.order.show_order()
            print("1. Quay lại")
            lable = "Vui lòng nhập lựa chọn : "
            select = input(lable)
            select = vi.validate_amout_input_field(select, lable, 1, 1)
            if select == 1:
                self.list_product = prd.Product().list_product
                self.searched = False
                self.user_menu()
        elif select == 4:
            self.user.edit_user(user=dta.get_session())
            self.user_menu()
        else:
            au.Auth().logout()
            self.admin_menu()
        return

    def product_management_menu(self):
        stf.clear_screen()
        self.product.xuat_dien_thoai()
        print("Mời lựa chọn dịch vụ: ")
        print("1. Thếm sản phẩm")
        print("2. Xóa sản phẩm")
        print(f"3. Chỉnh sửa thông tin sản phẩm")
        print("4. Quay lại")
        lable = "Vui lòng nhập lựa chọn : "
        select = input(lable)
        select = vi.validate_amout_input_field(select, lable, 1, 4)
        if select == 1:
            self.product.nhap_dien_thoai()
            self.product_management_menu()
        elif select == 2:
            self.product.xoa_dien_thoai()
            self.product_management_menu()
        elif select == 3:
            self.product.edit_product()
            self.product_management_menu()
        else:
            self.admin_menu()
        #Search & sort product: coming soon!
        return

    def order_managerment_menu(self):
        stf.clear_screen()
        self.product.xuat_dien_thoai()
        print("Mời lựa chọn dịch vụ: ")
        #Coming soon
        # print("1. Chỉnh trạng thái đơn hàng")
        print("1. Quay lại")
        lable = "Vui lòng nhập lựa chọn : "
        select = input(lable)
        select = vi.validate_amout_input_field(select, lable, 1, 1)
        if select == 1:
            self.product_management_menu()

    def user_managerment_menu(self):
        stf.clear_screen()
        self.user.xuat_tt_all_user()
        print("Mời lựa chọn dịch vụ: ")
        print("1. Chỉnh sửa thông tin người dùng")
        print("2. Xóa người dùng")
        print("3. Quay lại")
        lable = "Vui lòng nhập lựa chọn : "
        select = input(lable)
        select = vi.validate_amout_input_field(select, lable, 1, 3)
        if select == 1:
            self.user.edit_user()
            self.user_managerment_menu()
        elif select == 2:
            self.user.delete_user()
            self.user_managerment_menu()
        else:
            self.admin_menu()
        #Search & sort & add user: coming soon!
        return

    def admin_menu(self):
        stf.clear_screen()
        print(f"Xin chào quản trị viên {dta.get_session()['name']}")
        print("Mời lựa chọn dịch vụ: ")
        print("1. Quản lý sản phẩm")
        print("2. Quản lý người dùng")
        print("3. Quản lý đơn hàng")
        print("4. Mua sắm")
        print("5. Đăng xuất")
        lable = "Vui lòng nhập lựa chọn : "
        select = input(lable)
        select = vi.validate_amout_input_field(select, lable, 1, 6)
        if select == 1:
            self.product_management_menu()
        elif select == 2:
            self.order_managerment_menu()
        elif select == 3:
            self.user_managerment_menu()
        elif select == 4:
            self.user_menu()
        else:
            au.Auth().logout()
            self.run()
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
