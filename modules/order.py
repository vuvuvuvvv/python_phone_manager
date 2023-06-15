from datetime import datetime
import modules.product as od_product
import modules.data as od_data
import modules.auth as od_auth
import modules.validate_input as od_vi
import modules.system_function as od_stf
from tabulate import tabulate
class Order:
    def __init__(self) -> None:
        self.id = None
        self.user_id = None
        self.code = None
        self.name = None
        self.phone_number = None
        self.address = None
        self.products = None
        self.total_price = None
        self.ngay_khoi_tao = None
        self.status = 1 #Always 1 after created
        self.order_status = {1: "Chờ xác nhận", 2: "Đang lấy hàng", 3: "Đang vận chuyển",
                             4: "Giao thành công", 5: "Đang hoàn trả", 6: "Đơn hàng bị hủy"}

    def create_order(self, cart = None):
        if cart is None:
            cart = od_data.get_cart_item_from_json
        data = {}
        data['code'] = od_stf.create_code_orders()
        while True :
            data['name'] = input("Nhập họ tên: ")
            if not od_vi.check_name(data['name']):
                print('Tên không hợp lệ')
                continue
            else:
                break
        while True :
            data['address'] = input("Nhập địa chỉ nhận hàng: ")
            if not od_vi.check_address(data['address']):
                print('Địa chỉ không hợp lệ')
                continue
            else:
                break
        while True :
            data['phone_number'] = input("Nhập số điện thoại liên hệ: ")
            if not od_vi.check_phone_number(data['phone_number']):
                print('Số điện thoại không hợp lệ')
                continue
            else:
                break
        data['products'] = []
        data['total_price'] = 0
        for item in cart:
            tmp_product = {}
            tmp_product['id'] = item['product']['id']
            tmp_product['quantity'] = item['quantity']
            data['total_price'] += item['product']['gia'] * item['quantity']
            data['products'].append(tmp_product)
        data['ngay_khoi_tao'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data['status'] = self.status
        od_data.save_order_item_to_json_file(data) 

    def get_order(self):
        return od_data.get_order_from_json()

    def show_order(self,title=None,orders=None) -> None:
        od_stf.clear_screen()
        if orders is None:
            orders = od_data.get_order_from_json()
        if len(orders)>0:
            title = f'ĐƠN HÀNG CỦA BẠN - BẠN CÓ TẤT CẢ {len(orders)} ĐƠN HÀNG' if not od_auth.Auth().is_admin() else 'ĐƠN HÀNG HIỆN CÓ'
            header = ['Sản phẩm','Giá bán','Số lượng',"Đơn giá"]
            product = od_product.Product()
            print(title)
            for order in orders:
                print("-----------------------------------")
                print(f"Mã vận đơn: {order['code']}")
                print(f"Trạng thái: {self.order_status[order['status']]}")
                print(f"Tên người nhận: {order['name']}")
                print(f"Địa chỉ giao: {order['address']}")
                print(f"Số điện thoại liên hệ: {order['phone_number']}")
                print("Đơn hàng bao gồm:")
                data = []
                for item in order['products']:
                    dienthoai = product.find_product_by_id(item['id'])
                    row = [
                        f"Điện thoại {dienthoai['ten']} {dienthoai['dung_luong']}GB RAM {dienthoai['dung_luong']}GB phiên bản {dienthoai['nam_sxuat']}",
                        f"{format(dienthoai['gia'], ',d').replace(',', '.')}VND",
                        f"{format(item['quantity'], ',d').replace(',', '.')}",
                        f"{format((dienthoai['gia'] * item['quantity']), ',d').replace(',', '.')}VND",
                    ]
                    data.append(row)
                table = tabulate(data, header, tablefmt="fancy_grid")
                print(table)
                print(f"Tổng thanh toán: {format(order['total_price'], ',d').replace(',', '.')}VND")
            print("-----------------------------------")
            print("")
            print("-----------------------------------")
        else:
            od_stf.clear_screen()
            print("+-----------------------------+")
            print("| Không có sản phẩm hiển thị! |")
            print("+-----------------------------+")
        return
