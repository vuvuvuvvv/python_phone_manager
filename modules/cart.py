from modules.data import *
from modules.system_function import *
from tabulate import tabulate
class Cart():
    def __init__(self) -> None:
        self.user_id = None
        self.product = None
        self.quantity = None
        self.status = 1
        self.ngay_khoi_tao = None

    def get_cart_item(self) -> dict:
        return {
                "product":self.product,
                "quantity":self.quantity,
                "status":self.status,
                "ngay_khoi_tao":self.ngay_khoi_tao
            }

    def show_cart(self) -> None:
        data = []
        header = ['Sản phẩm','Giá bán','Số lượng',"Đơn giá"]
        total_price = 0
        for cart in get_dict_cart_from_json():
            dienthoai = cart['product']
            total_price += dienthoai['gia'] * cart['quantity']
            row = [
                f"Dien thoai {dienthoai['ten']} {dienthoai['dung_luong']}GB RAM {dienthoai['dung_luong']}GB phien ban {dienthoai['nam_sxuat']}",
                f"{format(dienthoai['gia'], ',d').replace(',', '.')}VND",
                f"{cart['quantity']}",
                f"{format((dienthoai['gia'] * cart['quantity']), ',d').replace(',', '.')}VND",
            ]
            data.append(row)
        table = tabulate(data, header, tablefmt="fancy_grid")
        clear_screen()
        print("GIO HANG")
        print(table)
        print(f"TONG THANH TOAN: {format(total_price, ',d').replace(',', '.')}VND")
        print("---------------------------------------------------")