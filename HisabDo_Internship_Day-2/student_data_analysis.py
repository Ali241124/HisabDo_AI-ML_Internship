# Student Data Analysis using Pandas

import pandas as pd

# Students dataset

students=[
    {"Name": "Ali", "Age": 22, "Course": "AI", "Marks": 85},
    {"Name": "Ayesha", "Age": 21, "Course": "Data Science", "Marks": 72},
    {"Name": "Ahmed", "Age": 23, "Course": "Software Engineering", "Marks": 91},
    {"Name": "Fatima", "Age": 22, "Course": "Cyber Security", "Marks": 68},
    {"Name": "Usman", "Age": 20, "Course": "AI", "Marks": 77},
    {"Name": "Sara", "Age": 21, "Course": "Computer Science", "Marks": 95},
    {"Name": "Hamza", "Age": 22, "Course": "Data Science", "Marks": 60},
    {"Name": "Zain", "Age": 23, "Course": "AI", "Marks": 88},
    {"Name": "Noor", "Age": 20, "Course": "Information Technology", "Marks": 74},
    {"Name": "Hassan", "Age": 22, "Course": "Software Engineering", "Marks": 81},
]

# Convert List to DataFrame

df = pd.DataFrame(students)

# Display all students

print("-" * 60)
print("ALL STUDENTS")
print("-" * 60)
print(df)

# Display students with marks above 70 

print("\n" + "-" * 60)
print("STUDENTS WITH MARKS ABOVE 70")
print("-" * 60)
above_70 = df[df["Marks"] > 70 ]
print(above_70)

# Average Marks 

average_marks = df["Marks"].mean()
print("\nAverage Marks:", round(average_marks, 2))

# Students with Highest Marks

highest_marks = df.loc[df["Marks"].idxmax()]
print("\nHighest Scoring Student")
print(highest_marks)

# Students with Lowest Marks

lowest_marks = df.loc[df["Marks"].idxmin()]
print("\nLowest Scoring Student")
print(lowest_marks)

# Total Students

total_students = len(df)
print("\nTotal Students:", total_students)