
import json
from pathlib import Path

FILE = Path("passwords.json")

def load_data():
    if FILE.exists():
        return json.loads(FILE.read_text())
    return {}

def save_data(data):
    FILE.write_text(json.dumps(data, indent=2))

while True:
    print("\n=== Password Manager ===")
    print("1. Save Password")
    print("2. View Accounts")
    print("3. Search Account")
    print("4. Exit")

    choice = input("Enter choice: ")

    data = load_data()

    if choice == "1":
        website = input("Website: ")
        username = input("Username: ")
        password = input("Password: ")
        data[website] = {"username": username, "password": password}
        save_data(data)
        print("Saved successfully!")

    elif choice == "2":
        for site, info in data.items():
            print(f"{site} | {info['username']} | {info['password']}")

    elif choice == "3":
        site = input("Enter website: ")
        if site in data:
            print(data[site])
        else:
            print("Account not found")

    elif choice == "4":
        break
