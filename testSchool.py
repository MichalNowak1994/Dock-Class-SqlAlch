import weakref


class School:
    __school_counter = 0
    objects = weakref.WeakSet()

    def __init__(self, school_name: str):
        self.school_name = school_name
        self.__class__.objects.add(self)

    def __repr__(self):
        return self.school_name


school_1 = School('nazwa1')
school_2 = School('nazwa2')
school_3 = School('nazwa3')
school_4 = School('nazwa4')

print([i for i in School.objects])
del school_3
print([i for i in School.objects])
print(*School.objects)
