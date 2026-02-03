import os

BASE_DIR = os.path.dirname(__file__)
ADMIN_PASSWORD_FILE = os.path.join(BASE_DIR, "..", "admin.txt")

def set_password(password):
    with open(ADMIN_PASSWORD_FILE, "w") as f:
        f.write(password)

def check_password(password):
    with open(ADMIN_PASSWORD_FILE, "r", encoding="utf-8") as f:
        password_file = f.read()
    if password == password_file:
        print("Access granted ✅")
        return True
    else:
        print("Access denied ❌")
        return False

def is_password_set():
    if os.path.exists(ADMIN_PASSWORD_FILE):
        return True
    else:
        set_password(input("Please set password for admin: "))
        return True