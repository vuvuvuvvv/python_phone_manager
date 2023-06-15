import json
import os
import modules.auth as auth_data
import modules.user as data_user

def save_session_to_json(dict_user):
    with open("./data/session/session.json", "w") as json_file:
        json.dump(dict_user, json_file, indent=4)

def get_session():
    with open("./data/session/session.json", "r") as json_file:
        return json.load(json_file)

def delete_session():
    with open("./data/session/session.json", "w") as json_file:
        json.dump("",json_file, indent=4)

def save_product_to_json_file(new_data=None, index=None):
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

def truncate_product_data():
    try:
        with open("./data/product/product.json", "w") as json_file:
            data = {}
            data['products'] = []
            json.dump(data, json_file)
    except Exception as err:
        print(f"Loi: {err}")

def get_dict_product_from_json():
    try:
        with open("./data/product/product.json", "r") as product_json_file:
            data = json.load(product_json_file)
            test = len(data['products'])
    except Exception:
        truncate_product_data()

    with open("./data/product/product.json", "r") as product_json_file:
        data = json.load(product_json_file)
    try:
        return data['products']
    except Exception:
        with open("./data/product/product.json", "w") as json_file:
            data['products'] = []
            json.dump(data, json_file, indent=4)
        return data['products']

def truncate_user_data():
    data = {} 
    data['products'] = []
    with open("./data/product/product.json", "w") as json_file:
        json.dump(data, json_file, indent=4)


def get_dict_user_from_json():
    try:
        with open("./data/client/entries.json", "r") as user_json_file:
            try:
                data = json.load(user_json_file)
                return data
            except Exception as err:
                print(f"Loi: {err}")
    except Exception as err:
        print(f"Loi: {err}")
    return

def save_user_to_json_file(new_data=None, index=None, role=None):
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
    return

def truncate_cart_data():
    data = {}
    data['cart'] = {}
    data['cart']['1'] = []
    with open("./data/cart/cart.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
    return


def get_cart_item_from_json():
    try:
        with open("./data/cart/cart.json", "r") as cart_json_file:
            data = json.load(cart_json_file)
            test = len(data['cart'])
    except Exception:
        truncate_cart_data()

    with open("./data/cart/cart.json", "r") as cart_json_file:
        data = json.load(cart_json_file)
    try:
        return data['cart'][str(get_session()['id'])]
    except Exception:
        with open("./data/cart/cart.json", "w") as json_file:
            data['cart'][str(get_session()['id'])] = []
            json.dump(data, json_file, indent=4)
        return data['cart'][str(get_session()['id'])]


def save_cart_item_to_json_file(cart_item):
    # TODO
    try:
        with open("./data/cart/cart.json", "r") as cart_json_file:
            data = json.load(cart_json_file)
            test = len(data['cart'])
    except Exception:
        truncate_cart_data()

    with open("./data/cart/cart.json", "r") as cart_json_file:
        data = json.load(cart_json_file)
    try:
        data['cart'][str(get_session()['id'])].append(cart_item)
        with open("./data/cart/cart.json", "w") as json_file:
            json.dump(data, json_file, indent=4)
    except Exception:
        with open("./data/cart/cart.json", "w") as json_file:
            data['cart'][str(get_session()['id'])] = []
            data['cart'][str(get_session()['id'])].append(cart_item)
            json.dump(data, json_file, indent=4)
    return


def update_cart_item_to_json_file(cart_item):
    with open("./data/cart/cart.json", "r") as cart_json_file:
        data = json.load(cart_json_file)
        for item in data['cart'][str(get_session()['id'])]:
            if cart_item['product'] == item['product']:
                data['cart'][str(get_session()['id'])][data['cart'][str(
                    get_session()['id'])].index(item)]['quantity'] = cart_item['quantity']
                break
    with open("./data/cart/cart.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
    return


def truncate_order_data():
    data = {}
    data['order'] = {}
    data['order'][str(get_session()['id'])] = []
    with open("./data/order/order.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
    return


def get_order_from_json():
    try:
        with open("./data/order/order.json", "r") as order_json_file:
            data = json.load(order_json_file)
            test = len(data['order'])
    except Exception:
        truncate_order_data()

    with open("./data/order/order.json", "r") as order_json_file:
        data = json.load(order_json_file)
    try:
        return data['order'][str(get_session()['id'])]
    except Exception:
        with open("./data/order/order.json", "w") as json_file:
            data['order'][str(get_session()['id'])] = []
            json.dump(data, json_file, indent=4)
        return data['order'][str(get_session()['id'])]

def get_all_order_from_json():
    with open("./data/order/order.json", "r") as order_json_file:
        data = json.load(order_json_file)
    try:
        return data['order']
    except Exception:
        truncate_order_data()
        get_all_order_from_json()
    return


def save_order_item_to_json_file(order_item):
    # TODO
    try:
        with open("./data/order/order.json", "r") as order_json_file:
            data = json.load(order_json_file)
            test = len(data['order'])
    except Exception:
        truncate_order_data()

    with open("./data/order/order.json", "r") as order_json_file:
        data = json.load(order_json_file)
    try:
        data['order'][str(get_session()['id'])].append(order_item)
        with open("./data/order/order.json", "w") as json_file:
            json.dump(data, json_file, indent=4)
    except Exception:
        with open("./data/order/order.json", "w") as json_file:
            data['order'][str(get_session()['id'])] = []
            data['order'][str(get_session()['id'])].append(order_item)
            json.dump(data, json_file, indent=4)
    return