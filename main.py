from core.product import list_product, add_product
from core.sales import add_to_sales, sales_list
from utils.security import *
from reports.excel_export import export_sales_to_excel


is_password_set()

def show_menu():
    print("\n=== Store Management System ===")
    print("1. List products")
    print("2. Selling")
    print("3. Add product (Admin)")
    print("4. Record sale")
    print("5. Export sales to Excel (Admin)")
    print("0. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "0":
            print("Bye 👋")
            break

        elif choice == "1":
            list_product()

        elif choice == "2":
            product_code = input("Enter product code: ")
            quantity = int(input("Enter quantity: "))
            add_to_sales(product_code, quantity)

        elif choice == "3":
            res = check_password(input("Enter password: "))
            if res == True:
                add_product(input("Enter product name: "), float(input("Enter price: ")), int(input("Enter quantity:")))
            else:
                print("Wrong password")


        elif choice == "4":
            sales_list()

        elif choice == "5":
            export_sales_to_excel()


        else:
            print("Invalid choice ⚠️")


if __name__ == "__main__":
    main()
