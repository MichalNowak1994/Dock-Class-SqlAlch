from Person import Person
from log.logs import logger
# from Student import Student
# from Group import Group
# from School import School
# import interface
# import save
from src.basic import run_db_select_statement, create_table, show_all_tables, drop_item_table, retrieve_all_item


p1 = Person("Aleksandra", "Grzesiak", "femaasdasdasle")
p2 = Person("Maciek", "Aleksandryjski", "male")
p3 = Person("Grzesiek", "Maciecki", "male")
p4 = Person("Tomasz", "Problem", "male")
p5 = Person("Adam", "Ignacki", "male")
p6 = Person("Agnieszka", "Jakastam", "female")
p7 = Person("Agnieszka", "Włodarczyk", "female")

Person.insert_person("Aleksander", "Grzesiacki", "male")


try:
    """Main program"""
    logger.info("Program Started")
    # Person.show_all_persons()
    retrieve_all_item()
    # logger.info("Printed in console a list of all persons")
    Person.find_single_person("Name", "AgnieszKa")
    logger.info("Printed in console result of find_single_person method")
    logger.info("Script ended")
except Exception as e:
    """Excepts"""
    logger.error("An error occurred:", exc_info=e)



















# s1 = Student(all_persons[0])
# s2 = Student(p2)
# s3 = Student(p3)
# s4 = Student(p4)
# s5 = Student(p5)
# s6 = Student(p6)
#
# school_1 = School("SCHOOLABC")
#
# group_1 = Group(school_1, "maths group")
# group_2 = Group(school_1, "maths group")
# group_3 = Group(school_1, "maths group")
# group_4 = Group(school_1, "history group")
# group_5 = Group(school_1, "maths group")
# group_6 = Group(school_1, "history group")
#
# save.save_new_random_students_csv(3)
# save.save_new_random_schools_json(3)
# save.save_new_random_students_json(3)
# save.save_new_school_from_csv(3)
#
# interface.generate_groups(4, 3, school_1)
#
# group_1.add_student(s1)
# group_1.add_student(s2)
# group_1.add_student(s3)
# group_2.add_student(s4)
# group_3.add_student(s5)
# group_4.add_student(s6)
#
# school_1.add_group(group_1)
# school_1.add_group(group_2)
# school_1.add_group(group_4)
#
# group_1.add_grade(s2, 5)
# group_1.add_grade(s3, 2.5)
# group_2.add_grade(s4, 3.5)
# group_3.add_grade(s5, 2)
#

# create_table()
# show_all_tables()
# drop_item_table())part_of_method(
# Person.insert_person("Aleksander", "Włodarczyk", "male")

# retrieve_all_item()

# while interface.app_up:
#     chosen_school = interface.choose_school(School.objects)        print(values)

#     os.system('clear')
#     tmp_1 = input(interface.prompt)
#     os.system('clear')
#     interface.menu(tmp_1, chosen_school)
#     tmp_2 = input("\nWciśnij enter, by kontynuować")
#     os.system('clear')
