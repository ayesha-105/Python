from item_class import Item
from filehandling import load_data, save_data, new_id

def add_item():
    items=load_data()
    while True:
        try:
            item_id= new_id(items)
            print(f"This new item id is {item_id}")
            item_name= input("Enter your item name: ").strip()
            if not item_name:
                print("This is required field.")
                continue
            item_category= input("Enter your item category: ").strip()
            if not item_category:
                print("This is required field..")
                continue
            quantity= int(input("Enter item quantity: "))
            if not quantity:
                print("This is required field.")
                continue
            supplier= input("Enter your item supplier: ").strip()
            if not supplier:
                print("This is required field.")
                continue
            price_per_unit= float(input("Enter price per unit: "))
            if not price_per_unit:
                print("This is required field.")
                continue
            expiry_date= input("Enter expiry date in this format (YYYY-MM-DD): ").strip()
            if not expiry_date:
                print("This is required field.")
                continue

            # create object for save the attributes values
            item = Item(
                item_id,
                item_name,
                item_category,
                quantity,
                supplier,
                price_per_unit,
                expiry_date
            )

            # conver obejtc to dictionary
            items.append(item.to_dict())
            save_data(items)
            print("The item has been added successfully.")
           
        except ValueError:
            print("Invalid input. Please enter correct values.")
            continue
        choice= input("Do you want to add another item? (yes/no): ").lower()
        if choice != "yes":
            break

def update_item():
    items = load_data()

    while True:
        try:
            id = int(input("Enter Item ID to update (or 0 to go back): "))
            if id == 0:
                print("Main menu.")
                break

            item = None
            for i in items:
                if i["item_id"] == id:
                    item = i
                    break

            if not item:
                print("This item ID not found, please enter a valid ID.")
                continue

            print(f"\nCurrent Item Data: {item}")

            while True:
                print("\nWhich field do you want to update?")
                print("1. Item Name")
                print("2. Category")
                print("3. Quantity")
                print("4. Supplier")
                print("5. Price per Unit")
                print("6. Expiry Date")
                print("7. Exit (Save & Go Back)")

                choice = input("Enter your choice (1-7): ")

                if choice == "1":
                    item["item_name"] = input("Enter new item name: ").strip()

                elif choice == "2":
                    item["item_category"] = input("Enter new category: ").strip()

                elif choice == "3":
                    item["quantity"] = int(input("Enter new quantity: "))

                elif choice == "4":
                    item["supplier"] = input("Enter new supplier: ").strip()

                elif choice == "5":
                    item["price_per_unit"] = float(input("Enter new price per unit: "))

                elif choice == "6":
                    item["expiry_date"] = input(
                        "Enter new expiry date (YYYY-MM-DD): "
                    ).strip()

                elif choice == "7":
                    save_data(items)
                    print("Item record updated successfully!")
                    return

                else:
                    print("Invalid choice. Try again.")

        except ValueError:
            print("Invalid input. Please enter correct numeric values.")

