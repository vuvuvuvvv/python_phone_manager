from modules import *
from datetime import *
import math

DanhSachSanPham = []
status = {
    0: "Khong hoat dong",
    1: 'Hoat dong'
}

# class Memory:
#     def __init__(self,storage,ram):
#         self.storage = storage
#         self.ram = ram
    
#     def __str__(self):
#         return f"Dung luong: {self.storage}GB\nRAM: {self.ram}GB\n"

#     def __del__ (self):
#         print("Đã xóa!")

class DienThoai:
    id = 0  # Auto increment
    ten = None
    hang = None
    dungluong = None
    soluong = None
    gia = None
    ram = None
    status = 1 #Automatically activated after creation
    nam_sxuat = None

    def __init__(self):
        DienThoai.id += 1

    def __str__(self):
        result = f"\nDien thoai: {self.ten}"\
            f"\nHang: {self.hang}" if self.hang else "" \
            f"\nSo luong: {self.soluong}" if self.soluong else "" \
            f"\nGia: {self.gia}" if self.gia else "" \
            f"\nDung luong: {self.dungluong}" if self.dungluong else "" \
            f"\nRAM: {self.ram}" if self.ram else "" \
            f"\nNam san xuat: {self.nam_sxuat}" if self.nam_sxuat else "" 
        return result

    # def sua_dien_thoai(self, id, new_dien_thoai):
    #     for i in range(len(self.dien_thoai_list)):
    #         if self.dien_thoai_list[i].id == id:
    #             self.dien_thoai_list[i] = new_dien_thoai
    #             break

    def __del__ (self, id):
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
        tmp_product = DienThoai()
        print(f'San pham thu {i + 1 if i > 0 else "nhat"}:')
        tmp_product.id = DienThoai.id

        tmp_product.ten = input("Nhap ten: ")
        while len(tmp_product.ten) <= 0 or len(tmp_product.ten) > 100:
            print("Ten khong duoc de trong va khong qua 100 ky tu!")
            tmp_product.ten = input("Nhap ten san pham: ")

        tmp_product.hang = input("Nhap ten hang san xuat: ")
        while len(tmp_product.ten) <= 0 or len(tmp_product.ten) > 100:
            print("Ten khong duoc de trong va khong qua 100 ky tu!")
            tmp_product.ten = input("Nhap ten hang san xuat: ")
            
        print('----------------------------')
        print("Nhap so loai dung luong cho:")
        print(str(tmp_product))
        lable_input = "So luong: "
        q_dungluong = input(lable_input)
        q_dungluong = ValidateAmountInputForm(q_dungluong, lable_input)
        list_dungluong = []
        for j in range(0, q_dungluong):
            print('----------------------------')
            print('Nhap dung luong cho: ')
            print(str(tmp_product))
            lable_input = "Nhap dung luong (GB): "
            tmp_product.dungluong = input(lable_input)
            tmp_product.dungluong = ValidateAmountInputForm(tmp_product.dungluong, lable_input)
            while tmp_product.dungluong in list_dungluong:
                print(f"Dung luong {tmp_product.dungluong}GB da co san!")
                tmp_product.dungluong = input(lable_input)
                tmp_product.dungluong = ValidateAmountInputForm(tmp_product.dungluong, lable_input)
            list_dungluong.append(tmp_product.dungluong)

            print('----------------------------')
            print("Nhap so loai RAM cho:")
            print(str(tmp_product))
            lable_input = "So luong: "
            q_ram = input(lable_input)
            q_ram = ValidateAmountInputForm(q_ram, lable_input)
            list_ram = []
            for k in range(0, q_ram):
                print('----------------------------')
                print('Nhap RAM cho: ')
                print(str(tmp_product))
                lable_input = "Nhap RAM (GB): "
                tmp_product.ram = input(lable_input)
                tmp_product.ram = ValidateAmountInputForm(tmp_product.ram, lable_input)
                while tmp_product.ram in list_ram:
                    print(f"Ram {tmp_product.ram}GB da co san!")
                    tmp_product.ram = input(lable_input)
                    tmp_product.ram = ValidateAmountInputForm(tmp_product.ram, lable_input)
                
                lable_input = "Gia ban (VND): "
                tmp_product.gia = input(lable_input)
                tmp_product.gia = ValidateAmountInputForm(tmp_product.gia, lable_input,1000000)

                lable_input = "So luong: "
                tmp_product.soluong = input(lable_input)
                tmp_product.soluong = ValidateAmountInputForm(tmp_product.soluong, lable_input)


                lable_input = "Nam san xuat: "
                tmp_product.nam_sxuat = input(lable_input)
                tmp_product.nam_sxuat = ValidateAmountInputForm(tmp_product.nam_sxuat, lable_input,1900, datetime.now().year)

                DanhSachSanPham.append[tmp_product]

# class User :
#     count = 0

#     def __init__(self, ten,ngaysinh,sdt,email,gioitinh,diachi):


#         self.ten = ten
#         self.ngaysinh = ngaysinh
#         self.sdt =sdt
#         self.email = email
#         self.gioitinh = gioitinh
#         self.diachi = diachi

#         User.count += 1

#     def set_id(self, ten):
#         self.ten = ten

#     def get_id(self):
#         return self.ten

#     def set_id(self, ngaysinh):
#         self.ngaysinh = ngaysinh

#     def get_id(self):
#         return self.ngaysinh

#     def set_id(self, sdt):
#         self.sdt = sdt

#     def get_id(self):
#         return self.sdt

#     def set_id(self, email):
#         self.email = email

#     def get_id(self):
#         return self.email

#     def set_id(self, gioitinh ):
#         self.gioitinh = gioitinh

#     def get_id(self):
#         return self.gioitinh

#     def set_id(self, diachi):
#         self.diachi = diachi

#     def get_id(self):
#         return self.diachi

#     def show_User(self):
#         # print("\n+--------------------+")
#         print(f"|Tên khách hàng                 :          {self.ten}   |")
#         print(f"|ngày sinh khách hàng           :          {self.ngaysinh}   |")
#         print(f"|số điện thoại khách hàng       :          {self.sdt}   |")
#         print(f"|email khách hàng                 :          {self.email}   |")
#         print(f"| giới tính khách hàng          :          {self.gioitinh}   |")
#         print(f"| địa chỉ khách hàng          :          {self.diachi}   |")
#         print("+----------------------------------------------+")

# a = User(" ĐÀO ", "06-06-2001 ", "12343252523","sada@gmail.com", "NAM  " , "NAM ĐỊNH" )
# b = User(" HOA ", "01-01-2003" , "33214321442","324234@gmail.com","NỮ ", " VIỆT NAM ")
# print(a.show_User())
# print(b.show_User())

nhapDienThoai()
