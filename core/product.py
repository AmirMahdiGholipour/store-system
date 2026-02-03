import os
from core.storage import load_json, save_json

BASE_DIR = os.path.dirname(__file__)  # مسیر core/
PRODUCT_FILE = os.path.join(BASE_DIR, "..", "products.json")

def add_product(name, price, stock):
    products = load_json(PRODUCT_FILE)
    if products:
        last_code = max(int(k.split("-")[1]) for k in products.keys())
        new_code = f"P-{last_code + 1}"
    else:
        new_code = "P-1001"

    products[new_code] = {
        "name": name,
        "price": price,
        "stock": stock
    }

    save_json(PRODUCT_FILE, products)
    return new_code, print(new_code)

def list_product():
    products = load_json(PRODUCT_FILE)
    if not products:
        print("No products found.")
        return
    for code, info in products.items():
        print(f"{code} | {info['name']} | {info['price']} | {info['stock']}")

