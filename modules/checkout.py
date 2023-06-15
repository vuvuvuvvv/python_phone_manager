import modules.data as co_data
import modules.cart as co_cart
import modules.order as co_order
from modules.validate_input import *
class Checkout:
    def checkout(self, list_item_in_cart = None):
        cart = co_cart.Cart() 
        if list_item_in_cart is None:
            list_item_in_cart = co_data.get_cart_item_from_json()
        cart.show_cart(title="THÔNG TIN ĐƠN HÀNG",cart=list_item_in_cart)
        print("XÁC NHẬN THANH TOÁN?")
        print("1. Xác nhận")
        print("2. Quay lại")
        lable = "Vui lòng nhập lựa chọn: "
        select = input(lable)
        select = validate_amout_input_field(select,lable,1,2)  
        if select == 1:
            order = co_order.Order()
            order.create_order(list_item_in_cart)
        return 

        
