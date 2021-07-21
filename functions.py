students = []

def get_students_titlecase():
    students_titlecase =[]
    for student in students:
        students_titlecase = student.title()
    return students_titlecase

def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(Students_titlecase)

def add_student(name,student_id=332):
    student = {"name":name,"student_id":student_id}
    students.append(name)


student_list = get_students_titlecase()

add_student("Mark",student_id=15)
