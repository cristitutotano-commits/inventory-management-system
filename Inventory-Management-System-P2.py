"""
Inventory Management System - Period 2
ITE 260 Computer Programming 1
"""

products = []  # List storing products as [name, quantity, price]

def add_product():
    name = input("Enter product name: ").strip()
    if not name:
        print("[ERROR] Product name cannot be empty!")
        return
    
    # Check duplicate
    for p in products:
        if p[0].lower() == name.lower():
            print(f"[ERROR] Product '{name}' already exists!")
            return

    try:
        quantity = int(input("Enter quantity: "))
        if quantity < 0:
            print("[ERROR] Quantity cannot be negative!")
            return
    except ValueError:
        print("[ERROR] Invalid quantity! Must be a number.")
        return

    try:
        price = float(input("Enter price: "))
        if price < 0:
            print("[ERROR] Price cannot be negative!")
            return
    except ValueError:
        print("[ERROR] Invalid price! Must be a number.")
        return

    products.append([name, quantity, price])
    print(f"[SUCCESS] Product '{name}' added successfully!")


def view_products():
    if not products:
        print("[INFO] No products in inventory.")
        return
    
    print(f"\n{'NAME':<20} {'QTY':<10} {'PRICE':<10} {'TOTAL VALUE':<12}")
    print("-" * 60)
    for p in products:
        total = p[1] * p[2]
        print(f"{p[0]:<20} {p[1]:<10} {p[2]:<10.2f} {total:<12.2f}")


def search_product():
    if not products:
        print("[INFO] Inventory is empty.")
        return

    name = input("Enter product name to search: ").strip().lower()
    if not name:
        print("[ERROR] Search term cannot be empty!")
        return

    found = False
    for p in products:
        if name in p[0].lower():
            print(f"\nFound: Name={p[0]}, Qty={p[1]}, Price={p[2]:.2f}, Total={p[1]*p[2]:.2f}")
            found = True
    
    if not found:
        print(f"[ERROR] Product '{name}' not found!")


def update_product():
    name = input("Enter product name to update: ").strip()
    if not name:
        print("[ERROR] Name cannot be empty!")
        return

    for p in products:
        if p[0].lower() == name.lower():
            print(f"Current: Qty={p[1]}, Price={p[2]}")
            try:
                new_qty = input(f"Enter new quantity (or press Enter to keep {p[1]}): ").strip()
                if new_qty:
                    new_qty = int(new_qty)
                    if new_qty < 0:
                        print("[ERROR] Quantity cannot be negative!")
                        return
                    p[1] = new_qty

                new_price = input(f"Enter new price (or press Enter to keep {p[2]}): ").strip()
                if new_price:
                    new_price = float(new_price)
                    if new_price < 0:
                        print("[ERROR] Price cannot be negative!")
                        return
                    p[2] = new_price

                print(f"[SUCCESS] Product '{p[0]}' updated!")
            except ValueError:
                print("[ERROR] Invalid number format!")
            return

    print(f"[ERROR] Product '{name}' not found!")


def stock_in():
    name = input("Enter product name for Stock In: ").strip()
    if not name:
        print("[ERROR] Name cannot be empty!")
        return

    for p in products:
        if p[0].lower() == name.lower():
            try:
                add_qty = int(input("Enter quantity to add: "))
                if add_qty <= 0:
                    print("[ERROR] Stock In quantity must be greater than 0!")
                    return
                # Arithmetic expression
                p[1] = p[1] + add_qty
                print(f"[SUCCESS] Stock In successful! New Qty of '{p[0]}': {p[1]}")
            except ValueError:
                print("[ERROR] Invalid quantity!")
            return

    print(f"[ERROR] Product '{name}' not found!")


def stock_out():
    name = input("Enter product name for Stock Out: ").strip()
    if not name:
        print("[ERROR] Name cannot be empty!")
        return

    for p in products:
        if p[0].lower() == name.lower():
            try:
                remove_qty = int(input("Enter quantity to remove: "))
                if remove_qty <= 0:
                    print("[ERROR] Stock Out quantity must be greater than 0!")
                    return
                # Validation: cannot remove more than available - comparison + logical
                if remove_qty > p[1]:
                    print(f"[ERROR] Insufficient stock! Available: {p[1]}, Requested: {remove_qty}")
                    return
                # Arithmetic expression
                p[1] = p[1] - remove_qty
                print(f"[SUCCESS] Stock Out successful! Remaining Qty of '{p[0]}': {p[1]}")
                
                # Low stock warning - logical expression
                if p[1] <= 5 and p[1] > 0:
                    print(f"[WARNING] Low stock for '{p[0]}'! Only {p[1]} left.")
                elif p[1] == 0:
                    print(f"[WARNING] '{p[0]}' is now out of stock!")
            except ValueError:
                print("[ERROR] Invalid quantity!")
            return

    print(f"[ERROR] Product '{name}' not found!")


def main_menu():
    while True:
        print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Stock In")
        print("6. Stock Out")
        print("7. Exit")
        
        choice = input("Select option (1-7): ").strip()

        # Decision-making logic with if/elif/else
        if choice == "1":
            add_product()
        elif choice == "2":
            view_products()
        elif choice == "3":
            search_product()
        elif choice == "4":
            update_product()
        elif choice == "5":
            stock_in()
        elif choice == "6":
            stock_out()
        elif choice == "7":
            print("Exiting system. Thank you!")
            break
        else:
            print("[ERROR] Invalid choice! Please select 1-7.")

if __name__ == "__main__":
    main_menu()
