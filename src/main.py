import csv
from pathlib import Path


def load_students(file_path):
    students = []

    with open(file_path, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            student = {
                "name": row["Name"],
                "score": float(row["Score"]),
                "attendance": float(row["Attendance"])
            }

            students.append(student)

    return students


def analyze_students(students):
    total_score = 0
    pass_count = 0
    fail_count = 0

    highest_score = students[0]["score"]
    lowest_score = students[0]["score"]

    top_student = students[0]["name"]
    lowest_student = students[0]["name"]

    for student in students:
        score = student["score"]
        total_score += score

        if score >= 50:
            pass_count += 1
            student["result"] = "Pass"
        else:
            fail_count += 1
            student["result"] = "Fail"

        if score > highest_score:
            highest_score = score
            top_student = student["name"]

        if score < lowest_score:
            lowest_score = score
            lowest_student = student["name"]

    average_score = total_score / len(students)

    analysis = {
        "average_score": average_score,
        "pass_count": pass_count,
        "fail_count": fail_count,
        "highest_score": highest_score,
        "lowest_score": lowest_score,
        "top_student": top_student,
        "lowest_student": lowest_student
    }

    return analysis


def display_report(students, analysis):
    print("CSV Student Score Analyzer")
    print("--------------------------")

    for student in students:
        print(
            f"Name: {student['name']}, "
            f"Score: {student['score']}, "
            f"Attendance: {student['attendance']}%, "
            f"Result: {student['result']}"
        )

    print()
    print("Summary")
    print("-------")
    print(f"Number of students: {len(students)}")
    print(f"Average score: {analysis['average_score']:.2f}")
    print(f"Students passed: {analysis['pass_count']}")
    print(f"Students failed: {analysis['fail_count']}")
    print(f"Top student: {analysis['top_student']} ({analysis['highest_score']:.2f})")
    print(f"Lowest student: {analysis['lowest_student']} ({analysis['lowest_score']:.2f})")


def save_report(students, analysis, output_path):
    with open(output_path, "w") as file:
        file.write("CSV Student Score Analyzer\n")
        file.write("--------------------------\n\n")

        file.write("Student Records\n")
        file.write("---------------\n")

        for student in students:
            file.write(
                f"Name: {student['name']}, "
                f"Score: {student['score']}, "
                f"Attendance: {student['attendance']}%, "
                f"Result: {student['result']}\n"
            )

        file.write("\nSummary\n")
        file.write("-------\n")
        file.write(f"Number of students: {len(students)}\n")
        file.write(f"Average score: {analysis['average_score']:.2f}\n")
        file.write(f"Students passed: {analysis['pass_count']}\n")
        file.write(f"Students failed: {analysis['fail_count']}\n")
        file.write(
            f"Top student: {analysis['top_student']} "
            f"({analysis['highest_score']:.2f})\n"
        )
        file.write(
            f"Lowest student: {analysis['lowest_student']} "
            f"({analysis['lowest_score']:.2f})\n"
        )


data_file = Path("data") / "students.csv"
output_file = Path("outputs") / "report.txt"

try:
    students = load_students(data_file)

    if len(students) == 0:
        print("No student records found.")
    else:
        analysis = analyze_students(students)
        display_report(students, analysis)
        save_report(students, analysis, output_file)

        print()
        print(f"Report saved to: {output_file}")

except FileNotFoundError:
    print("Error: students.csv was not found in the data folder.")
except KeyError:
    print("Error: The CSV file does not contain the required columns.")
except ValueError:
    print("Error: Score or attendance contains invalid numeric data.")




