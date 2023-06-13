try:
    import copy
    from datetime import *
    from modules.data import *
    from modules.dien_thoai import *
    from modules.system_function import *
    from modules.validate_input import *
    from tabulate import tabulate
    from modules.auth import *
except Exception as err:
    print(f"Loi: {err}")

status = {
    0: "Khong hoat dong",
    1: "Hoat dong"
}

class Product():
    def __init__(self):
        self.list_dien_thoai = get_dict_product_from_json()['products']

    def nhap_dien_thoai(self) -> None:
        # Nhap so san pham
        print('----------------------------')
        lable_input = "So luong dien thoai muon nhap: "
        sl_dienthoai = input(lable_input)

        #Clear screen
        clear_screen()

        sl_dienthoai = validate_amout_input_field(sl_dienthoai,lable_input,1,100)
        # Nhap thong tin san pham
        print('----------------------------')
        print('NHAP THONG TIN CHO DIEN THOAI:')
        for i in range(0, sl_dienthoai):
            #Khoi tao dienthoai
            dienthoai = DienThoai()
            
            print(f'San pham thu {i + 1 if i > 0 else "nhat"}:')
            #Nhap ten
            tmp_ten = input("Nhap ten: ")
            while len(tmp_ten) <= 0 or len(tmp_ten) > 100:
                print("Ten khong duoc de trong va khong qua 100 ky tu!")
                tmp_ten = input("Nhap ten san pham: ")
            #Nhap hang san xuat
            tmp_hang = input("Nhap ten hang san xuat: ")
            while len(tmp_hang) <= 0 or len(tmp_hang) > 100:
                print("Ten khong duoc de trong va khong qua 100 ky tu!")
                tmp_hang = input("Nhap ten hang san xuat: ")

            dienthoai.set_ten(tmp_ten)
            dienthoai.set_hang(tmp_hang)

            #Clear screen
            clear_screen()

            #
            # Khoi tao vong lap lap theo so loai dung luong, moi loai dung luong co 1 hoac nhieu loai ram khac nhau
            # Moi 1 loai dien thoai co dung luong va RAM lai co 1 muc gia va so luong khac
            #
            #Nhap so loai dung luong
            print('----------------------------')
            print("NHAP DUNG LUONG DIEN THOAI CHO:")
            print(str(dienthoai))
            print('----------------------------')
            lable_input = "So luong loai dung luong: "
            so_dung_luong = input(lable_input)
            so_dung_luong = validate_amout_input_field(so_dung_luong, lable_input)
            list_dung_luong = [] #Khoi tao mang dung luong cho du lieu dien thoai hien tai = []
            for j in range(0, so_dung_luong):
                #
                # Khoi tao 1 ban sao cua dienthoai de lay du lieu id, ten va hang
                # Sau khi khoi tao va hoan thien thong tin => save vao ds_dien_thoai & del
                # dienthoai sau khi luu
                #
                bansao_dt = copy.deepcopy(dienthoai)
                #Nhap dung luong
                print('----------------------------')
                print(f'Nhap loai dung luong thu {"nhat" if j == 0 else j+1}: ')
                lable_input = "Nhap dung luong (GB): "
                tmp_dung_luong = input(lable_input)
                tmp_dung_luong = validate_amout_input_field(tmp_dung_luong, lable_input)
                while True:
                    if tmp_dung_luong in list_dung_luong:
                        print(f"Dung luong {tmp_dung_luong}GB da co san!")
                        tmp_dung_luong = input(lable_input)
                        tmp_dung_luong = validate_amout_input_field(tmp_dung_luong, lable_input)
                    else:
                        bansao_dt.set_dung_luong(tmp_dung_luong)
                        list_dung_luong.append(tmp_dung_luong)
                        break
            
                #Clear screen
                clear_screen()

                #Nhap so loai RAM cho loai dien thoai co dung luong vua nhap
                print('----------------------------')
                print("NHAP RAM DIEN THOAI CHO:")
                print(str(bansao_dt))
                print('----------------------------')
                lable_input = "Nhap RAM (GB): "
                tmp_ram = input(lable_input)
                tmp_ram = validate_amout_input_field(tmp_ram, lable_input)
                bansao_dt.set_ram(tmp_ram)

                #Clear screen
                clear_screen()

                #Hoan thien gia ban, so luong, nam san xuat cho dien thoai 
                print('----------------------------')
                print('HOAN THIEN THONG TIN CHO: ')
                print(str(bansao_dt))
                #Gia ban
                lable_input = "Gia ban (VND): "
                tmp_gia = input(lable_input)
                tmp_gia = validate_amout_input_field(tmp_gia, lable_input,1000000)
                bansao_dt.set_gia(tmp_gia)
                #So luong
                lable_input = "So luong: "
                tmp_so_luong = input(lable_input)
                tmp_so_luong = validate_amout_input_field(tmp_so_luong, lable_input)
                bansao_dt.set_so_luong(tmp_so_luong)
                #Nam san xuat
                lable_input = "Nam san xuat: "
                tmp_nam_sxuat = input(lable_input)
                tmp_nam_sxuat = validate_amout_input_field(tmp_nam_sxuat, lable_input,1900, datetime.now().year)
                bansao_dt.set_nam_sxuat(tmp_nam_sxuat)
                bansao_dt.set_ngay_khoi_tao(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                #Save
                save_product_to_json_file(bansao_dt.get_dict_thongtin_dienthoai())
                #Clear screen
                clear_screen()
                del bansao_dt
            #Xoa dien thoai
            del dienthoai

    def xuat_dien_thoai(self) -> None:
        try:
            auth = Auth()
            data = []
            header = ['Ten san pham','Hang san xuat','Dung luong','RAM','Gia ban','Nam san xuat']
            # Neu la Admin thi hien thi ca san pham khong con hoat dong va trang thai cua tat ca san pham
            if auth.is_admin():
                header.append('Trang thai')
            for dienthoai in self.list_dien_thoai:
                row = [
                    f"{dienthoai['ten']} {dienthoai['dung_luong']} GB",
                    f"{dienthoai['hang']}",
                    f"{dienthoai['dung_luong']} GB",
                    f"{dienthoai['ram']} GB",
                    f"{format(dienthoai['gia'], ',d').replace(',', '.')}VND",
                    f"{dienthoai['nam_sxuat']}"
                ]
                if auth.is_admin():
                    row.append(f"{status[dienthoai['status']]}")
                    data.append(row)
                else:
                    if dienthoai['status'] == 1:
                        data.append(row)
            table = tabulate(data, header, tablefmt="grid")
            clear_screen()
            print("DANH SACH SAN PHAM")
            print(table)
        except Exception as err:
            print(f"Loi: {err}")

    #No return
    def xoa_dien_thoai(self,order_phone):
        if len(self.list_dien_thoai) == 0:
            print("Danh sach dien thoai rong!")
        else:
            order_phone = input('Nhap id dien thoai muon xoa:')
            order_phone = validate_amout_input_field(order_phone)
            try:
                with open('./data/client/entries.json', 'w') as file:
                    order_phone -= 1
                    phone_deleted = self.list_dien_thoai[order_phone]
                    index = self.list_dien_thoai.index(phone_deleted)

                    self.list_dien_thoai.pop(index)

                    json.dump(self.dict_user, file, indent=4)
                #Renew data
                self.dict_user = get_dict_product_from_json()
            # print("Xóa thành công!")
            except Exception as err:
                print(f"Loi: {err}")

    #Find by name
    def find_product_by_condition(self,property,value) -> dict:
        get_all_product = sorted(self.list_dien_thoai,key=lambda x: x[property])
        list_product = []
        #Find by product name
        for item in get_all_product:
            if property == "ten":
                #Lower case va be nho ten san pham de so sanh
                pr_name = item["ten"].lower().split(" ")
                #Kiem tra tu khoa tim kiem
                #Co 2 tu tro len: -> Be nho de so sanh va tim kiem
                if " " in value:
                    keywords = value.lower().split(" ")
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
            else:
                if value in item[property]:
                    if item not in list_product:
                        list_product.append(item)
        #Tra ve ket qua
        if len(list_product) == 0:
            return None
        else:
            return list_product

    #No return
    def sap_xep_danh_sach_dien_thoai() -> None:
        pass