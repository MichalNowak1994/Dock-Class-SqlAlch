class PersonInGroup:

    def __init__(self, group_id: int, student_obj: object):
    
        self.group_id = group_id
        self.student_obj = student_obj
        self.index_number = student_obj.index_number
        self.grade = 0

