# Import Libraries

import pandas as pd 
import matplotlib.pyplot as plt

# Load Dataset

df = pd.read_excel("student_performance_dataset.xlsx")

# Display Dataset

print("-"*60)
print("Student Performance Dataset")
print("-"*60)
print(df)

# Basic Information

print("\nDataset Information")
print(df.info())

print("\nStatistical Summary")
print(df.describe())

# Handle Missing Values

df.fillna(0, inplace=True)

# Average Scores

print("\nAverage Assignment Score: ", round(df["Assignment Score"].mean(),2))
print("Average Midterm Score: "), round(df["Midterm Score"].mean(),2)
print("Average Final Score: "), round(df["Final Score"].mean(),2)

# Highest and Lowest Final Score

highest = df.loc[df["Final Score"].idxmax()]
lowest = df.loc[df["Final Score"].idxmin()]
print("\nHighest Scoring Student")
print(highest)
print("\nLowest Scoring Student")
print(lowest)

# Attendance Below 75%

print("\nStudents with Attendance Below 75%")
low_attendance = df[df["Attendance"] < 75]
print(low_attendance)

# Student at Risk

print("\nStudents At Risk (Final Score < 60)")
at_risk = df[df["Final Score"] < 60]
print(at_risk)

# Average Score by course

course_average = df.groupby("Course")["Final Score"].mean()
print("\nAverage Final Score by Course")
print(course_average)

# Relation between attendance and final score

correlation = df["Attendance"].corr(df["Final Score"])
print("\nCorrelation between Attendance and Final Score:")
print(round(correlation,2))

# -----------------------
# Visualization
# -----------------------

# Score Distribution

plt.figure(figsize=(6,4))
plt.hist(df["Final Score"], bins=8)
plt.title("Final Score Distribution")
plt.xlabel("Final Score")
plt.ylabel("Number of Students")
plt.savefig("charts/score_distribution.png")
plt.show()

# Average Score By Course

plt.figure(figsize=(7,4))
course_average.plot(kind="bar")
plt.title("Average Final Score By Course")
plt.ylabel("Average Score")
plt.tight_layout()
plt.savefig("charts/average_score_by_course.png")
plt.show()

# Attendance VS Final Score

plt.figure(figsize=(6,4))
plt.scatter(df["Attendance"], df["Final Score"])
plt.title("Attendance VS Final Score")
plt.xlabel("Attendance")
plt.ylabel("Final Score")
plt.savefig("charts/attendance_vs_final_score.png")
plt.show()
