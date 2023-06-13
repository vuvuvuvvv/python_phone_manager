try:
    from modules.auth import *
except Exception as err:
    print(f"Loi: {err}")

class Cart():
    def __init__(self) -> None:
        self.id = None
        self.user_id = None
        self.status = 1
        self.ngay_khoi_tao = None

    def add_to_cart():
        auth = Auth()
        uid = auth.session_user['id']