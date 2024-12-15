# задание
# Есть список словарей со студентами `students`. В каждом объекте есть имя и фамилия студента,
# а также список оценок (целых чисел). Нужно написать функцию get_best_students, которая берёт студентов и находит того,
# у кого средний балл наибольший. Возвращает функция список студентов с лучшим баллом. У некоторых студентов в оценках
# есть None: их среднюю оценку мы считаем равной 0.


students = [
    {"name": "John", "surname": "Doe", "grades": [5, 5, 4, 4]},
    {"name": "Jane", "surname": "Doe", "grades": [4, 3, 4, 3, 5]},
    {"name": "Bill", "surname": "Gates", "grades": [5, 5, 5, 3]},
    {"name": "Steve", "surname": "Jobs", "grades": [3, 5, 4, 3, 3, 5]},
    {"name": "Guido", "surname": "Van Rossum", "grades": [5, 3, 5, 4, 5, 5, 3, 5]},
    {"name": "Elon", "surname": "Musk", "grades": None}
]


# решение


def get_best_students(*, students: list[dict]) -> list[dict]:
    best_students = []
    best_average_grade = 0
    for student in students:
        grades = student["grades"]
        print(grades)
        if grades is None:
            average_grade = 0
        else:
            average_grade = sum(grades) / len(grades)
        if average_grade > best_average_grade:
            best_average_grade = average_grade
            best_students = [student]
        elif average_grade == best_average_grade:
            best_students.append(student)
    return best_students


print(get_best_students(students=students))  # Outputs: [{'name': 'John', 'surname': 'Doe', 'grades': [5, 5, 5, 4]}, {"name": "Bill", "surname": "Gates", "grades": [5, 5, 5, 3]}]
