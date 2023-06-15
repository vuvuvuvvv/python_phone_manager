from datetime import datetime
import modules.data as od_data
import modules.auth as od_auth
import modules.validate_input as od_vi
import modules.system_function as od_stf
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
        self.order_status = {1: "Đợi xác nhận", 2: "Đang lấy hàng", 3: "Đang vận chuyển",
                             4: "Giao thành công", 5: "Đang hoàn trả", 6: "Đơn hàng bị hủy"}

    def create_order(self, cart = None):
        auth = od_auth.Auth()
        if cart is None:
            cart = od_data.get_dict_cart_from_json
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

    def get_dict_order(self):
        return {
            "name":self.name,
            "product":self.products,
            "total_price":self.total_price,
            "ngay_khoi_tao": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status":self.order_status[self.status]
        }


