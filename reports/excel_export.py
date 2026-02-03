import os
from core.storage import load_json
import pandas as pd

# مسیر روت پروژه
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SALES_FILE = os.path.join(BASE_DIR, "sales.json")
PRODUCTS_FILE = os.path.join(BASE_DIR, "products.json")

def export_sales_to_excel(filename="sales_report.xlsx"):
    sales = load_json(SALES_FILE)
    products = load_json(PRODUCTS_FILE)

    if not sales:
        print("No sales data to export ⚠️")
        return

    data = []
    total_sales_sum = 0

    for sale_code, info in sales.items():
        product_name = products[info["product_code"]]["name"]
        quantity = info["quantity"]
        unit_price = products[info["product_code"]]["price"]
        total_price = info["total_price"]

        total_sales_sum += total_price

        data.append({
            "Sale Code": sale_code,
            "Product": product_name,
            "Quantity": quantity,
            "Unit Price": unit_price,
            "Total Price": total_price
        })

    df = pd.DataFrame(data)

    total_row = {
        "Sale Code": "TOTAL SALES",
        "Product": "",
        "Quantity": "",
        "Unit Price": "",
        "Total Price": total_sales_sum
    }
    df.loc[len(df)] = total_row
    df.to_excel(filename, index=False)
    print(f"✅ Sales exported to {filename}")
