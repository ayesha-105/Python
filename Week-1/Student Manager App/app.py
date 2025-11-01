from filehandling import load_data, save_data

#    CRUD Operations
def add_student(): 
    students= load_data()
    while True:
        try:
            id= int(input("Enter Student Id: "))
            if any(s["Id"]==id for s in students):
                print("Student with this Id already exists. Enter a unique Id.")
                continue
            name= input("Enter student name: ")
            age= input("Enter student age: ")
            dept= input("Enter student department: ")

            students.append({"Id": id, "Name": name, "Age": age, "Department": dept})
            save_data(students)
            print("Student record added successfully!")

        except ValueError:
            print("Invalid input. Please enter correct values.")
            continue

        choice= input("Do you want to add another student record? (yes / no): ").strip().lower()
        if choice != "yes":
            break

def update_student():
    students = load_data()

    while True:
        try:
            id = int(input("Enter ID to update (or 0 to go back): "))
            if id == 0:
                print("Main menu.")
                break

            student = None
            for s in students:
                if s["Id"] == id:
                    student = s
                    break

            if not student:
                print("This student ID not found, please enter a valid ID.")
                continue 

            print(f"\nCurrent Data: {student}")

            while True:
                print("\nWhich field do you want to update?")
                print("1. Name")
                print("2. Age")
                print("3. Department")
                print("4. Exit (Save & Go Back)")

                choice = input("Enter your choice (1-4): ")

                if choice == "1":
                    student["Name"] = input("Enter new name: ")
                elif choice == "2":
                    student["Age"] = input("Enter new age: ")
                elif choice == "3":
                    student["Department"] = input("Enter new department: ")
                elif choice == "4":
                    save_data(students)
                    print("Student record updated successfully!")
                    return 
                else:
                    print("Invalid choice. Try again.")

        except ValueError:
            print("Invalid input. Please enter a valid numeric ID.")

def delete_student():
    students = load_data()

    while True:
        try:
            id = int(input("Enter student ID to delete (or 0 to go back): "))
            if id == 0:
                print("Main menu.")
                break

            student = None
            for s in students:
                if s["Id"] == id:
                    student = s
                    break

            if not student:
                print("Student ID not found, please enter a valid ID.")
                continue

            students.remove(student)
            save_data(students)
            print(f"Student record with ID {id} deleted successfully!")

        except ValueError:
            print("Invalid input. Please enter a valid numeric ID.")
            continue
def list_students():
    students = load_data()
    if not students:
        print("No students found.")
        return
    print("\n  Student List  ")
    for s in students:
        print(f"ID: {s['Id']}, Name: {s['Name']}, Age: {s['Age']}, Department: {s['Department']}")
    
        
            




  

    

