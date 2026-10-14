# Student Performance Analytics System

## Project Title
**Student Performance Analytics System**

## Student Details
- **Student Name:** Ediga Dharani
- **Branch:** CSE (AI & ML)
- **Course:** Python with AI — EWB Courses

## 1. Objective
To build a Python-based Student Performance Analytics System that reads student data, processes marks and attendance, and presents useful academic summaries such as averages, grades, pass/fail statistics, subject-wise performance, and top performers.

## 2. Technologies Used
- Python
- NumPy
- Pandas
- CSV dataset

## 3. Dataset Description
The dataset is stored in `students.csv` and contains 20 sample student records. The columns are Student ID, Name, Department, Maths, Science, English, Computer, and Attendance.

## 4. Implementation
1. Load the CSV dataset using Pandas.
2. Check that the required columns are available and convert marks and attendance values to numeric data.
3. Calculate each student's total and average marks.
4. Assign grades based on average marks.
5. Determine pass/fail status: a student passes when every subject mark is at least 35.
6. Calculate class average, average attendance, and subject-wise averages.
7. Identify the top performer and the student with the lowest average.
8. Display the analysis clearly in the terminal.

## 5. Key Features
- Student-wise total and average marks.
- Grade assignment using a defined grading scale.
- Pass/fail classification based on subject marks.
- Overall class average and average attendance.
- Subject-wise average performance.
- Identification of top and lowest average performers.

## 6. Final Outcome
The program summarizes the student dataset and makes it easier to review individual and class performance. It demonstrates Python fundamentals, functions, conditions, NumPy calculations, Pandas data handling, and CSV processing.

## 7. Challenges & Learning
- Practiced loading and organizing CSV data with Pandas.
- Learned to validate columns and process numeric values.
- Applied functions and conditions for grades and pass/fail results.
- Used data aggregation to calculate averages and compare performance.
- Practiced organizing files and documenting a project for GitHub.

## 8. GitHub Repository
https://github.com/Dharani-diploma/Student-Performance-Analytics-System

## Project Files
- `main.py` — main program.
- `students.csv` — sample student dataset.
- `requirements.txt` — required Python packages.
- `Project_Documentation.pdf` — separate documentation prepared using the EWB assessment sections.

## How to Run
1. Install Python 3.9 or later.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the program:

   ```bash
   python main.py
   ```

Keep `main.py` and `students.csv` in the same folder.
