import modules.data as c_data
import modules.system_function as stf
from tabulate import tabulate
from datetime import datetime
class Cart:
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
                "ngay_khoi_tao":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

    def show_cart(self,title="GIỎ HÀNG",cart=None) -> None:
        if cart is None:
            cart = c_data.get_dict_cart_from_json()
        data = []
        header = ['Sản phẩm','Giá bán','Số lượng',"Đơn giá"]
        total_price = 0
        for item in cart:
            dienthoai = item['product']
            total_price += dienthoai['gia'] * item['quantity']
            row = [
                f"Điện thoại {dienthoai['ten']} {dienthoai['dung_luong']}GB RAM {dienthoai['dung_luong']}GB phiên bản {dienthoai['nam_sxuat']}",
                f"{format(dienthoai['gia'], ',d').replace(',', '.')}VND",
                f"{format(item['quantity'], ',d').replace(',', '.')}",
                f"{format((dienthoai['gia'] * item['quantity']), ',d').replace(',', '.')}VND",
            ]
            data.append(row)
        table = tabulate(data, header, tablefmt="fancy_grid")
        stf.clear_screen()
        print(title)
        print(table)
        print(f"TỔNG GIÁ: {format(total_price, ',d').replace(',', '.')}VND")
        print("---------------------------------------------------")
    
    def find_cart_item_in_cart_by_product(self,product):
        cart = c_data.get_dict_cart_from_json()
        for item in cart:
            if item['product'] == product:
                return item
        return None