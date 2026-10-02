employees = {}

while True:
    print("\n1. Add")
    print("2. Remove")
    print("3. Search")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter employee name: ")
        department = input("Enter department: ")

        employees[name] = department
        print("Employee added.")

    elif choice == "2":
        name = input("Enter employee name: ")

        if name in employees:
            del employees[name]
            print("Employee removed.")
        else:
            print("Employee not found.")

    elif choice == "3":
        name = input("Enter employee name: ")

        if name in employees:
            print("Department:", employees[name])
        else:
            print("Employee not found.")

    elif choice == "4":
        for name, department in employees.items():
            print(name, ":", department)

    elif choice == "5":
        break

    else:
        print("Invalid choice.")