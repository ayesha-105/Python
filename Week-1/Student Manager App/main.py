import app

def main():
    print("Welcome to Student Manager App")
    while True:
        print("\nChoose an option:")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. List Students")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            app.add_student()
        elif choice == "2":
            app.update_student()
        elif choice == "3":
            app.delete_student()
        elif choice == "4":
            app.list_students()
        elif choice == "5":
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
if __name__ == "__main__":   
    main()
