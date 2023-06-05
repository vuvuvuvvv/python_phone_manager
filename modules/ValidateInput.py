def ValidateAmountInputForm(val,lable = None,min = None,max = None):
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