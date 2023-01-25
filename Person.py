from sqlalchemy import text, Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from db.core.initializer import create_connection

"""Database engine creating"""
Base = declarative_base()
engine = create_engine(
    "postgresql://learner:StrongPassword123@localhost:5432/learnsqlalchemy"
)
Session = sessionmaker(bind=engine)
session = Session()


class Person(Base):
    """A class that contains people who can become students. Persons are saved and read from the database"""
    __tablename__ = "person"
    __counter = 0

    name = Column(String)
    surname = Column(String)
    gender = Column(String)
    person_id = Column(Integer, primary_key=True)

    def __init__(self, name: str, surname: str, gender: str) -> None:
        """Init of class person"""
        self.name = name
        self.surname = surname
        self.gender = gender if gender in ("male", "female") else "male"
        self.person_id = self.__increment_counter()
        if not Person.is_existing_person(name, surname):
            session.add(self)
            session.commit()
            session.close()

    def __repr__(self) -> str:
        """Replacing the dunder method with your own display"""
        return f"{self.name.ljust(25)}, {self.surname.ljust(25)}, {self.gender.ljust(25)}\n"

    @staticmethod
    def is_existing_person(name: str, surname: str) -> bool:
        """A method that checks whether the added people are already in the database"""
        existing_person = (
            session.query(Person).filter_by(name=name, surname=surname).first()
        )
        return existing_person is not None

    @classmethod
    def __increment_counter(cls) -> int:
        """Increments counter used for assigning person_id"""
        cls.__counter += 1
        return cls.__counter

    @classmethod
    def insert_person(cls, name: str, surname: str, gender: str) -> None:
        """A method that add new persons to database

        name (str) : argument that takes the first name of inserting person
        surname (str) : argument that takes the surname of inserting person
        gender (str) : argument that takes the gender of inserting person

        """
        if not Person.is_existing_person(name, surname):
            with create_connection() as conn:
                conn.execute(
                    text(
                        "INSERT INTO person (name, surname, gender) VALUES (:name, :surname, :gender)"
                    ),
                    {
                        "name": name,
                        "surname": surname,
                        "gender": gender if gender in ("male", "female") else "male",
                    },
                )

    @staticmethod
    def show_all_persons() -> None:
        """A method that displays all people in the database"""
        print(
            " Imię:".ljust(26),
            "Nazwisko:".ljust(25),
            "Płeć:",
            "\n ----------------------------------------------------------",
        )
        print(
            str(session.query(Person).all())
            .replace(",", "")
            .replace("[", " ")
            .replace("]", "")
        )

    @staticmethod
    def part_of_method_find_single_person(
        column: str, list_of_columns: list, what_we_try_to_find: str
    ) -> None:
        """Part of the "find_single_person" method that prevents code duplication"""
        dict_of_persons = {}
        times = -1
        is_return = False
        list_of_persons = list(session.query(Person).all())
        dict_of_persons[column] = list_of_columns
        values = list(*dict_of_persons.values())
        for name in values:
            times += 1
            if str(name).lower() == what_we_try_to_find.lower():
                print("", str(list_of_persons[times]).replace(",", "").strip())
                is_return = True
        if not is_return:
            print(" Nie ma osoby o podanych przez Ciebie danych")

    @staticmethod
    def find_single_person(where_to_find: str, what_to_find: str) -> None:
        """A method that allows you to find all the values given in the argument in the column given in the argument

        where_to_find (str) :  argument that takes the column we are going to search
        what_to_find (str) : argument that takes the information we are looking for in this column

        """
        list_of_persons = list(session.query(Person).all())
        names, surnames, genders = [], [], []
        print(
            " Imię:".ljust(26),
            "Nazwisko:".ljust(25),
            "Płeć:",
            "\n ----------------------------------------------------------",
        )
        for person in list_of_persons:
            names.append(person.name)
            surnames.append(person.surname)
            genders.append(person.gender)
        if where_to_find.lower() == "name":
            Person.part_of_method_find_single_person(
                what_we_try_to_find=what_to_find,
                list_of_columns=names,
                column="' name '",
            )
        elif where_to_find.lower() == "surname":
            Person.part_of_method_find_single_person(
                what_we_try_to_find=what_to_find,
                list_of_columns=surnames,
                column="'" "surname" "'",
            )
        elif where_to_find.lower() == "gender":
            Person.part_of_method_find_single_person(
                what_we_try_to_find=what_to_find,
                list_of_columns=genders,
                column="'" "gender" "'",
            )
        else:
            print(" Nie ma takiej kolumny")
