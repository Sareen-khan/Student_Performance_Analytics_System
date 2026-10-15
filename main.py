
import numpy as np
import pandas as pd

# Load Excel file
df = pd.read_excel("Student_Performance_Data_Sheet.xlsx")

# Calculate average marks
df["average_marks"] = (
    df["maths"] + df["programming"] + df["database"]
) / 3

# Calculate overall percentage
df["overall_percentage"] = (
    df["average_marks"] * 0.70
    + df["attendance_percent"] * 0.15
    + df["assignment_percent"] * 0.15
)

# Find performance category
category = []

for score in df["overall_percentage"]:
    if score >= 85:
        category.append("Excellent")
    elif score >= 70:
        category.append("Good")
    elif score >= 50:
        category.append("Needs Improvement")
    else:
        category.append("At Risk")

df["performance_category"] = category

# Find pass or fail
result = []

for marks in df["average_marks"]:
    if marks >= 40:
        result.append("Pass")
    else:
        result.append("Fail")

df["result"] = np.array(result)

# Display menu
print("STUDENT PERFORMANCE SYSTEM")
print("1. Class Performance Summary")
print("2. Search Student Report")

choice = input("Enter your choice: ")

if choice == "1":

    print("\nTotal Students:", len(df))
    print("Class Average:", round(df["overall_percentage"].mean(), 2))
    print("Highest Percentage:", round(df["overall_percentage"].max(), 2))
    print("Lowest Percentage:", round(df["overall_percentage"].min(), 2))

    print("\nTop 5 Students:")
    top_students = df.sort_values(
        by="overall_percentage", ascending=False
    ).head(5)

    print(top_students[
        ["student_id", "student_name", "overall_percentage",
         "performance_category"]
    ].to_string(index=False))

elif choice == "2":

    name = input("Enter student name: ").strip().lower()

    found = False

    for i in range(len(df)):
        if str(df.loc[i, "student_name"]).lower() == name:

            found = True

            print("\\nStudent Name:", df.loc[i, "student_name"])
            print("Student ID:", df.loc[i, "student_id"])
            print("Department:", df.loc[i, "department"])
            print("Maths Marks:", df.loc[i, "maths"])
            print("Programming Marks:", df.loc[i, "programming"])
            print("Database Marks:", df.loc[i, "database"])
            print("Attendance:", df.loc[i, "attendance_percent"])
            print("Assignment:", df.loc[i, "assignment_percent"])
            print("Average Marks:", round(df.loc[i, "average_marks"], 2))
            print("Overall Percentage:", round(df.loc[i, "overall_percentage"], 2))
            print("Category:", df.loc[i, "performance_category"])
            print("Result:", df.loc[i, "result"])

    if found == False:
        print("Student not found!")

else:
    print("Invalid choice!")
