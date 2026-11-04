# Case Study 20: University Admission Decision Engine

students = [
    ("Ravi", 85, 75),
    ("Priya", 92, 80),
    ("Rahul", 68, 60),
    ("Sneha", 78, 65),
    ("Anu", 95, 90)
]

eligible = []

for name, marks, subject_marks in students:
    if marks >= 75 and subject_marks >= 65:
        eligible.append((name, marks, subject_marks))
    else:
        print(name, "is not eligible")

eligible.sort(key=lambda x: (x[1], x[2]), reverse=True)

print("\nEligible Candidates Ranking")

rank = 1

for name, marks, subject_marks in eligible:
    print(rank, name, "Aggregate:", marks,
          "Subject Marks:", subject_marks)
    rank += 1
