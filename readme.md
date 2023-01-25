## Aplikacja pozwala na dodawanie, przechowywanie i wyświetlanie danych dotyczących studentów (ich danych osobowych i ocen) oraz grup i szkół, do których przynależą.


**Aby utworzyć nową szkołę należy użyć następującej komendy:**\
   ``<obiekt przechowujący szkołę> = School("<nazwa szkoły>")``\
*Przykład:* \
```school_1 = School("Nazwa szkoły")```

**Aby utworzyć nową grupę przedmiotową w danej szkole:**\
```<zmienna przechowująca grupę> = Group(<obiekt typu szkoła>, "<nazwa grupy>">)```\
```<obiekt typu szkoła>.add_group(<obiekt typu grupa>)```\
*Przykład:*\
```group_1 = Group(school_1, "history group")```\
```school_1.add_group(group_1) ```

**Aby utworzyć nowego studenta należy:**
>**Utworzyć osobę:**\
```<zmienna przechowująca osobę> = Person("<imię>", "<nazwisko>", "<płeć>")```\
*Przykład:*\
```person_1 = Person("Aleksandra", "Grzesiak", "female")```


Płeć może przyjmować wartośći: "male" lub "female".\
W przypadku podania innej wartości, automatycznie zostanie przypisana "male".


 >**Utworzyć studenta na podstawie osoby:**\
```<zmienna przechowująca studenta> = Student(<obiekt typu osoba>)```\
*Przykład:*\
```student_1 = Student(person_1)```
 
Student otrzymuje kolejny numer albumu z zakresu zaczynającego się od 100.

**Aby dodać studenta do grupy:**\
```<obiekt typu grupa>.add_student(<obiekt typu student>)```\
*Przykład:*\
```group_1.add_student(student_1)```

W grupie nie może być więcej niż 5 studentów.


**Aby dodać ocenę dla studenta w danej grupie:**\
```<obiekt typu grupa>.add_grade(<obiekt typu student>, <ocena>)```\
*Przykład:*\
```group_1.add_grade(student_1, 5)```

Dozwolone są oceny będące liczbami całkowitymi z zakresu od 2 do 5.



## **Aplikacja pozwala na wyświetlanie (z wykorzystaniem intuicyjnego interfejsu):**
* listy osób w grupie (nr albumu)
* listy wszystkich studentów (nr albumu) dla szkoły
* listy osób dla grupy z ocenami (nr albumu, ocena)
* listy osób dla grupy bez ocen, (nr albumu)
* listy osób dla szkoły, bez ocen (bez podziału na grupy)
* liczby studentów łącznie
* listy grup zajęciowych z liczbą studentów (id grupy, nazwa, liczba_studentów)


