import json
def save_product_to_json_file(new_data=None):
    try:
        with open("./data/product/product.json", "r") as json_file:
            # Thực hiện các hoạt động trên tệp=
            try:
                data = json.load(json_file)            
                data['products'].append(new_data)
                with open("./data/product/product.json", "w") as json_file:
                    json.dump(data, json_file,indent=4)
            except json.JSONDecodeError as e:
                print("Lỗi xảy ra khi phân tích cú pháp JSON:", str(e))
            except Exception as e:
                print("Lỗi không xác định:", str(e))


    except FileNotFoundError:
        print("Không tìm thấy tệp.")

    except PermissionError:
        print("Không có quyền truy cập vào tệp.")

    except IOError:
        print("Lỗi khi đọc/ghi dữ liệu từ tệp.")
        
def truncate_products():
    try:
        with open("./data/product/product.json", "w") as json_file: 
            # data = {}
            # data['products'] = []
            # json.dump(data, json_file)
            json.dump("", json_file)

    except FileNotFoundError:
        print("Không tìm thấy tệp.")

    except PermissionError:
        print("Không có quyền truy cập vào tệp.")

    except IOError:
        print("Lỗi khi đọc/ghi dữ liệu từ tệp.")