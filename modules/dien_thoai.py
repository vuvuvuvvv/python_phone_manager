status = {
    0: "Khong hoat dong",
    1: 'Hoat dong'
}


class DienThoai:
    count = 0  # Tu dong tang

    def __init__(self):
        # Khi co tham chieu den class Dienthoai => count tang <=> id san pham tu tang
        DienThoai.count += 1
        self.id = DienThoai.count
        self.ten = None
        self.hang = None
        self.dung_luong = None
        self.ram = None
        self.so_luong = None
        self.gia = None
        self.nam_sxuat = None
        self.ngay_khoi_tao = None
        self.status = 1  # Automatically activated after creation

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

    def set_dung_luong(self, dung_luong):
        self.dung_luong = dung_luong

    def get_dung_luong(self):
        return self.dung_luong

    def set_so_luong(self, so_luong):
        self.so_luong = so_luong

    def get_so_luong(self):
        return self.so_luong

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

    def set_ngay_khoi_tao(self, ngay_khoi_tao):
        self.ngay_khoi_tao = ngay_khoi_tao

    def __str__(self):
        result = f"Dien thoai: {self.get_ten()}"
        if self.hang is not None:
            result += f"\nHang: {self.get_hang()}"
        if self.dung_luong is not None:
            result += f"\nDung luong: {format(self.get_dung_luong(), ',d').replace(',', '.')} GB"
        if self.ram is not None:
            result += f"\nRAM: {format(self.get_ram(), ',d').replace(',', '.')} GB"
        if self.gia is not None:
            result += f"\nGia: {format(self.get_gia(), ',d').replace(',', '.')}VND"
        if self.so_luong is not None:
            result += f"\nSo luong: {format(self.get_so_luong(), ',d').replace(',', '.')}"
        if self.nam_sxuat is not None:
            result += f"\nNam san xuat: {self.get_nam_sxuat()}"
        return result

    def get_dict_thongtin_dienthoai(self):
        return {
                "id" : self.id,
                "ten" : self.ten,
                "hang" : self.hang,
                "dung_luong" : self.dung_luong,
                "ram" : self.ram,
                "so_luong" : self.so_luong,
                "gia" : self.gia,
                "nam_sxuat" : self.nam_sxuat,
                "status" : status[self.status],
                "ngay_khoi_tao" : self.ngay_khoi_tao
            }

    def __del__(self):
        pass
