import pandas as pd
import numpy as np


DATA_FILE = "students.csv"


def assign_grade(average):
    """Return a letter grade based on the student's average marks."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    return "F"


def analyze_students(data):
    """Calculate totals, averages, grades, and pass/fail status."""
    subject_columns = ["Maths", "Science", "English", "Computer"]

    data = data.copy()
    data["Total"] = data[subject_columns].sum(axis=1)
    data["Average"] = data[subject_columns].mean(axis=1)
    data["Grade"] = data["Average"].apply(assign_grade)
    data["Result"] = np.where((data[subject_columns] >= 35).all(axis=1), "Pass", "Fail")
    return data


def main():
    try:
        students = pd.read_csv(DATA_FILE)
    except FileNotFoundError:
        print(f"Error: '{DATA_FILE}' was not found. Keep it in the same folder as main.py.")
        return

    required_columns = [
        "Student_ID", "Name", "Department", "Maths", "Science",
        "English", "Computer", "Attendance"
    ]
    missing = [column for column in required_columns if column not in students.columns]
    if missing:
        print("Error: Missing required columns:", ", ".join(missing))
        return

    subject_columns = ["Maths", "Science", "English", "Computer"]
    students[subject_columns + ["Attendance"]] = students[subject_columns + ["Attendance"]].apply(
        pd.to_numeric, errors="coerce"
    )
    students = students.dropna(subset=subject_columns + ["Attendance"])

    if students.empty:
        print("No valid student records were found.")
        return

    results = analyze_students(students)
    print("\nSTUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 42)
    print(f"Number of students analyzed: {len(results)}")
    print(f"Overall class average: {results['Average'].mean():.2f}")
    print(f"Students passed: {(results['Result'] == 'Pass').sum()}")
    print(f"Students failed: {(results['Result'] == 'Fail').sum()}")
    print(f"Average attendance: {results['Attendance'].mean():.2f}%")

    print("\nSTUDENT-WISE SUMMARY")
    print(results[["Student_ID", "Name", "Department", "Total", "Average", "Grade", "Result"]]
          .to_string(index=False, formatters={"Average": "{:.2f}".format}))

    print("\nSUBJECT-WISE AVERAGES")
    print(results[subject_columns].mean().round(2).to_string())

    top_student = results.loc[results["Average"].idxmax()]
    lowest_student = results.loc[results["Average"].idxmin()]
    print("\nTOP PERFORMER")
    print(f"{top_student['Name']} — average: {top_student['Average']:.2f}")
    print("\nLOWEST AVERAGE")
    print(f"{lowest_student['Name']} — average: {lowest_student['Average']:.2f}")


if __name__ == "__main__":
    main()
