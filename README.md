# Student Performance Analytics System

## 1. Project overview
This beginner-level Python project analyses student marks, attendance and assignment scores. It uses **Python, NumPy and Pandas** to calculate performance, classify students, compare departments and export reports.

**Important:** `student_data.csv` contains fictional sample records made for demonstration. Replace them with authorised data if your instructor requires real data.

## 2. Features
- Reads student records from a CSV spreadsheet.
- Calculates average marks and a weighted overall percentage.
- Assigns categories: Excellent, Good, Needs Improvement or At Risk.
- Marks students as Pass/Fail based on average subject marks (40 or more = Pass).
- Shows class statistics, department-wise averages and top five students.
- Exports detailed and summary CSV reports.

## 3. Technology and concepts
- Python: variables, data types, functions, conditions, loops/iteration, file handling.
- NumPy: numeric arrays, mean calculations and `where`.
- Pandas: CSV loading, DataFrames, cleaning, filtering, grouping and exporting.

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
