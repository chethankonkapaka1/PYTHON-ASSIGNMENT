# Case Study 70: Scholarship Shortlisting

students = [
    ("Ravi", 85, 90, 150000),
    ("Priya", 95, 95, 100000),
    ("Rahul", 70, 80, 120000),
    ("Sneha", 88, 85, 200000),
    ("Anu", 92, 92, 90000)
]

quota = 3
eligible = []

for name, marks, attendance, income in students:
    if marks >= 80 and attendance >= 75 and income <= 150000:
        eligible.append((name, marks, attendance, income))

eligible.sort(key=lambda x: x[1], reverse=True)

print("Scholarship Shortlist:")

for i in range(min(quota, len(eligible))):
    name, marks, attendance, income = eligible[i]
    print(i + 1, name, "Marks:", marks,
          "Attendance:", attendance, "Income:", income)

print("Total Selected:", min(quota, len(eligible)))
