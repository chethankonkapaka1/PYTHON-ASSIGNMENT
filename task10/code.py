# Case Study 100: Smart Campus Management

students = []
events = []
resources = []

while True:
    print("\n--- SMART CAMPUS MANAGEMENT ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Register for Event")
    print("4. Allocate Resources")
    print("5. View Summary")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        attendance = float(input("Enter attendance percentage: "))
        marks = float(input("Enter marks: "))

        students.append((name, attendance, marks))
        print("Student added successfully")

    elif choice == "2":
        if len(students) == 0:
            print("No student records found")
        else:
            for name, attendance, marks in students:
                print("\nName:", name)
                print("Attendance:", attendance, "%")
                print("Marks:", marks)

                if attendance >= 75 and marks >= 40:
                    print("Status: Eligible")
                else:
                    print("Status: Not Eligible")

    elif choice == "3":
        name = input("Enter student name: ")
        event = input("Enter event name: ")

        events.append((name, event))
        print("Event registration successful")

    elif choice == "4":
        resource = input("Enter resource name: ")
        quantity = int(input("Enter quantity: "))

        if quantity > 0:
            resources.append((resource, quantity))
            print("Resource allocated successfully")
        else:
            print("Invalid quantity")

    elif choice == "5":
        print("\n--- CAMPUS SUMMARY ---")
        print("Total Students:", len(students))
        print("Total Event Registrations:", len(events))
        print("Total Resource Allocations:", len(resources))

        print("\nEvent Registrations:")
        for name, event in events:
            print(name, "-", event)

        print("\nResource Allocations:")
        for resource, quantity in resources:
            print(resource, "-", quantity)

    elif choice == "6":
        print("Thank you for using Smart Campus Management")
        break

    else:
        print("Invalid choice. Please try again.")
