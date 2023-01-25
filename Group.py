from PersonInGroup import PersonInGroup


class Group:
    __group_id_counter = 0
    __group_number = {}

    def __init__(self, school_obj: object, group_name: str):
        self.group_name = group_name
        if self.group_name not in Group.__group_number.keys():
            Group.__group_number[self.group_name] = 0
        self.group_id = self.__group_increment_counter()
        self.school_obj = school_obj
        self.school_id = school_obj.school_id
        self.group_number = self.__group_number_increment_counter(self.group_name)
        self.students = []

    # Ustalenia z godz. 13:30 - metoda add_student wyświetla alert o przekroczeniu limitu
    def add_student(self, student_obj: object):
        """Adds PersonInGroup object to students list"""
        if len(self.students) < 5:
            self.students.append(PersonInGroup(self.group_id, student_obj))
        else:
            print("Limit 5-os przekroczony. Utwórz nową grupę.")

    def add_grade(self, student_obj: object, grade: float):
        """Adds grade to grades list in PersonInGroup object"""
        if grade in [2, 2.5, 3, 3.5, 4, 4.5, 5]:
            for student in self.students:
                if student.index_number == student_obj.index_number:
                    student.grade = grade
        else:
            print("Możliwe oceny to: 2, 2.5, 3, 3.5, 4, 4.5, 5")

    def get_students_index(self):
        """Prints index numbers of each PersonInGroup object in students list"""
        print('Wygenerowano raport: lista osób w grupie (nr albumu)\n')
        print("Imię:".ljust(19), "Nazwisko:".ljust(19), "Numer indeksu:".ljust(19), "\n")

        for student in self.students:
            print(f"{student.student_obj.person_obj.name}".ljust(20), end="")
            print(f"{student.student_obj.person_obj.surname}".ljust(20), end="")
            print(f"{student.index_number}".ljust(20))

        if len(self.students) == 0:
            print("Brak studentów spełniających podane kryteria")

    def get_students_with_grades(self):
        """Prints grade s and index numbers of each PersonInGroup object in students list that has more than 0 grades"""
        __temp_list = []
        print("Imię:".ljust(19), "Nazwisko:".ljust(19), "Numer indeksu:".ljust(19), "Ocena:".ljust(9), "\n")
        for student in self.students:
            if student.grade != 0:
                print(f"{student.student_obj.person_obj.name}".ljust(20), end="")
                print(f"{student.student_obj.person_obj.surname}".ljust(20), end="")
                print(f"{student.index_number}".ljust(20), end="")
                print(f"{student.grade}".ljust(10))
            else:
                __temp_list.append('1')
        if len(__temp_list) == len(self.students):
            print("Brak studentów spełniających podane kryteria")

    def show_full_name(self):
        return f"{self.group_name} {self.group_number}"

    def get_students_without_grades(self):
        """Prints index numbers of each PersonInGroup object in students list that has 0 grades"""
        __temp_list = []
        __group_print_1 = ""
        __group_print_2 = ""
        for student in self.students:
            if student.grade == 0:
                print(f"{student.student_obj.person_obj.name}".ljust(20), end="")
                print(f"{student.student_obj.person_obj.surname}".ljust(20), end="")
                print(f"{student.index_number}".ljust(20), end="")
                print(f"{self.show_full_name()}")
            else:
                __temp_list.append('0')
            if len(__temp_list) == len(self.students):
                __group_print = "Brak studentów spełniających podane kryteria"
#                 print("Brak studentów spełniających podane kryteria")
        if len(self.students) == 0:
            __group_print_2 = "Grupa jest pusta"
#             print("Grupa jest pusta")
        return __group_print_1, __group_print_2

    def get_every_student(self):
        """Prints name and index number for every student in group"""
        for student in self.students:
            print(f"{student.student_obj.person_obj.name}".ljust(20), end="")
            print(f"{student.student_obj.person_obj.surname}".ljust(20), end="")
            print(f"{student.index_number}")

    @classmethod
    def __group_increment_counter(cls):
        """Increments counter used for assigning group_id"""
        cls.__group_id_counter += 1
        return cls.__group_id_counter

    @classmethod
    def __group_number_increment_counter(cls, group_name: str):
        """Generator increments group number counter used for assigning consecutive group numbers"""
        cls.__group_number[group_name] += 1
        return cls.__group_number[group_name]
