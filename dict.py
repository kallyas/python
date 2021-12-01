# Dictionary Assignment
# Author: Iden 
# create a dictionary called ReportCard. the keys will be the students and the values will be their graes
# in your report card dictionary, change one of the students grades
# create a while loop that prints 10 numbers but it skips the number 3
# create a list that prints out all the items outside of the list
#  create an if statement that use the input method.
ReportCard = {}
def create_ReportCard():
    # ReportCard = {}
    students_number = int(input("How many students are in your class? "))

    for i in range(students_number):
        student_name = input("What is the student's name? ")
        student_grade = input(f"What is {student_name}'s grade? ")
        ReportCard[student_name] = student_grade

    return ReportCard
print("************Report Card****************\n")
print(create_ReportCard())

def change_grade():
    student_name = input("Which student's name would you like to change their grade?: ")

    if student_name in ReportCard:
        student_grade = input(f"What is {student_name}'s new grade? ")
        ReportCard[student_name] = student_grade
    else:
        return "That student is not in your class."

    return ReportCard

print("************Change Grade****************\n")
print(change_grade())

def skip_number():
    i = 0
    while i < 10:
        i += 1
        if i == 3:
            continue
        print(i)

print("************Skip Number****************\n")
skip_number()

def outside_list():
    outside_list = ["a", "b", "c", "d", "e"]
    for i in outside_list:
        print(i)

print("************Outside List****************\n")
outside_list()


def if_statement():
    if input("Would you like to change a student's grade? (y/n): ") == "y":
        change_grade()
    else:
        return "Thank you for using the program."

print("************If Statement****************\n")
print(if_statement())
