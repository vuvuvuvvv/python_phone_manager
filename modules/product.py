import copy
from datetime import *
from modules.save_data import *
from modules.dien_thoai import *
from modules.clear_screen import *
from modules.validate_input import *

#
# Mo hinh dictionary danh sach chua dien thoai
#   ds_dien_thoai = {
#       id1 = [
#           dienthoai1,
#           dienthoai2,
#           ...
#       ],
#       id2 = [...],
#   }
#
class Product():
    def __init__(self):
        pass

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
                bansao_dungluong_dt = copy.deepcopy(dienthoai)
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
                        bansao_dungluong_dt.set_dung_luong(tmp_dung_luong)
                        list_dung_luong.append(tmp_dung_luong)
                        break
            
                #Clear screen
                clear_screen()

                #Nhap so loai RAM cho loai dien thoai co dung luong vua nhap
                print('----------------------------')
                print("NHAP RAM DIEN THOAI CHO:")
                print(str(bansao_dungluong_dt))
                print('----------------------------')
                lable_input = "So luong loai RAM: "
                so_ram = input(lable_input)
                so_ram = validate_amout_input_field(so_ram, lable_input)
                list_ram = []
                for k in range(0, so_ram):
                    #Nhap RAM
                    bansao_ram_dt = copy.deepcopy(bansao_dungluong_dt)
                    print('----------------------------')
                    print(f'Nhap loai RAM thu {"nhat" if k == 0 else k+1}: ')
                    lable_input = "Nhap RAM (GB): "
                    tmp_ram = input(lable_input)
                    tmp_ram = validate_amout_input_field(tmp_ram, lable_input)
                    while True:
                        if tmp_ram in list_ram:
                            print(f"RAM {tmp_ram}GB da co san!")
                            tmp_ram = input(lable_input)
                            tmp_ram = validate_amout_input_field(tmp_ram, lable_input)
                        else:
                            bansao_ram_dt.set_ram(tmp_ram)
                            list_ram.append(tmp_ram)
                            break

                    #Clear screen
                    clear_screen()

                    #Hoan thien gia ban, so luong, nam san xuat cho dien thoai 
                    print('----------------------------')
                    print('HOAN THIEN THONG TIN CHO: ')
                    print(str(bansao_ram_dt))
                    #Gia ban
                    lable_input = "Gia ban (VND): "
                    tmp_gia = input(lable_input)
                    tmp_gia = validate_amout_input_field(tmp_gia, lable_input,1000000)
                    bansao_ram_dt.set_gia(tmp_gia)
                    #So luong
                    lable_input = "So luong: "
                    tmp_so_luong = input(lable_input)
                    tmp_so_luong = validate_amout_input_field(tmp_so_luong, lable_input)
                    bansao_ram_dt.set_so_luong(tmp_so_luong)
                    #Nam san xuat
                    lable_input = "Nam san xuat: "
                    tmp_nam_sxuat = input(lable_input)
                    tmp_nam_sxuat = validate_amout_input_field(tmp_nam_sxuat, lable_input,1900, datetime.now().year)
                    bansao_ram_dt.set_nam_sxuat(tmp_nam_sxuat)
                    bansao_ram_dt.set_ngay_khoi_tao(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    #Save
                    save_product_to_json_file(bansao_ram_dt.get_dict_thongtin_dienthoai())

                    del bansao_ram_dt
                    #Clear screen
                    # clear_screen()

                del bansao_dungluong_dt
            #Xoa dien thoai
            del dienthoai

    #No return
    def xuat_dien_thoai() -> None:
        pass
    #No return
    def xoa_dien_thoai_theo_id() -> None:
        pass

    #Return class
    def tim_kiem_dien_thoai_theo_id() -> dict:
        pass

    #No return
    def sap_xep_danh_sach_dien_thoai() -> None:
        pass