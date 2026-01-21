import app

def main():
    print("Welcome to Inventory Management System")

    while True:
        print("\nChoose an option:")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Delete Item")
        print("4. List Items")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            app.add_item()
        elif choice == "2":
            app.update_item()
        elif choice == "3":
            app.delete_item()
        elif choice == "4":
            app.list_items()
        elif choice == "5":
            print("Exiting the Inventory Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
