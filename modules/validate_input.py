
import re

def validate_amout_input_field(val,lable = None,min = None,max = None):
    while True:
        try:
            val = int(val)
            if ((val <1) if (min == None) else (val < min)) or ((val>max) if (max != None) else False) or not isinstance(val, int):
                val = 1/0
            else:
                break
        except (ZeroDivisionError,ValueError):
            error_msg = f"Du lieu khong hop le! "
            if max is not None:
                error_msg += f"Du lieu trong khoang {format(min, ',d').replace(',', '.') if min is not None else 1}->{format(max, ',d').replace(',', '.')}"
            else:
                if min is not None:
                    error_msg += f"Du lieu trong khoang {format(min, ',d').replace(',', '.')} tro len."
            print(error_msg)
            val = input(lable)
    return val

def check_username(username):
    pattern = r"^[a-zA-Z0-9]{8,}"
    if re.fullmatch(pattern, username):
        return True
    else:
        return False

def check_password(password):
    pattern = r"^[A-Z][a-zA-Z0-9]{7,}"
    if re.fullmatch(pattern, password):
        return True
    else:
        return False


def check_phone_number(phone):
    pattern = r"^(0|84)\d{10}"
    if re.fullmatch(pattern, phone):
        return True
    else:
        return False


def check_email(email):
    pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
    if re.fullmatch(pattern, email):
        return True
    else:
        return False


def check_name(name):
    pattern = r"^[a-zA-Z\s]+$"
    if re.fullmatch(pattern, name):
        return True
    else:
        return False
    
def checkSelect(desiredRange = []):
    try:
        if not isinstance(desiredRange, list):
            10/0
        select = 0
        while select not in desiredRange or not isinstance(select, int):
            select = input("Nhap lua chon: ")
            if select.isnumeric():
                select = int(select)
            else:
                select = 0
                # pass
                # try:
                #     select = float(select)
                # except ValueError:
                #     pass # skip loop
    except Exception:
        print("Khoang gia tri khong hop le!")
    return select