class Student:
    __student_counter = 0
    __index_counter = 99

    def __init__(self, person_obj: object):
        self.student_id = self.__increment_counter()
        self.person_obj = person_obj
        self.person_id = person_obj.person_id
        self.index_number = self.__increment_index_counter()

    @classmethod
    def __increment_counter(cls):
        """Increments counter used for assigning student_id"""
        cls.__student_counter += 1
        return cls.__student_counter

    @classmethod
    def __increment_index_counter(cls):
        """Increments counter used for assigning indices"""
        cls.__index_counter += 1
        return cls.__index_counter
