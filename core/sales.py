import os
from core.storage import load_json, save_json

BASE_DIR = os.path.dirname(__file__)  # مسیر core/
PRODUCT_FILE = os.path.join(BASE_DIR, "..", "products.json")
SALES_FILE = os.path.join(BASE_DIR, "..", "sales.json")

def add_to_sales(product_code, quantity):
    products = load_json(PRODUCT_FILE)

    if product_code not in products:

        print("The product code is not available ⚠️")
        return None

    if quantity > products[product_code]["stock"]:

        print(f"The {product_code} is out of stock ⚠️")
        return None

    sales = load_json(SALES_FILE)

    if not sales:
        sales_code = "S-1001"

    else:
        last_code = max(int(k.split("-")[1]) for k in sales.keys())
        sales_code = f"S-{last_code + 1}"

    products[product_code]["stock"] -= quantity
    total_price = products[product_code]["price"] * quantity

    sales[sales_code] = {
        "product_code": product_code,
        "quantity": quantity,
        "total_price": total_price,
        }

    save_json(SALES_FILE, sales)
    save_json(PRODUCT_FILE, products)

    return print(f"The Product {product_code}({products[product_code]['name']}) *{quantity} has been sold by PRICE: {total_price}$\n Price for each: {products[product_code]['price']}.")


def sales_list():
    sales = load_json(SALES_FILE)
    if not sales:
        print("No sales data available ⚠️")
    sorted_sales = sorted(sales.items(), key=lambda x: int(x[0].split("-")[1]))
    products = load_json(PRODUCT_FILE)
    for code, info in sorted_sales:
        product_name = products[info["product_code"]]["name"]
        qty = info["quantity"]
        total = info["total_price"]
        print(f"🔴 {code} | {product_name} | {qty} | {total}$")

