from modules import *
from datetime import *
import math

#
# Mo hinh dictionary danh sach chua dien thoai
#   DanhSachSanPham = {
#       id1 = [
#           dienthoai1,
#           dienthoai2,
#           ...
#       ],
#       id2 = [...],
#   }
#
DanhSachSanPham = {}
status = {
    0: "Khong hoat dong",
    1: 'Hoat dong'
}

class DienThoai:
    count = 0  # Auto increment

    def __init__(self):
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
            result += f"\nDung luong: {self.get_dungluong()} GB"
        if self.ram is not None:
            result += f"\nRAM: {self.get_ram()} GB"
        if self.gia is not None:
            result += f"\nGia: {format(self.get_gia(), ',d').replace(',', '.')}VND"
        if self.soluong is not None:
            result += f"\nSo luong: {self.get_soluong()}"
        if self.nam_sxuat is not None:
            result += f"\nNam san xuat: {self.get_nam_sxuat()}"
        return result

    def get_list_thongtin_dienthoai(self):
        return [self.id, self.ten, self.hang, self.dungluong, self.ram, self.soluong, self.gia, self.nam_sxuat, status[self.status]]

    def __del__ (self):
        # for dien_thoai in self.dien_thoai_list:
        #     if dien_thoai.id == id:
        #         self.dien_thoai_list.remove(dien_thoai)
        #         break
        return 


def nhapDienThoai():
    # Nhap so san pham
    print('----------------------------')
    lable_input = "So luong dien thoai muon nhap: "
    sl_dienthoai = input(lable_input)
    sl_dienthoai = ValidateAmountInputForm(sl_dienthoai,lable_input,1,100)
    # Nhap thong tin san pham
    print('----------------------------')
    print('Nhap thong tin cho dien thoai:')
    for i in range(0, sl_dienthoai):
        dienthoai = DienThoai()
        #
        #Khoi tao key va value luu du lieu dien thoai vao dictionary DanhSachSanPham
        # Key: Id dien thoai
        # Value: List du lieu dien thoai
        #
        DanhSachSanPham[dienthoai.get_id()] = []
        print(f'San pham thu {i + 1 if i > 0 else "nhat"}:')
        #Nhap ten
        tmp_ten = input("Nhap ten: ")
        while len(tmp_ten) <= 0 or len(tmp_ten) > 100:
            print("Ten khong duoc de trong va khong qua 100 ky tu!")
            tmp_ten = input("Nhap ten san pham: ")
        dienthoai.set_ten(tmp_ten)

        #Nhap hang san xuat
        tmp_hang = input("Nhap ten hang san xuat: ")
        while len(tmp_hang) <= 0 or len(tmp_hang) > 100:
            print("Ten khong duoc de trong va khong qua 100 ky tu!")
            tmp_hang = input("Nhap ten hang san xuat: ")
        dienthoai.set_hang(tmp_hang)

        #
        # Khoi tao vong lap lap theo so loai dung luong, moi loai dung luong co 1 hoac nhieu loai ram khac nhau
        # Moi 1 loai dien thoai co dung luong va RAM lai co 1 muc gia va so luong khac
        #
        #Nhap so loai dung luong
        print('----------------------------')
        print("Nhap so loai dung luong cho:")
        print(str(dienthoai))
        lable_input = "So luong loai dung luong: "
        so_dungluong = input(lable_input)
        so_dungluong = ValidateAmountInputForm(so_dungluong, lable_input)
        list_dungluong = [] #Khoi tao mang dung luong cho du lieu dien thoai hien tai = []
        for j in range(0, so_dungluong):
            #Nhap dung luong
            print('----------------------------')
            print(f'Nhap loai dung luong thu {"nhat" if j == 0 else j+1}: ')
            lable_input = "Nhap dung luong (GB): "
            tmp_dungluong = input(lable_input)
            tmp_dungluong = ValidateAmountInputForm(tmp_dungluong, lable_input)
            while True:
                if tmp_dungluong in list_dungluong:
                    print(f"Dung luong {tmp_dungluong}GB da co san!")
                    tmp_dungluong = input(lable_input)
                    tmp_dungluong = ValidateAmountInputForm(tmp_dungluong, lable_input)
                else:
                    dienthoai.set_dungluong(tmp_dungluong)
                    list_dungluong.append(tmp_dungluong)
                    break
            #Nhap so loai RAM cho loai dien thoai co dung luong vua nhap
            print('----------------------------')
            print("Nhap so loai RAM cho:")
            print(str(dienthoai))
            lable_input = "So luong loai RAM: "
            so_ram = input(lable_input)
            so_ram = ValidateAmountInputForm(so_ram, lable_input)
            list_ram = []
            for k in range(0, so_ram):
                #Nhap RAM
                print('----------------------------')
                print(f'Nhap loai RAM thu {"nhat" if k == 0 else k+1}: ')
                lable_input = "Nhap RAM (GB): "
                tmp_ram = input(lable_input)
                tmp_ram = ValidateAmountInputForm(tmp_ram, lable_input)
                while True:
                    if tmp_ram in list_ram:
                        print(f"RAM {tmp_ram}GB da co san!")
                        tmp_ram = input(lable_input)
                        tmp_ram = ValidateAmountInputForm(tmp_ram, lable_input)
                    else:
                        dienthoai.set_ram(tmp_ram)
                        list_ram.append(tmp_ram)
                        break
                
                #Hoan thien gia ban, so luong, nam san xuat cho dien thoai 
                print('----------------------------')
                print('Hoan thien thong tin cho: ')
                print(str(dienthoai))
                #Gia ban
                lable_input = "Gia ban (VND): "
                tmp_gia = input(lable_input)
                tmp_gia = ValidateAmountInputForm(tmp_gia, lable_input,1000000)
                dienthoai.set_gia(tmp_gia)
                #So luong
                lable_input = "So luong: "
                tmp_soluong = input(lable_input)
                tmp_soluong = ValidateAmountInputForm(tmp_soluong, lable_input)
                dienthoai.set_soluong(tmp_soluong)
                #Nam san xuat
                lable_input = "Nam san xuat: "
                tmp_nam_sxuat = input(lable_input)
                tmp_nam_sxuat = ValidateAmountInputForm(tmp_nam_sxuat, lable_input,1900, datetime.now().year)
                dienthoai.set_nam_sxuat(tmp_nam_sxuat)
                #Them vao dictionary DanhSachSanPham voi key la id cua san pham
                DanhSachSanPham[dienthoai.get_id()].append(dienthoai)
                print('----------------------------')
                # for item in dienthoai.get_list_thongtin_dienthoai():
                #     print(item)
                # print('----------------------------')
                print(DanhSachSanPham)
                print('----------------------------')

nhapDienThoai()
