students = {
    "Bob": {
        "marks": {
            "Maths": 80,
            "Science": 90,
            "English": 70
        }
    }
}

# ask a user to add a new student with name and marks
new_student = input("Enter a new student name: ")
new_student_marks_Maths = input("Enter the maths marks of the new student: ")
new_student_marks_Science = input("Enter the science marks of the new student: ")
new_student_marks_English = input("Enter the english marks of the new student: ")

students[new_student] = {
    "marks": {
        "Maths": new_student_marks_Maths,
        "Science": new_student_marks_Science,
        "English": new_student_marks_English
    }
}

print(students)


