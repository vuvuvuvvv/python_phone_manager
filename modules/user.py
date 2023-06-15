import json
import modules.data as user_data
import modules.auth as user_auth
import modules.validate_input as vi
import modules.system_function as stf
from tabulate import tabulate
from datetime import datetime


gender = {
    1: 'Nữ',
    2: 'Nam'
}

permission = {
    0: 'Khách',
    1: 'Admin'
}

status = {
    0: "Không hoạt động",
    1: "Hoạt động"
}

class User:
    def __init__(self) -> None:
        self.id = None
        self.username = None
        self.password = None
        self.name = None
        self.phone_num = None
        self.mail = None
        self.gender = None #1: Female / 2: Male
        self.role = 0 #0: customer, 1: admin
        self.status = 1
        self.ngay_khoi_tao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_dict_tt_user(self):
        return {
            "username": self.username,
            "password": self.password,
            "id": self.id + 1,
            "name": self.name,
            "mail": self.mail,
            "phone_num": self.phone_num,
            "gender": self.gender,
            "status": self.status,
            "ngay_khoi_tao": self.ngay_khoi_tao
        }
    
    def xuat_tt_all_user(self,title = "DANH SÁCH NGƯỜI DÙNG", list_user = None) -> None:
        if list_user is None or len(list_user) > 0:
            auth = user_auth.Auth()
        
            if list_user is None:
                get_all_user = user_data.get_dict_user_from_json()['list_admin'] + user_data.get_dict_user_from_json()['list_client']
            else:
                get_all_user = list_user
            data = []
            header = ['STT','Tên người dùng','Tên đăng nhập','Điện thoại','Email','Giới tính','Quyền hạn','Trạng thái']
            i = 1
            for user in get_all_user:
                row = [
                    i,
                    f"{'(Bạn)' if user['id'] == user_data.get_session()['id'] else ''} {user['name']}",
                    f"{user['username']}",
                    f"{user['phone_num']}",
                    f"{user['mail']}",
                    f"{gender[user['gender']]}",
                    f"{permission[user['role']]}",
                    f"{status[user['status']]}",
                ]
                i+=1
                data.append(row)
            table = tabulate(data, header, tablefmt="fancy_grid")
            stf.clear_screen()
            print(title)
            print(table)
        else:
            stf.clear_screen()
            print("+-----------------------------+")
            print("| Không có nội dung hiển thị! |")
            print("+-----------------------------+")

    def delete_user(self,order_user):
        if len(self.list_dien_thoai) == 0:
            print("Danh sách người dùng rỗng!")
        else:
            order_user = input('Nhập STT người muốn xóa:')
            order_user = vi.validate_amout_input_field(order_user)
            try:
                with open('./data/client/entries.json', 'w') as file:
                    order_user -= 1
                    all_user = user_data.get_dict_user_from_json()['list_admin'] + user_data.get_dict_user_from_json()['list_client']
                    user_deleted = all_user[order_user]
                    if user_deleted['role'] == 0:
                        index = user_data.get_dict_user_from_json()['list_client'].index(user_deleted)
                        user_data.get_dict_user_from_json()['list_client'].pop(index)
                    else:
                        index = user_data.get_dict_user_from_json()['list_admin'].index(user_deleted)
                        user_data.get_dict_user_from_json()['list_admin'].pop(index)

                    json.dump(user_data.get_dict_user_from_json(), file, indent=4)
            # print("Xóa thành công!")
            except Exception as err:
                print(f"Lỗi: {err}")

    def find_user_by_id_or_username(self, key):
        #Get all user & sort by Id
        if isinstance(key,int):
            property = "id"
        else:
            property = "username"
        get_all_user = sorted((user_data.get_dict_user_from_json()['list_admin'] + user_data.get_dict_user_from_json()['list_client']),key=lambda x: x[property])
        left = 0
        right = len(get_all_user) - 1

        while left <= right:
            mid = (left + right) // 2

            if get_all_user[mid][property] == key:
                return get_all_user[mid]
            elif get_all_user[mid][property] < key:
                left = mid + 1
            else:
                right = mid - 1
        return None
    
    def edit_user(self, user = None) -> None:
        #ten cac thuoc tinh
        lable_properties = ['Tên người dùng','Tên đăng nhập',"Mật khẩu",'Điện thoại','Email','Giới tính','Trạng thái',"Tất cả","Thoát"]
        #cac truong thuoc tinh cua user
        properties = ['name','username','password','phone_num','mail','gender','status',None,True]

        if user is None:
            list_user = user_data.get_dict_user_from_json()['list_admin'] + user_data.get_dict_user_from_json()['list_client']
            self.xuat_tt_all_user()
            print("Chọn STT người dùng muốn sửa thông tin:")
            lable = "Chọn: "
            select = input(lable)
            select = vi.validate_amout_input_field(select,lable= lable,max=len(list_user))
            user_edited = list_user[select - 1]
        else:
            user_edited = user
        #Tim vi tri du lieu de thao tao voi file du lieu
        index = user_data.get_dict_user_from_json()[('list_client' if user_edited['role'] == 0 else "list_admin")].index(user_edited)
        stf.clear_screen()
        self.xuat_tt_all_user(title="THÔNG TIN NGƯỜI DÙNG HIỆN TẠI",list_user=[user_edited])

        print("Chọn mục bạn muốn sửa: ")
        #Nếu là admin => Không cho chỉnh sửa trạng thái hoạt động của bản thân
        if user_edited == user_data.get_session():
            lable_properties.pop(lable_properties.index('Trạng thái'))
            properties.pop(properties.index('status'))
        #In ra các lựa chọn
        for i in range (1, len(lable_properties) +1):
            print(f"{i}. {lable_properties[i-1]}")
        lable = "Chọn: "
        select = input(lable)
        select = vi.validate_amout_input_field(select,lable= lable,max=len(lable_properties))
        property = properties[select - 1]
        #Nhập
        stf.clear_screen()
        print("Thay đổi thông tin: ")
        if lable_properties[select - 1] == "Thoát" and property:
            return
        elif property is None:
            while True:
                is_username_exists = False
                tmp_username = input('Nhập tên đăng nhập: ')
                if vi.check_username(tmp_username):
                    for x in (user_data.get_dict_user_from_json()['list_admin'] + user_data.get_dict_user_from_json()['list_client']):
                        if tmp_username == x['username']:
                            is_username_exists = True
                            print("Tên đăng nhập đã được sử dụng!")
                            break
                    if is_username_exists == True:
                        continue
                    else:
                        break
                else:
                    print("Tên đăng nhập phải có 8 ký tự bao gồm chữ thường, chữ in hoa, chữ số")
                    continue
            while True:
                tmp_password = input('Vui lòng nhập mật khẩu: ')
                if not vi.check_password(tmp_password):
                    print("Mật khẩu có ít nhất 8 ký tự, bắt đầu bằng chữ in hoa")
                    continue
                else:
                    break
            while True:
                password_again = input('Nhập lại mật khẩu: ')
                if (tmp_password == password_again):
                    tmp_password = tmp_password
                    break
                else:
                    print("Mật khẩu không giống!")
                    continue 

            while True :
                tmp_name = input("Nhập họ tên: ")
                if not vi.check_name(tmp_name):
                    print('Tên không hợp lệ')
                    continue
                else:
                    break
            while True:
                tmp_mail = input("Nhập email: ")
                if not vi.check_email(tmp_mail):
                    print('Email không hợp lệ')
                    continue
                else:
                    break
            while True:
                tmp_phone_num = input("Nhập số điện thoại: ")
                if not vi.check_phone_number(tmp_phone_num):
                    print('Số điện thoại bắt đầu bằng 0 hoặc 84 và có 9 chữ số phía sau')
                    continue
                else:
                    break
            lable = "Giới tính (1: Nữ / 2: Nam): "
            tmp_gender = input(lable)
            tmp_gender = vi.validate_amout_input_field(tmp_gender,lable,1,2) 

            if user_edited != user_data.get_session():
                lable_input = "Trạng thái (0: Không hoạt động | 1: Hoạt động):"
                tmp_status = input(lable_input)
                tmp_status = vi.validate_amout_input_field(tmp_status, lable_input,0,1)
            else:
                tmp_status = 1
            #Lưu dữ liệu vào 1 biến nhớ tạm
            tmp = [tmp_name,tmp_username,tmp_phone_num,tmp_mail,tmp_gender,tmp_status]
            for field, item in zip(tmp,properties):
                user_edited[item] = field
        elif property == 'name':
            while True :
                user_edited[property] = input("Nhập họ tên: ")
                if not vi.check_name(user_edited[property]):
                    print('Tên không hợp lệ')
                    continue
                else:
                    break
        elif property == 'username':
            while True:
                is_username_exists = False
                user_edited[property] = input('Nhập tên đăng nhập: ')
                if vi.check_username(user_edited[property]):
                    for x in (user_data.get_dict_user_from_json()['list_admin'] + user_data.get_dict_user_from_json()['list_client']):
                        if user_edited[property] == x['username']:
                            is_username_exists = True
                            print("Tên đăng nhập đã được sử dụng!")
                            break
                    if is_username_exists == True:
                        continue
                    else:
                        break
                else:
                    print("Tên đăng nhập phải có 8 ký tự bao gồm chữ thường, chữ in hoa hoặc chữ số")
                    continue
        elif property == 'password':
            while True:
                user_edited[property] = input('Vui lòng nhập mật khẩu: ')
                if not vi.check_password(user_edited[property]):
                    print("Mật khẩu có ít nhất 8 ký tự, bắt đầu bằng chữ in hoa")
                    continue
                else:
                    break
            while True:
                password_again = input('Nhập lại mật khẩu: ')
                if (user_edited[property] == password_again):
                    break
                else:
                    print("Mật khẩu không giống!")
                    continue 
        elif property == 'phone_num':
            while True:
                user_edited[property] = input("Nhập số điện thoại: ")
                if not vi.check_phone_number(user_edited[property]):
                    print('Số điện thoại bắt đầu bằng 0 hoặc 84 và có 9 chữ số phía sau')
                    continue
                else:
                    break
        elif property == 'mail':
            while True:
                user_edited[property] = input("Nhập email: ")
                if not vi.check_email(user_edited[property]):
                    print('Email không hợp lệ')
                    continue
                else:
                    break
        elif property == 'gender':
            lable_input = "Giới tính (1: Nữ | 2: Nam):"
            user_edited[property] = input(lable_input)
            user_edited[property] = vi.validate_amout_input_field(user_edited[property], lable_input,1,2)
        #Khong cho phep chinh sua trang thai hoat dong cua ban than
        elif property == 'status' and user_edited != user_data.get_session():
            lable_input = "Trạng thái (0: Không hoạt động | 1: Hoạt động):"
            user_edited[property] = input(lable_input)
            user_edited[property] = vi.validate_amout_input_field(user_edited[property], lable_input,0,1)
        #Lưu vào data
        user_data.save_user_to_json_file(user_edited,index,user_edited['role'])

        if user_data.get_session()['role'] == 0:
            user_data.save_session_to_json(user_edited)
            self.edit_user(user_data.get_session())

        if user_auth.Auth().is_admin():
            if user is None:
                self.xuat_tt_all_user()
            else:
                self.xuat_tt_all_user(list_user=[user_data.get_dict_user_from_json()[('list_client' if user_edited['role'] == 0 else "list_admin")][index]])
        