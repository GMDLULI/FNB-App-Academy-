def student_input():
    learner_name = input("Please enter your name: ")
    english_mark = float(input("Enter your English mark: "))
    math_mark = float(input("Enter your Math mark: "))
    science_mark = float(input("Enter your Computer Science mark: "))
    show_report = input("Would you like to see your report? (yes/no): ").strip().lower()

    return  {'name': learner_name,
            "english": english_mark, 
            'math': math_mark,
            'science': science_mark,
            'show': show_report}

def teacher_input():
    search_learner = input("Enter name of student to search for: ").strip().lower()
    return search_learner


def calculate_grade(mark):
    if mark >= 80:
        return "A"
    elif 79 >= mark >= 70:
        return  "B"
    elif 69 >= mark >= 60:
        return  "C"
    elif 59 >= mark >= 50:
        return "D" 
    else:
        return "F"
    
def calculate_average(student):
    """Calculate the student's average mark."""
    return (
        student["english"]
        + student["math"]
        + student["science"]
    ) / 3

def show_results(student):
    print("\n----- REPORT -----")
    print(f"Student: {student['name']}")

    for subject in ("english", "math", "science"):
        mark = student[subject]
        grade = calculate_grade(mark)

        print(f"{subject.title():<10}: {mark:.1f} - Grade {grade}")

        if grade == "F":
            print(
                f"Please pay attention to your {subject.title()} class."
            )
    average = calculate_average(student)
    print(f"\nAverage: {average:.2f}")
    print("------------------\n")
    


students_marks= []


while True:
    role = input(
        "\nWho are you?\n"
        "A. Student\n"
        "B. Teacher\n"
        "Q. Quit\n"
        "Choice: "
    ).strip().lower()

    if role == 'a':
        student = student_input()
        students_marks.append(student)
        print('Student Added successfully!')

        if student['show'] == 'yes':
            show_results(student)
                        
           
    elif role == 'b':
        if not students_marks:
            print('No Students have been added yet.')
            continue

        search_name = teacher_input()
        found = False
        for student in students_marks:
            if student["name"].lower() == search_name:
                show_results(student)
                found = True
                break

        if not found:
            print("Student not found.")

    elif role == "q":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter A, B, or Q.")

       


