
# grade_manager.py
# Student Marks and Grade Management System

# Dictionary to store student names, marks, and grades
students = {}


# Function to calculate grade
def calculate_grade(mark):
    if 90 <= mark <= 100:
        return "A"
    elif 80 <= mark < 90:
        return "B"
    elif 70 <= mark < 80:
        return "C"
    elif 60 <= mark < 70:
        return "D"
    else:
        return "E"


# Function to add a student
def add_student():
    try:
        name = input("Enter student name: ").strip()

        if not name:
            print("Error: Student name cannot be empty.")
            return

        mark = float(input("Enter student mark (0-100): "))

        if not 0 <= mark <= 100:
            print("Error: Mark must be between 0 and 100.")
            return

        if name in students:
            print("Error: Student already exists.")
            return

        grade = calculate_grade(mark)

        students[name] = {
            "mark": mark,
            "grade": grade
        }

        print(f"Student {name} added successfully!")
        print(f"Grade: {grade}")

    except Exception as e:
        print("An error occurred:", e)


# Function to display students and statistics
def show_students():
    try:
        if not students:
            print("\nNo student records available.")
            return

        print("\n" + "=" * 45)
        print("          STUDENT MARKS REPORT")
        print("=" * 45)

        print(f"{'Name':<20}{'Mark':>10}{'Grade':>10}")
        print("-" * 45)

        for name, details in students.items():
            print(
                f"{name:<20}"
                f"{details['mark']:>10.2f}"
                f"{details['grade']:>10}"
            )

        print("-" * 45)

        marks = [details["mark"] for details in students.values()]

        average = sum(marks) / len(marks)
        highest = max(marks)
        lowest = min(marks)

        print(f"\nTotal students : {len(students)}")
        print(f"Class average  : {average:.2f}")
        print(f"Highest mark   : {highest:.2f}")
        print(f"Lowest mark    : {lowest:.2f}")

        print("=" * 45)

    except Exception as e:
        print("An error occurred:", e)


# Main menu function
def main():
    while True:
        try:
            print("\n===== STUDENT GRADE MANAGER =====")
            print("1. Add Student")
            print("2. Show Students")
            print("3. Quit")

            choice = input("Enter your choice (1-3): ").strip()

            if choice == "1":
                add_student()

            elif choice == "2":
                show_students()

            elif choice == "3":
                print("Thank you for using Grade Manager!")
                break

            else:
                print("Invalid choice! Please enter 1, 2, or 3.")

        except Exception as e:
            print("An unexpected error occurred:", e)


# Run the program
if __name__ == "__main__":
    main()
