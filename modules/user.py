try:
    from modules.data import *
    from modules.validate_input import *
    from modules.system_function import *
    from tabulate import tabulate
except ImportError:
    pass

gender = {
    1: 'Nu',
    2: 'Nam'
}

permission = {
    0: 'Khach',
    1: 'Admin'
}

status = {
    0: "Khong hoat dong",
    1: "Hoat dong"
}

class User:
    def __init__(self) -> None:
        self.dict_user = get_dict_user_from_json()
        self.id = None
        self.username = None
        self.password = None
        self.name = None
        self.phone_num = None
        self.mail = None
        self.gender = None #1: Female / 2: Male
        self.address = None
        self.role = 0 #0: customer, 1: admin
        self.status = None
        self.ngay_khoi_tao = None

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
    
    def xuat_tt_all_user(self) -> None:
        get_all_user = self.dict_user['list_admin'] + self.dict_user['list_client']
        data = []
        header = ['Ten nguoi dung','Ten dang nhap','Dien thoai','Email','Gioi tinh','Quyen han','Trang thai']
        for user in get_all_user:
            row = [
                f"{user['name']}",
                f"{user['username']}",
                f"{user['phone_num']}",
                f"{user['mail']}",
                f"{gender[user['gender']]}",
                f"{permission[user['role']]}",
                f"{status[user['status']]}",
            ]
            data.append(row)
        table = tabulate(data, header, tablefmt="grid")
        clear_screen()
        print("DANH SACH NGUOI DUNG")
        print(table)

    def delete_user(self,order_user):
        if len(self.list_dien_thoai) == 0:
            print("Danh sach nguoi dung rong!")
        else:
            order_user = input('Nhap id nguoi muon xoa:')
            order_user = validate_amout_input_field(order_user)
            try:
                with open('./data/client/entries.json', 'w') as file:
                    order_user -= 1
                    all_user = self.dict_user['list_admin'] + self.dict_user['list_client']
                    user_deleted = all_user[order_user]
                    if user_deleted['role'] == 0:
                        index = self.dict_user['list_client'].index(user_deleted)
                        self.dict_user['list_client'].pop(index)
                    else:
                        index = self.dict_user['list_admin'].index(user_deleted)
                        self.dict_user['list_admin'].pop(index)

                    json.dump(self.dict_user, file, indent=4)
                #Renew data
                self.dict_user = get_dict_user_from_json()
            # print("Xóa thành công!")
            except Exception as err:
                print(f"Loi: {err}")