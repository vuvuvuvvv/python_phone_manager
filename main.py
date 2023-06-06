from modules import *
from datetime import *
import math
import copy

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
ds_dien_thoai = {}
status = {
    0: "Khong hoat dong",
    1: 'Hoat dong'
}

class DienThoai:
    count = 0  # Tu dong tang

    def __init__(self):
        #Khi co tham chieu den class Dienthoai => count tang <=> id san pham tu tang
        DienThoai.count += 1
        self.id = DienThoai.count
        self.ten = None
        self.hang = None
        self.dungluong = None
        self.ram = None
        self.soluong = None
        self.gia = None
        self.nam_sxuat = None
        self.status = 1 #Automatically activated after creation

    def get_id(self):
        return self.id
    
    def set_ten(self, ten):
        self.ten = ten
    
    def get_ten(self):
        return self.ten
    
    def set_hang(self, hang):
        self.hang = hang
    
    def get_hang(self):
        return self.hang
    
    def set_dungluong(self, dungluong):
        self.dungluong = dungluong
    
    def get_dungluong(self):
        return self.dungluong
    
    def set_soluong(self, soluong):
        self.soluong = soluong
    
    def get_soluong(self):
        return self.soluong
    
    def set_gia(self, gia):
        self.gia = gia
    
    def get_gia(self):
        return self.gia
    
    def set_ram(self, ram):
        self.ram = ram
    
    def get_ram(self):
        return self.ram
    
    def set_nam_sxuat(self, nam_sxuat):
        self.nam_sxuat = nam_sxuat
    
    def get_nam_sxuat(self):
        return self.nam_sxuat

    def __str__(self):
        result = f"Dien thoai: {self.get_ten()}"
        if self.hang is not None:
            result += f"\nHang: {self.get_hang()}"
        if self.dungluong is not None:
            result += f"\nDung luong: {format(self.get_dungluong(), ',d').replace(',', '.')} GB"
        if self.ram is not None:
            result += f"\nRAM: {format(self.get_ram(), ',d').replace(',', '.')} GB"
        if self.gia is not None:
            result += f"\nGia: {format(self.get_gia(), ',d').replace(',', '.')}VND"
        if self.soluong is not None:
            result += f"\nSo luong: {format(self.get_soluong(), ',d').replace(',', '.')}"
        if self.nam_sxuat is not None:
            result += f"\nNam san xuat: {self.get_nam_sxuat()}"
        return result

    def get_list_thongtin_dienthoai(self):
        return [self.id, self.ten, self.hang, self.dungluong, self.ram, self.soluong, self.gia, self.nam_sxuat, status[self.status]]

    def __del__ (self):
        # print("")
        return


def nhap_tt_dien_thoai():
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
        #
        #Khoi tao key va value luu du lieu dien thoai vao dictionary ds_dien_thoai
        # Key: Id dien thoai
        # Value: List du lieu dien thoai
        #
        ds_dien_thoai[dienthoai.get_id()] = []
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
        so_dungluong = input(lable_input)
        so_dungluong = validate_amout_input_field(so_dungluong, lable_input)
        list_dungluong = [] #Khoi tao mang dung luong cho du lieu dien thoai hien tai = []
        for j in range(0, so_dungluong):
            #
            # Khoi tao 1 ban sao cua dienthoai de lay du lieu id, ten va hang
            # Sau khi khoi tao va hoan thien thong tin => save vao ds_dien_thoai & del
            # dienthoai sau khi luu
            #
            bansao_dienthoai = copy.deepcopy(dienthoai)
            #Nhap dung luong
            print('----------------------------')
            print(f'Nhap loai dung luong thu {"nhat" if j == 0 else j+1}: ')
            lable_input = "Nhap dung luong (GB): "
            tmp_dungluong = input(lable_input)
            tmp_dungluong = validate_amout_input_field(tmp_dungluong, lable_input)
            while True:
                if tmp_dungluong in list_dungluong:
                    print(f"Dung luong {tmp_dungluong}GB da co san!")
                    tmp_dungluong = input(lable_input)
                    tmp_dungluong = validate_amout_input_field(tmp_dungluong, lable_input)
                else:
                    bansao_dienthoai.set_dungluong(tmp_dungluong)
                    list_dungluong.append(tmp_dungluong)
                    break
        
            #Clear screen
            clear_screen()

            #Nhap so loai RAM cho loai dien thoai co dung luong vua nhap
            print('----------------------------')
            print("NHAP RAM DIEN THOAI CHO:")
            print(str(bansao_dienthoai))
            print('----------------------------')
            lable_input = "So luong loai RAM: "
            so_ram = input(lable_input)
            so_ram = validate_amout_input_field(so_ram, lable_input)
            list_ram = []
            for k in range(0, so_ram):
                #Nhap RAM
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
                        bansao_dienthoai.set_ram(tmp_ram)
                        list_ram.append(tmp_ram)
                        break

                #Clear screen
                clear_screen()

                #Hoan thien gia ban, so luong, nam san xuat cho dien thoai 
                print('----------------------------')
                print('HOAN THIEN THONG TIN CHO: ')
                print(str(bansao_dienthoai))
                #Gia ban
                lable_input = "Gia ban (VND): "
                tmp_gia = input(lable_input)
                tmp_gia = validate_amout_input_field(tmp_gia, lable_input,1000000)
                bansao_dienthoai.set_gia(tmp_gia)
                #So luong
                lable_input = "So luong: "
                tmp_soluong = input(lable_input)
                tmp_soluong = validate_amout_input_field(tmp_soluong, lable_input)
                bansao_dienthoai.set_soluong(tmp_soluong)
                #Nam san xuat
                lable_input = "Nam san xuat: "
                tmp_nam_sxuat = input(lable_input)
                tmp_nam_sxuat = validate_amout_input_field(tmp_nam_sxuat, lable_input,1900, datetime.now().year)
                bansao_dienthoai.set_nam_sxuat(tmp_nam_sxuat)
                #Them vao dictionary ds_dien_thoai voi key la id cua san pham
                ds_dien_thoai[dienthoai.get_id()].append(copy.deepcopy(bansao_dienthoai))

                #Xoa ban sao dienthoai
                del bansao_dienthoai
                
                #Clear screen
                clear_screen()
                
                # print('----------------------------')
                # print(str(ds_dien_thoai[1][0]))
                # print('----------------------------')
                # print(str(dienthoai))
                # print('----------------------------')

        #Xoa dien thoai
        del dienthoai

nhap_tt_dien_thoai()
