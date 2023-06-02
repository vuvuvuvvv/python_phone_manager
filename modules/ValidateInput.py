def ValidateAmountInputForm(val,lable = None,min = None,max = None):
    while True:
        try:
            val = int(val)
            if ((val <1) if (min == None) else (val < min)) or ((val>max) if (max != None) else False) or not isinstance(val, int):
                val = 1/0
            else:
                break
        except (ZeroDivisionError,ValueError):
            print(f"Du lieu khong hop le! {f'Trong khoang {min if min else 1} ' + ('->'if(max) else 'tro len') + f' {max}' if (max) else '':}")
            val = input(lable)
    return val