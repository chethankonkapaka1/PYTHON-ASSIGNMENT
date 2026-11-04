# Case Study 10: Campus Event Financial Planning

venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost: "))
transport = float(input("Enter transport cost: "))
certificates = float(input("Enter certificate cost: "))

sponsorship = float(input("Enter sponsorship amount: "))
fee = float(input("Enter registration fee per student: "))

total_expenses = venue + equipment + catering + transport + certificates

print("\nTotal Event Expenses:", total_expenses)

remaining = total_expenses - sponsorship

if remaining > 0:
    print("Sponsorship Shortfall:", remaining)
else:
    print("Sponsorship covers all expenses")

if fee > 0:
    students = int(remaining / fee)

    if remaining % fee != 0:
        students += 1

    if students < 0:
        students = 0

    print("Minimum Registrations Needed:", students)
else:
    print("Registration fee must be greater than zero")
