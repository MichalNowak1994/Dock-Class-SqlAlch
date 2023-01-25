import weakref


class School:
    __school_counter = 0
    objects = weakref.WeakSet()

    def __init__(self, school_name: str):
        self.school_id = self.__school_increment_counter()
        self.school_name = school_name
        self.groups = []
        self.__class__.objects.add(self)

    def __repr__(self):
        return self.school_name

    @classmethod
    def __school_increment_counter(cls):
        """Increments counter used for assigning school_id"""
        cls.__school_counter += 1
        return cls.__school_counter

    def add_group(self, group_obj: object):
        """Adds groups to school list in School object"""
        self.groups.append(group_obj)

    # def get_students(self):
    #     """Prints group name and group number of each object in group list"""
    #     for group in self.groups:
    #         # print(f"\nNazwa grupy: {group.group_name}\nNumer grupy: {group.group_number}")
    #         group.show_full_name()
    #         group.get_students_index()

    def get_students_in_school_without_grades(self):
        """Prints index numbers of each School object in students list that has 0 grades"""
        for group in self.groups:
            group.get_students_without_grades()

    def get_number_of_students(self):
        """Prints number of PersonInGroup objects in all groups (duplicates excluded)"""
        __tmp_students = []
        for group in self.groups:
            for student in group.students:
                __tmp_students.append(student.student_obj)
        print(f"Liczba osób w szkole {self.school_name}: {len(set(__tmp_students))}")

    def get_groups_details(self):
        """Print group details and number of each PersonInGroup objects in each group in groups list"""
        for group in self.groups:
            __tmp_group_students = []
            for student in group.students:
                __tmp_group_students.append(student.student_obj)
            print(f"{group.group_id}".ljust(10), end="")
            print(f"{group.show_full_name()}".ljust(20), end="")
            print(f"{len(set(__tmp_group_students))}")
