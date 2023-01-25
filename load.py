from Person import Person
from Student import Student
import csv
import json


def place_student_object_in_group(students, school):
    while students:
        for group in school.groups:
            length = 5 - len(group.students)
            for i in range(length):
                try:
                    group.add_student(students.pop())
                except:
                    break
        if len(students) > 0:
            print("Zabrakło miejsca w grupach!!! Nie wszyscy studenci zostali dodani, dodaj kolejne grupy")
        break


def load_new_students(school, file_type: str):
    if file_type in ("csv", "json"):
        students = []
        with open(f'students.{file_type}', mode='r') as _data:
            new_students = json.load(_data) if file_type == 'json' else csv.reader(_data, delimiter=';')
            for student in new_students:
                student = student if file_type == 'json' else dict(zip(["name", "surname", "gender"], student))
                p = Person(**student)
                s = Student(p)
                students.append(s)
        students_num = len(students)
        place_student_object_in_group(students, school)
        print(f"Załadowano {students_num} nowych studentów")
    else:
        print("Nieobsługiwany format pliku")


def load_new_school(file_type: str):
    schools = []
    with open(f'school.{file_type}', newline='') as _data:
        new_schools = json.load(_data) if file_type == 'json' else csv.reader(_data, delimiter=';')
        for school in new_schools:
            schools.append(school[0])
    print("Załadowano listę nowych szkół")
    return schools
