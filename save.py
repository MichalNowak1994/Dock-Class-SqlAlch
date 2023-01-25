import csv
from string import ascii_lowercase
from random import choice, randint
import json

json_school_list = []
random_list = []
__RANDOM_GENDER = ['male', 'female']


def get_random_string():
    letters = ascii_lowercase
    result_str = ''.join(choice(letters) for _ in range(randint(3, 10)))
    return result_str.capitalize()


def save_new_random_students_csv(how_many_students):
    with open('students.csv', 'w', newline='') as csvfile:
        new_student = csv.writer(csvfile, delimiter=';')
        for _ in range(how_many_students):
            new_student.writerow([get_random_string(), get_random_string(), __RANDOM_GENDER[randint(0, 1)]])


def save_new_school_from_csv(how_many):
    with open('school.csv', 'w', newline='') as csvfile:
        new_student = csv.writer(csvfile, delimiter=';')
        for _ in range(how_many):
            new_student.writerow([get_random_string().upper()])


def save_new_random_students_json(how_many):
    for i in range(how_many):
        random_dict = {"name": get_random_string(),
                       "surname": get_random_string(),
                       "gender": __RANDOM_GENDER[randint(0, 1)]}
        random_list.append(random_dict)
    json_object = json.dumps(random_list, indent=4)
    with open('students.json', 'w') as outfile:
        outfile.write(json_object)


def save_new_random_schools_json(how_many):
    for i in range(how_many):
        json_school = [get_random_string().upper()]
        json_school_list.append(json_school)
    new_json_object = json.dumps(json_school_list, indent=4)
    with open('school.json', 'w') as outfile:
        outfile.write(new_json_object)
