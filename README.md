# Student Performance Analytics System

## 1. Project Title
* Project Name: Student Performance Analytics System
* Developer: Sareen Khan

## 2. Objective
The primary objective of this project is to automate the analysis of student academic performance. It was created to solve the challenge of manual grade calculation and reporting by processing student marks, attendance, and assignment records to generate accurate performance metrics, class summaries, and individual student reports efficiently.

## 3. Technologies Used
* **Programming Language:** Python
* **Data Processing Libraries:** Pandas, NumPy
* **Development Environment:** Visual Studio Code (VS Code)

## 4. Dataset Description
| Column | Meaning |
|---|---|
| student_id | Unique student code |
| student_name | Fictional student name |
| department | CSE, IT or ECE |
| maths / programming / database | Subject marks out of 100 |
| attendance_percent | Attendance from 0 to 100 |
| assignment_percent | Assignment score from 0 to 100 |

## 5. Implementation
The application is implemented in Python using a structured, modular approach:
1. Data Loading: Reads raw student data from an Excel file using Pandas (`pd.read_excel`).
2. Calculation: 
     * Average marks = (Maths + Programming + Database) / 3.
     * Overall percentage = (Average marks × 0.70) + (Attendance × 0.15) + (Assignment score × 0.15).
     * Category: 85+ Excellent; 70–84.99 Good; 50–69.99 Needs Improvement; below 50 At Risk.
     * Pass/Fail is based on average subject marks: 40 or more = Pass.
3. Interactive Interface: Built using user input controls and string methods 
     * Option 1: 
  * *Option 2 (Student Search):* Performs case-insensitive record lookups using row traversal (`df.loc`) to output complete individual student transcripts.
* **Automated Excel Export:** Automatically serializes and saves the fully processed dataset containing all calculated metrics into a clean output file (`student_performance_report.xlsx`) via `df.to_excel()`
---

## 6. Key Features
* **Class Performance Summary:** Displays total student count, class average, highest/lowest percentages, and a sorted leaderboard of the top 5 students.
* **Individual Student Search:** Allows users to search for specific students by name to view their complete subject-wise marks, attendance, average, category, and final result.
* **Automated Excel Reporting:** Generates clean, updated output spreadsheets (`student_performance_report.xlsx`) containing all computed analytics.

---

## 7. Output / Screenshots
*(Aap yahan apne terminal ke outputs ya generated Excel files ki screenshot images add kar sakte hain)*
* **Terminal Menu & Summary Output**
* **Individual Student Search Result**

---

## 8. Final Outcome
The project successfully achieves its goal of automating student data analytics. It provides educators and administrators with a fast, reliable tool to gauge overall class performance, identify at-risk students, and export clean institutional reports without manual calculation errors.

---

## 9. Challenges & Learning
* **Challenges Faced:** Encountered Git configuration and authentication hurdles (`GitCredentialManager`) while pushing the repository, alongside structuring conditional data loops in Pandas.
* **Solutions & Learnings:** Resolved credential and identity setups via Git config commands, and gained deep practical experience in data manipulation, vector operations with NumPy, and file handling using Pandas.

---

## 10. GitHub Repository
* **Repository Link:** [https://github.com/Sareen-khan/Student_Performance_Analytics_System](https://github.com/Sareen-khan/Student_Performance_Analytics_System)

## 1. Project overview
This beginner-level Python project analyses student marks, attendance and assignment scores. It uses **Python, NumPy and Pandas** to calculate performance, classify students, compare departments and export reports.

**Important:** `student_data.csv` contains fictional sample records made for demonstration. Replace them with authorised data if your instructor requires real data.

## 2. Features
- Reads student records from a Excel spreadsheet.
- Calculates average marks and a weighted overall percentage.
- Assigns categories: Excellent, Good, Needs Improvement or At Risk.
- Marks students as Pass/Fail based on average subject marks (40 or more = Pass).
- Shows class statistics, department-wise averages and top five students.
- Exports detailed and summary Excel reports.

## 3. Technology and concepts
- Python: variables, data types, functions, conditions, loops/iteration, file handling.
- NumPy: numeric arrays, mean calculations and `where`.
- Pandas: Excel loading, DataFrames, cleaning, filtering, grouping and exporting.

## 4. Dataset columns
| Column | Meaning |
|---|---|
| student_id | Unique student code |
| student_name | Fictional student name |
| department | CSE, IT or ECE |
| maths / programming / database | Subject marks out of 100 |
| attendance_percent | Attendance from 0 to 100 |
| assignment_percent | Assignment score from 0 to 100 |

## 5. Calculation method
1. Average marks = (Maths + Programming + Database) / 3.
2. Overall percentage = (Average marks × 0.70) + (Attendance × 0.15) + (Assignment score × 0.15).
3. Category: 85+ Excellent; 70–84.99 Good; 50–69.99 Needs Improvement; below 50 At Risk.
4. Pass/Fail is based on average subject marks: 40 or more = Pass.

These are project-defined rules for demonstration, not an official college grading policy.

## 6. Setup and execution (Windows)
1. Install Python 3.10 or newer from https://www.python.org/downloads/ . During installation, tick **Add Python to PATH**.
2. Extract the project ZIP.
3. Open the extracted folder in VS Code.
4. Open **Terminal → New Terminal**.
5. Run:
   ```bash
   py -m pip install -r requirements.txt
   ```
6. Run:
   ```bash
   py main.py
   ```
7. Review the terminal summary and the generated `output` folder.

If `py` does not work, try `python` instead.

## 7. Project folder structure
```text
Student_Performance_Analytics_System/
├── main.py
├── student_data.csv
├── requirements.txt
├── README.md
├── PROJECT_REPORT.md
├── SUBMISSION_CHECKLIST.md
└── output/                       # created when you run main.py
    ├── student_performance_report.csv
    ├── department_summary.csv
    └── students_needing_support.csv
```

## 8. How to create your own spreadsheet
Open `student_data.csv` in Excel or Google Sheets. The first row is the header. Add one student per row and keep the column names exactly the same. Save/download as **CSV UTF-8** and keep the file beside `main.py`. Use marks and percentages between 0 and 100.

## 9. Limitations and future improvements
- The included records are sample data.
- The project currently uses a simple weighted formula and fixed thresholds.
- Future upgrades could include charts, a login screen, a graphical interface, and more subjects.
