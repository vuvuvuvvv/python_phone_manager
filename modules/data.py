import json
import os
import modules.auth as auth_data
import modules.user as data_user


def save_product_to_json_file(new_data=None, index=None) -> None:
    try:
        with open("./data/product/product.json", "r") as json_file:
            try:
                data = json.load(json_file)
                if index is None:
                    data['products'].append(new_data)
                else:
                    data['products'][index] = new_data
                with open("./data/product/product.json", "w") as json_file:
                    json.dump(data, json_file, indent=4)
            except Exception as err:
                print(f"Loi: {err}")
    except Exception as err:
        print(f"Loi: {err}")


def truncate_product_data() -> None:
    try:
        with open("./data/product/product.json", "w") as json_file:
            data = {}
            data['products'] = []
            json.dump(data, json_file)
    except Exception as err:
        print(f"Loi: {err}")


def get_dict_product_from_json() -> None:
    try:
        with open("./data/product/product.json", "r") as product_json_file:
            try:
                data = json.load(product_json_file)
                return data['products']
            except Exception as err:
                print(f"Loi: {err}")
    except Exception as err:
        print(f"Loi: {err}")


def truncate_user_data() -> None:
    try:
        with open("./data/client/entries.json", "w") as json_file:
            data = {}
            data['list_admin'] = []
            data['list_client'] = []
            json.dump(data, json_file, indent=4)
    except Exception as err:
        print(f"Loi: {err}")


def get_dict_user_from_json() -> None:
    try:
        with open("./data/client/entries.json", "r") as user_json_file:
            try:
                data = json.load(user_json_file)
                return data
            except Exception as err:
                print(f"Loi: {err}")
    except Exception as err:
        print(f"Loi: {err}")


def save_user_to_json_file(new_data=None, index=None, role=None) -> None:
    try:
        with open("./data/client/entries.json", "r") as user_json_file:
            try:
                data = json.load(user_json_file)
                if index is None:
                    data['list_client'].append(new_data)
                else:
                    data[('list_client' if role == 0 else "list_admin")
                          ][index] = new_data
                with open("./data/client/entries.json", "w") as json_file:
                    json.dump(data, json_file, indent=4)
            except Exception as err:
                print(f"Loi (in: {os.path.abspath(__file__)}): {err}")
    except Exception as err:
        print(f"Loi (in: {os.path.abspath(__file__)}): {err}")


def truncate_cart_data() -> None:
    data = None
    with open("./data/cart/cart.json", "r") as user_json_file:
        data = json.load(user_json_file)
        data['cart'][str(auth_data.Auth().session_user['id'])] = []
    with open("./data/cart/cart.json", "w") as json_file:
        json.dump(data, json_file, indent=4)


def get_dict_cart_from_json() -> None:
    auth = auth_data.Auth()
    while True:
        try:
            with open("./data/cart/cart.json", "r") as user_json_file:
                data = json.load(user_json_file)
            return data['cart'][str(auth.session_user['id'])]
        except Exception:
            truncate_cart_data()


def save_cart_item_to_json_file(cart_item):
    auth = auth_data.Auth()
    # TODO
    with open("./data/cart/cart.json", "r") as user_json_file:
        data = json.load(user_json_file)
        try:
            len(data['cart'][str(auth.session_user['id'])])
        except Exception:
            data['cart'][str(auth.session_user['id'])] = []
        data['cart'][str(auth.session_user['id'])].append(cart_item)
    with open("./data/cart/cart.json", "w") as json_file:
        json.dump(data, json_file, indent=4)


def update_cart_item_to_json_file(cart_item):
    auth = auth_data.Auth()
    with open("./data/cart/cart.json", "r") as user_json_file:
        data = json.load(user_json_file)
        for item in data['cart'][str(auth.session_user['id'])]:
            if cart_item['product'] == item['product']:
                data['cart'][str(auth.session_user['id'])][data['cart'][str(
                    auth.session_user['id'])].index(item)]['quantity'] = cart_item['quantity']
                break
    with open("./data/cart/cart.json", "w") as json_file:
        json.dump(data, json_file, indent=4)


def truncate_order_data() -> None:
    try:
        with open("./data/order/order.json", "r") as user_json_file:
            data = json.load(user_json_file)
            len(data['order'])
    except Exception:
        data = {}
        data['order'] = {}
        data['order'][str(auth_data.Auth().session_user['id'])] = []
        with open("./data/order/order.json", "w") as json_file:
            json.dump(data, json_file, indent=4)


def get_dict_order_from_json() -> None:
    auth = auth_data.Auth()
    while True:
        try:
            with open("./data/order/order.json", "r") as user_json_file:
                data = json.load(user_json_file)
            return data['order'][str(auth.session_user['id'])]
        except Exception:
            truncate_order_data()
            get_dict_order_from_json()

def get_all_order_from_json() -> None:
    while True:
        try:
            with open("./data/order/order.json", "r") as user_json_file:
                data = json.load(user_json_file)
            return data['order']
        except Exception:
            truncate_order_data()
            get_all_order_from_json()


def save_order_item_to_json_file(order_item):
    auth = auth_data.Auth()
    # TODO
    try:
        with open("./data/order/order.json", "r") as user_json_file:
            data = json.load(user_json_file)
            test = len(data['order'])
    except Exception:
        truncate_order_data()

    with open("./data/order/order.json", "r") as user_json_file:
        data = json.load(user_json_file)
    try:
        data['order'][str(auth.session_user['id'])].append(order_item)
        with open("./data/order/order.json", "w") as json_file:
            json.dump(data, json_file, indent=4)
    except Exception:
        with open("./data/order/order.json", "w") as json_file:
            data['order'][str(auth.session_user['id'])] = []
            data['order'][str(auth.session_user['id'])].append(order_item)
            json.dump(data, json_file, indent=4)