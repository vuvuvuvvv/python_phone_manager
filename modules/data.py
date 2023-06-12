import json
def save_product_to_json_file(new_data=None) -> None:
    try:
        with open("./data/product/product.json", "r") as json_file:
            # Thực hiện các hoạt động trên tệp=
            try:
                data = json.load(json_file)            
                data['products'].append(new_data)
                with open("./data/product/product.json", "w") as json_file:
                    json.dump(data, json_file,indent=4)
            except Exception as err:
                print(f"Loi: {err}")
    except Exception as err:
        print(f"Loi: {err}")
        
def truncate_product_data() -> None:
    try:
        with open("./data/product/product.json", "w") as json_file: 
            json.dump("", json_file)
    except Exception as err:
        print(f"Loi: {err}")
        
def truncate_user_data() -> None:
    try:
        with open("./data/client/entries.json", "w") as json_file: 
            data = {}
            data['list_admin'] = []
            data['list_client'] = []
            json.dump(data, json_file,indent=4)
    except Exception as err:
        print(f"Loi: {err}")

def get_dict_product_from_json() -> None:
    try:
        with open("./data/product/product.json", "r") as product_json_file:
            # Thực hiện các hoạt động trên tệp
            try:
                data = json.load(product_json_file)        
                return data
            except Exception as err:
                print(f"Loi: {err}")
    except Exception as err:
        print(f"Loi: {err}")

def get_dict_user_from_json() -> None:
    try:
        with open("./data/client/entries.json", "r") as user_json_file:
            # Thực hiện các hoạt động trên tệp
            try:
                data = json.load(user_json_file)        
                return data
            except Exception as err:
                print(f"Loi: {err}")
    except Exception as err:
        print(f"Loi: {err}")

def save_user_to_json_file(new_data=None) -> None:
    try:
        with open("./data/client/entries.json", "r") as user_json_file:
            # Thực hiện các hoạt động trên tệp
            try:
                data = json.load(user_json_file)            
                data['list_client'].append(new_data)
                with open("./data/product/product.json", "w") as json_file:
                    json.dump(data, json_file,indent=4)
            except Exception as err:
                print(f"Loi: {err}")
    except Exception as err:
        print(f"Loi: {err}")