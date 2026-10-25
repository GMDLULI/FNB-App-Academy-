learner_name = input("Please enter your name: ")
english_mark = float(input("Enter your English mark: "))
math_mark = float(input("Enter your Math mark: "))
compSci_mark = float(input("Enter your Computer Science mark: "))

learner_marks = {
    "English": english_mark,
    "Math": math_mark,
    "Computer Science": compSci_mark
}
average_mark = (english_mark + math_mark + compSci_mark) / 3
grade = ""

for subject, mark in learner_marks.items():
    if mark >= 80:
        grade = "A"
    elif 79 >= mark >= 70:
        grade = "B"
    elif 69 >= mark >= 60:
        grade = "C"
    elif 59 >= mark >= 50:
        grade = "D" 
    else:
        grade = "F"
        print(f"hello, {learner_name}! please pay attention to your {subject} class. Your grade is {grade}.")
    print(f"Hello, {learner_name}! Your grade for {subject} is {grade}.")



if average_mark <= 50:
    print(f"Your average mark is {average_mark:.2f}. You have failed the course.")
else:
    print(f"Your average mark is {average_mark:.2f}. You have passed the course.")





