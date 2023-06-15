import copy
import json
from datetime import *
import modules.data as prd_data
import modules.cart as prd_cart
import modules.auth as prd_auth
import modules.dien_thoai as prd_dt
import modules.system_function as stf
import modules.validate_input as vi
import modules.checkout as prd_checkout
from tabulate import tabulate
import sys

status = {
    0: "Không hoạt động",
    1: "Hoạt động"
}

class Product:
    def __init__(self) -> None:
        self.list_product = prd_data.get_dict_product_from_json()

    def nhap_dien_thoai(self) -> None:
        # Nhap so san pham
        print('----------------------------')
        lable_input = "Số lượng điện thoại muốn nhập vào kho: "
        sl_dienthoai = input(lable_input)

        #Clear screen
        stf.clear_screen()

        sl_dienthoai = vi.validate_amout_input_field(sl_dienthoai,lable_input,1,100)
        # Nhap thong tin san pham
        print('----------------------------')
        print('NHẬP THÔNG TIN CHO ĐIỆN THOẠI:')
        for i in range(0, sl_dienthoai):
            #Khoi tao dienthoai
            dienthoai = prd_dt.DienThoai()
            print(f'Sản phẩm thứ {i + 1 if i > 0 else "nhất"}:')
            #Nhap ten
            tmp_ten = input("Nhập tên: ")
            while len(tmp_ten) <= 0 or len(tmp_ten) > 100:
                print("Tên không được để trống và không được quá 100 ký tự!")
                tmp_ten = input("Nhập tên sản phẩm: ")
            #Nhap hang san xuat
            tmp_hang = input("Nhập tên hãng sản xuất: ")
            while len(tmp_hang) <= 0 or len(tmp_hang) > 100:
                print("Tên không được để trống và không được quá 100 ký tự!")
                tmp_hang = input("Nhập tên hãng: ")

            dienthoai.set_ten(tmp_ten)
            dienthoai.set_hang(tmp_hang)

            #Clear screen
            stf.clear_screen()
            #
            # Khoi tao vong lap lap theo so loai dung luong, moi loai dung luong co 1 hoac nhieu loai ram khac nhau
            # Moi 1 loai dien thoai co dung luong va RAM lai co 1 muc gia va so luong khac
            #
            #Nhap so loai dung luong
            print('----------------------------')
            print("NHẬP DUNG LƯỢNG CHO:")
            print(str(dienthoai))
            print('----------------------------')
            lable_input = "Số loại dung lượng: "
            so_dung_luong = input(lable_input)
            so_dung_luong = vi.validate_amout_input_field(so_dung_luong, lable_input)
            list_dung_luong = [] #Khoi tao mang dung luong cho du lieu dien thoai hien tai = []
            for j in range(0, so_dung_luong):
                #
                # Khoi tao 1 ban sao cua dienthoai de lay du lieu id, ten va hang
                # Sau khi khoi tao va hoan thien thong tin => save vao ds_dien_thoai & del
                # dienthoai sau khi luu
                #
                bansao_dt = copy.deepcopy(dienthoai)
                bansao_dt.id = ( (int(sorted(prd_data.get_dict_product_from_json(),key=lambda x:x['id'],reverse=True)[0]['id'])+1) if len(prd_data.get_dict_product_from_json()) > 0 else 1)
                #Nhap dung luong
                print('----------------------------')
                print(f'Nhập loại dung lượng thứ {"nhất" if j == 0 else j+1} cho: ')
                print(str(bansao_dt))
                print('----------------------------')
                lable_input = "Nhập dung lượng (GB): "
                tmp_dung_luong = input(lable_input)
                tmp_dung_luong = vi.validate_amout_input_field(tmp_dung_luong, lable_input)
                while True:
                    if tmp_dung_luong in list_dung_luong:
                        print(f"Dung lượng {tmp_dung_luong}GB đã có sẵn cho sản phẩm hiện nhập!")
                        tmp_dung_luong = input(lable_input)
                        tmp_dung_luong = vi.validate_amout_input_field(tmp_dung_luong, lable_input)
                    else:
                        bansao_dt.set_dung_luong(tmp_dung_luong)
                        list_dung_luong.append(tmp_dung_luong)
                        break
            
                #Clear screen
                stf.clear_screen()

                #Nhap so loai RAM cho loai dien thoai co dung luong vua nhap
                print('----------------------------')
                print("NHẬP RAM ĐIỆN THOẠI CHO:")
                print(str(bansao_dt))
                print('----------------------------')
                lable_input = "Nhập RAM (GB): "
                tmp_ram = input(lable_input)
                tmp_ram = vi.validate_amout_input_field(tmp_ram, lable_input)
                bansao_dt.set_ram(tmp_ram)

                #Clear screen
                stf.clear_screen()

                #Hoan thien gia ban, so luong, nam san xuat cho dien thoai 
                print('----------------------------')
                print('HOÀN THIỆN THÔNG TIN CHO: ')
                print(str(bansao_dt))
                #Gia ban
                lable_input = "Giá bán (VND): "
                tmp_gia = input(lable_input)
                tmp_gia = vi.validate_amout_input_field(tmp_gia, lable_input,1000000)
                bansao_dt.set_gia(tmp_gia)
                #So luong
                lable_input = "Số lượng: "
                tmp_so_luong = input(lable_input)
                tmp_so_luong = vi.validate_amout_input_field(tmp_so_luong, lable_input)
                bansao_dt.set_so_luong(tmp_so_luong)
                #Nam san xuat
                lable_input = "Năm sản xuất: "
                tmp_nam_sxuat = input(lable_input)
                tmp_nam_sxuat = vi.validate_amout_input_field(tmp_nam_sxuat, lable_input,1900, datetime.now().year)
                bansao_dt.set_nam_sxuat(tmp_nam_sxuat)
                #Save
                prd_data.save_product_to_json_file(bansao_dt.get_dict_thongtin_dienthoai())
                #Clear screen
                stf.clear_screen()
                del bansao_dt
            #Xoa dien thoai
            del dienthoai

    def xuat_dien_thoai(self,title = "DANH SÁCH SẢN PHẨM", list_product = None) -> None:
        if list_product is None or len(list_product) != 0:
            auth = prd_auth.Auth()
            if list_product is None:
                list_product = prd_data.get_dict_product_from_json()
            data = []
            header = ['STT','Tên sản phẩm','Hãng sản xuất','Dung lượng','RAM','Giá bán','Số lượng','Năm sản xuất']
            # Neu la Admin thi hien thi ca san pham khong con hoat dong va trang thai cua tat ca san pham
            if auth.is_admin():
                header.append('Trạng thái')
            i = 1
            for dienthoai in list_product:
                row = [
                    i,
                    f"{dienthoai['ten']} {dienthoai['dung_luong']} GB",
                    f"{dienthoai['hang']}",
                    f"{dienthoai['dung_luong']} GB",
                    f"{dienthoai['ram']} GB",
                    f"{format(dienthoai['gia'], ',d').replace(',', '.')}VND",
                    f"{dienthoai['so_luong']}",
                    f"{dienthoai['nam_sxuat']}"
                ]
                i+= 1
                if auth.is_admin():
                    row.append(f"{status[dienthoai['status']]}")
                    data.append(row)
                else:
                    if dienthoai['status'] == 1:
                        data.append(row)
            table = tabulate(data, header, tablefmt="fancy_grid")
            stf.clear_screen()
            print(title)
            print(table)
        else:
            stf.clear_screen()
            print("+-----------------------------+")
            print("| Không có sản phẩm hiển thị! |")
            print("+-----------------------------+")


    def xoa_dien_thoai(self) -> None:
        stf.clear_screen()
        self.xuat_dien_thoai()
        if len(prd_data.get_dict_product_from_json()) == 0:
            print("Danh sách điện thoại rỗng!")
        else:
            lable = 'Nhập STT điện thoai muốn xóa:'
            order_phone = input(lable)
            order_phone = vi.validate_amout_input_field(order_phone,lable,max=len(prd_data.get_dict_product_from_json()))
            with open('./data/product/product.json', 'r') as file:
                data = json.load(file)
            data['products'].pop(order_phone -1)
            with open('./data/product/product.json', 'w') as file:
                json.dump(data, file, indent=4)

    def buy_now(self,list_product = None):
        cart = prd_cart.Cart()
        checkout = prd_checkout.Checkout()
        if list_product is None:
            list_product = prd_data.get_dict_product_from_json()
        self.xuat_dien_thoai(list_product=list_product)
        lable = "Chọn sản phẩm bạn muốn mua: "
        select = input(lable)
        select = vi.validate_amout_input_field(select,lable,1,len(list_product))
        #Tìm ra sản phẩm được chọn
        selected_product = list_product[select - 1]
        #In ra màn hình sản phẩm mua
        self.xuat_dien_thoai(title="THÔNG TIN SẢN PHẨM MUA:",list_product=[selected_product])
        lable = "Số lượng mua: "
        quantity = input(lable)
        quantity = vi.validate_amout_input_field(quantity,lable,1,selected_product['so_luong'])
        #Tạo nhanh 1 đơn trong giỏ hàng và tạo thành đơn hàng

        cart.product = selected_product
        cart.quantity = quantity
        checkout.checkout([cart.get_cart_item()])

    #Find by name
    def find_product_by_condition(self) -> dict:
        stf.clear_screen()
        self.xuat_dien_thoai()
        list_product = []
        #Find by product name
        lable_properties = ['Tên sản phẩm','Hãng sản xuất','Dung lượng','RAM','Năm sản xuất']
        properties = ['ten','hang','dung_luong','ram','nam_sxuat']
        print("Chọn mục bạn muốn tìm kiếm! ")
        print("Tìm kiếm sản phẩm theo: ")
        for i in range (1, len(lable_properties) +1):
            print(f"{i}. {lable_properties[i-1]}")
        lable = "Chọn: "
        select = input(lable)
        select = vi.validate_amout_input_field(select,lable= lable,max=len(lable_properties))
        property = properties[select - 1]
        get_all_product = sorted(prd_data.get_dict_product_from_json(),key=lambda x: x[property])

        if property in ["ten",'hang']:
            lable = f"{lable_properties[select-1]} bạn muốn tìm: "
            value = str(input(lable))
            value = value.lower().strip()
        else:
            lable = f"{lable_properties[select-1]} bạn muốn tìm: "
            value = input(lable)
            value = vi.validate_amout_input_field(value,lable)
                
        for item in get_all_product:
            if property == "ten":
                #Lower case va be nho ten san pham de so sanh
                pr_name = item["ten"].lower().strip()
                #Kiem tra tu khoa tim kiem
                #Co 2 tu tro len: -> Be nho de so sanh va tim kiem
                if " " in value:
                    keywords = value.split(" ")
                    #Lap theo tung tu co trong keyword
                    for letter in keywords:
                        #Neu co trong ten san pham => Add vao list
                        if str(letter) in pr_name:
                            #Check trung san pham
                            if item not in list_product:
                                list_product.append(item)
                else:
                    if value in pr_name:
                        if item not in list_product:
                            list_product.append(item)
            #Find by other property (Hang, nam san xuat,...)
            elif property == 'hang':
                if value in item[property].lower().strip():
                    if item not in list_product:
                        list_product.append(item)
            else:
                if value == item[property]:
                    if item not in list_product:
                        list_product.append(item)
        return list_product
    
    def find_product_by_id(self, id) -> dict:
        get_all_product = prd_data.get_dict_product_from_json()
        for item in get_all_product:
            if id == item['id']:
                return item
        return None

    #No return
    def sap_xep_danh_sach_dien_thoai(self,list_product = None) -> None:
        self.xuat_dien_thoai(list_product=(list_product if list_product is not None else None))
        lable_properties = ['Tên sản phẩm','Hãng sản xuất','Dung lượng','RAM','Giá bán','Số lượng','Năm sản xuất','Thời gian đăng bán']
        properties = ['ten','hang','dung_luong','ram','gia','so_luong','nam_sxuat','ngay_khoi_tao']
        print("Chọn mục bạn muốn sắp xếp: ")
        for i in range (1, len(lable_properties) +1):
            print(f"{i}. {lable_properties[i-1]}")
        lable = "Chọn: "
        select = input(lable)
        select = vi.validate_amout_input_field(select,lable= lable,max=len(lable_properties))
        property = properties[select - 1]
        self.xuat_dien_thoai(list_product=(list_product if list_product is not None else None))
        print("Sắp xếp theo: ")
        if property in ['nam_sxuat','ngay_khoi_tao']:
            print('1. Cũ nhất')
            print('2. Mới nhất')
        elif property in ['ten','hang']:
            print('1. Từ a-z')
            print('2. Từ z-a')
        else:
            print('1. Tăng dần')
            print('2. Giảm dần')
        lable = "Chọn: "
        select = input(lable)
        select = vi.validate_amout_input_field(select,lable,1,2)
        return sorted(prd_data.get_dict_product_from_json(),key=lambda x: x[property], reverse=(True if select ==2 else False))
    
    def add_to_cart(self, list_product = None) -> None:
        stf.clear_screen()
        cart = prd_cart.Cart()
        dienthoai = prd_dt.DienThoai()
        if list_product is None:
            list_product = prd_data.get_dict_product_from_json()
        self.xuat_dien_thoai(list_product=list_product)
        lable = "Chọn sản phẩm thêm vào giỏ: "
        select = input(lable)
        select = vi.validate_amout_input_field(select,lable,1,len(list_product))
        uid = prd_data.get_session()['id']
        current_cart = prd_data.get_cart_item_from_json()
        product_selected = list_product[select - 1]
        cartitem = cart.find_cart_item_in_cart_by_product(product_selected)
        print("-------------------------------")
        total_quantity = product_selected['so_luong']
        if cartitem is not None:
            total_quantity = product_selected['so_luong'] - cartitem['quantity']
            print(f"Sản phẩm hiện đã có sẵn trong giỏ hàng, bạn chỉ có thể thêm tối đa {format(total_quantity, ',d').replace(',', '.')} sản phẩm.")
        print(dienthoai.show_tt_dt(product_selected))
        print("-------------------------------")
        lable = "Nhập số lượng sản phẩm muốn thêm: "
        quantity = input(lable)
        quantity = vi.validate_amout_input_field(quantity,lable,1,total_quantity)

        cart.user_id = uid
        cart.product = product_selected
        cart.quantity = quantity
        produc_is_exists_in_cart = False
        for item in current_cart:
            if item["product"] == product_selected:
                cart.quantity += item['quantity']
                produc_is_exists_in_cart = True
                prd_data.update_cart_item_to_json_file(cart.get_cart_item())
                break
        if not produc_is_exists_in_cart:
            prd_data.save_cart_item_to_json_file(cart.get_cart_item())
        stf.clear_screen()
        cart.show_cart()
        return

    def edit_product(self, list_product = None) -> None:
        if list_product is None:
            list_product = prd_data.get_dict_product_from_json()
        self.xuat_dien_thoai()
        print("Chọn STT sản phẩm muốn sửa:")
        lable = "Chọn: "
        select = input(lable)
        select = vi.validate_amout_input_field(select,lable= lable,max=len(list_product))
        index = select - 1
        edited_product = list_product[index]
        stf.clear_screen()
        self.xuat_dien_thoai(title="THÔNG TIN SẢN PHẨM SỬA",list_product=[edited_product])
        lable_properties = ['Tên sản phẩm','Hãng sản xuất','Dung lượng','RAM','Giá bán','Số lượng','Năm sản xuất',"Trạng thái","Tất cả"]
        properties = ['ten','hang','dung_luong','ram','gia','so_luong','nam_sxuat',"status",None]
        print("Chọn mục bạn muốn sửa: ")
        for i in range (1, len(lable_properties) +1):
            print(f"{i}. {lable_properties[i-1]}")
        lable = "Chọn: "
        select = input(lable)
        select = vi.validate_amout_input_field(select,lable= lable,max=len(lable_properties))

        property = properties[select - 1]

        if property is None:
            tmp_ten = input("Nhập tên: ")
            while len(tmp_ten) <= 0 or len(tmp_ten) > 100:
                print("Tên không được để trống và không được quá 100 ký tự!")
                tmp_ten = input("Nhập tên sản phẩm: ")
                
            tmp_hang = input("Nhập tên hãng sản xuất: ")
            while len(tmp_hang) <= 0 or len(tmp_hang) > 100:
                print("Tên không được để trống và không được quá 100 ký tự!")
                tmp_hang = input("Nhập tên hãng: ")
            lable_input = "Nhập dung lượng (GB): "
            tmp_dung_luong = input(lable_input)
            tmp_dung_luong = vi.validate_amout_input_field(tmp_dung_luong, lable_input)
            lable_input = "Nhập RAM (GB): "
            tmp_ram = input(lable_input)
            tmp_ram = vi.validate_amout_input_field(tmp_ram, lable_input)
            lable_input = "Giá bán (VND): "
            tmp_gia = input(lable_input)
            tmp_gia = vi.validate_amout_input_field(tmp_gia, lable_input,1000000)
            lable_input = "Số lượng: "
            tmp_so_luong = input(lable_input)
            tmp_so_luong = vi.validate_amout_input_field(tmp_so_luong, lable_input)
            lable_input = "Năm sản xuất: "
            tmp_nam_sxuat = input(lable_input)
            tmp_nam_sxuat = vi.validate_amout_input_field(tmp_nam_sxuat, lable_input,1900, datetime.now().year)
            lable_input = "Trạng thái (0: Không hoạt động | 1: Hoạt động):"
            tmp_status = input(lable_input)
            tmp_status = vi.validate_amout_input_field(tmp_status, lable_input,0,1)
            tmp = [tmp_ten,tmp_hang,tmp_dung_luong,tmp_ram,tmp_gia,tmp_so_luong,tmp_nam_sxuat,tmp_status]
            for field, item in zip(tmp,properties):
                edited_product[item] = field
        elif property == 'ten':
            edited_product[property] = input("Nhập tên: ")
            while len(edited_product[property]) <= 0 or len(edited_product[property]) > 100:
                print("Tên không được để trống và không được quá 100 ký tự!")
                edited_product[property] = input("Nhập tên sản phẩm: ")
        elif property == 'hang':
            edited_product[property] = input("Nhập tên hãng sản xuất: ")
            while len(edited_product[property]) <= 0 or len(edited_product[property]) > 100:
                print("Tên không được để trống và không được quá 100 ký tự!")
                edited_product[property] = input("Nhập tên hãng: ")
        elif property == 'dung_luong':
            lable_input = "Nhập dung lượng (GB): "
            edited_product[property] = input(lable_input)
            edited_product[property] = vi.validate_amout_input_field(edited_product[property], lable_input)
             
        elif property == 'ram':
            lable_input = "Nhập RAM (GB): "
            edited_product[property] = input(lable_input)
            edited_product[property] = vi.validate_amout_input_field(edited_product[property], lable_input)
        elif property == 'gia':
            lable_input = "Giá bán (VND): "
            edited_product[property] = input(lable_input)
            edited_product[property] = vi.validate_amout_input_field(edited_product[property], lable_input,1000000)
        elif property == 'so_luong':
            lable_input = "Số lượng: "
            edited_product[property] = input(lable_input)
            edited_product[property] = vi.validate_amout_input_field(edited_product[property], lable_input)
        elif property == 'nam_sxuat':
            lable_input = "Năm sản xuất: "
            edited_product[property] = input(lable_input)
            edited_product[property] = vi.validate_amout_input_field(edited_product[property], lable_input,1900, datetime.now().year)

        elif property == 'status':
            lable_input = "Trạng thái (0: Không hoạt động | 1: Hoạt động):"
            edited_product[property] = input(lable_input)
            edited_product[property] = vi.validate_amout_input_field(edited_product[property], lable_input,0,1)
        prd_data.save_product_to_json_file(edited_product,index)
        self.xuat_dien_thoai()
        print("Sửa thành công!")