import os
import load
from save import get_random_string
from School import School
from Group import Group

app_up = True
school_list = []


def generate_groups(names_num, repetition_num, school):
    tmp_groups = []
    for _ in range(names_num):
        rand_str = get_random_string()
        for _ in range(repetition_num):
            group = Group(school, rand_str)
            tmp_groups.append(group)
            school.add_group(group)


def quit_app():
    global app_up
    print("Kończymy")
    app_up = False


def choose_school(set_of_schools):
    list_of_schools = list(set_of_schools)
    for i in range(len(list_of_schools)):
        print(f"Aby wybrać: {list_of_schools[i].school_name}, wpisz: {i}\n")
    return list_of_schools[int(input())]


def choose_group(chosen_school):
    try:
        os.system('clear')
        print("Aby wybrać grupę: ".ljust(25), "Wybierz:")
        for group in chosen_school.groups:
            print(
                f"{group.show_full_name()}".ljust(25),  f"{chosen_school.groups.index(group)}")
        return int(input())
    except IndexError:
        print('Błędna cyfra spróbuj wybrać inną')
    except TypeError:
        print('Miałeś podać cyfrę, a nie jakieś słowa')


def list_of_every_student_in_group(chosen_school):
    try:
        os.system('clear')
        group_index = choose_group(chosen_school)
        os.system('clear')
        chosen_school.groups[group_index].get_students_index()
    except IndexError:
        print('Błędna cyfra spróbuj wybrać inną')
    except TypeError:
        print('Miałeś podać cyfrę, a nie jakieś słowa')


def list_of_every_student_in_school(chosen_school):
    try:
        os.system('clear')
        print('Wygenerowano raport: lista wszystkich studentów (nr albumu) dla szkoły\n')
        print("Imię:".ljust(19), "Nazwisko:".ljust(19), "Numer indeksu:", "\n")
        for group in range(len(chosen_school.groups)):
            chosen_school.groups[group].get_every_student()
    except IndexError:
        print('Błędna cyfra spróbuj wybrać inną')
    except TypeError:
        print('Miałeś podać cyfrę, a nie jakieś słowa')


def students_in_group_with_grades(chosen_school):
    try:
        os.system('clear')
        group_index = choose_group(chosen_school)
        os.system('clear')
        print('Wygenerowano raport: lista studentów, którzy mają ocenę w wybranej grupie\n')
#         print("Imię:".ljust(19), "Nazwisko:".ljust(19), "Numer indeksu:".ljust(19))
        chosen_school.groups[group_index].get_students_with_grades()
    except IndexError:
        print('Błędna cyfra spróbuj wybrać inną')
    except TypeError:
        print('Miałeś podać cyfrę, a nie jakieś słowa')


def students_in_group_without_grades(chosen_school):
    try:
        os.system('clear')
        group_index = choose_group(chosen_school)
        os.system('clear')
        print('Wygenerowano raport: lista studentów, którzy nie mają oceny w wybranej grupie\n')
        print("Imię:".ljust(19), "Nazwisko:".ljust(19), "Numer indeksu:".ljust(19), "Grupa:\n")
        result = chosen_school.groups[group_index].get_students_without_grades()
        if result != ("", ""):
            text_1, text_2 = result
            print(text_1, text_2) 
    except IndexError:
        print('Błędna cyfra spróbuj wybrać inną')
    except TypeError:
        print('Miałeś podać cyfrę, a nie jakieś słowa')


def number_of_students(chosen_school):
    try:
        os.system('clear')
        print('Wygenerowano raport: liczba studentów łącznie\n')
        chosen_school.get_number_of_students()
    except IndexError:
        print('Błędna cyfra spróbuj wybrać inną')
    except TypeError:
        print('Miałeś podać cyfrę, a nie jakieś słowa')


def students_without_grades_in_school(chosen_school):
    try:
        os.system('clear')
        print('Wygenerowano raport: lista osób dla szkoły, bez ocen (bez podziału na grupy)\n')
        print("Imię:".ljust(19), "Nazwisko:".ljust(19), "Numer indeksu:".ljust(19), "Grupa:\n")
        chosen_school.get_students_in_school_without_grades()
    except IndexError:
        print('Błędna cyfra spróbuj wybrać inną')
    except TypeError:
        print('Miałeś podać cyfrę, a nie jakieś słowa')


def groups_in_school_with_details(chosen_school):
    try:
        os.system('clear')
        print('Wygenerowano raport: lista grup zajęciowych z liczbą studentów\n')
        print("Id grupy:".ljust(9), "Nazwa grupy:".ljust(19), "Liczba studentów:\n")
        chosen_school.get_groups_details()
    except IndexError:
        print('Błędna cyfra spróbuj wybrać inną')
        choose_group(chosen_school)
    except TypeError:
        print('Miałeś podać cyfrę, a nie jakieś słowa')


def load_new_schools():
    global school_list
    file_format = choose_format()
    new_schools = load.load_new_school(file_format)

    for school in school_list:
        if school.school_name in new_schools:
            new_schools.remove(school.school_name)
    for school in new_schools:
        tmp_school = School(school)
        school_list.append(tmp_school)
        generate_groups(2, 3, tmp_school)


def load_students_into_groups(chosen_school):
    file_format = choose_format()
    load.load_new_students(chosen_school, file_format)


def choose_format():
    os.system('clear')
    prompt = f"Wybierz: \n0 - żeby załadować plik json\n1 - żeby wybrać CSV \n"
    user_input = input(prompt)
    if user_input == '0':
        return "json"
    if user_input == '1':
        return "csv"


def menu(user_input, chosen_school):
    global school_list
    match user_input:
        case "quit":
            return quit_app()
        case "1":
            return list_of_every_student_in_group(chosen_school)
        case "2":
            return list_of_every_student_in_school(chosen_school)
        case "3":
            return students_in_group_with_grades(chosen_school)
        case "4":
            return students_in_group_without_grades(chosen_school)
        case "5":
            return students_without_grades_in_school(chosen_school)
        case "6":
            return number_of_students(chosen_school)
        case "7":
            return groups_in_school_with_details(chosen_school)
        case "8":
            return load_students_into_groups(chosen_school)
        case "9":
            return load_new_schools()
        case _:
            print('Taka komenda nie istnieje')


prompt = """Wybierz opcję:

--------------------------------------Generuj raport-------------------------------------------------
- 1 -  lista osób w grupie (nr albumu)
- 2 -  lista wszystkich studentów (nr albumu) dla szkoły
- 3 -  lista osób dla grupy z ocenami (nr albumu, ocena)
- 4 -  lista osób dla grupy bez ocen, (nr albumu)
- 5 -  lista osób dla szkoły, bez ocen (bez podziału na grupy)
- 6 -  liczba studentów łącznie
- 7 -  lista grup zajęciowych z liczbą studentów (id grupy, nazwa, liczba_studentów)

--------------------------------------Załaduj dane-------------------------------------------------
- 8 -  stwórz nowych studentów na podstawie pliku "students"
- 9 -  stwórz nowe szkoły na podstawie pliku "schools"
-----------------------------------------------------------------------------------------------------
- quit -  zakończ program
-----------------------------------------------------------------------------------------------------
"""
