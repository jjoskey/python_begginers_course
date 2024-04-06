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


# Моё решение вариант 1
def get_best_students(student):
    top_students = []
    score_max = []
    for i in range(len(student)):
        #print(student[i])
        if (student[i]['grades']) is not None:
            student[i]['grades'] = (sum(student[i]['grades']) / len(student[i]['grades']))
            score_max.append(student[i]['grades'])
        else:
            student[i]['grades'] = 0
            score_max.append(student[i]['grades'])
        #if student[i]['grades'] == max(score_max):
            
    for i in range(len(student)):
        if student[i]['grades'] == max(score_max):
            top_students.append(student[i])
    return top_students
        


# print(get_best_students(students))
# print(students[3])

# Моё решение вариант 2, правильный.
def best_students(students):
    top_students = []
    score_max = []
    for student in students:
        print(student)
        if (student['grades']) is not None:
            student['grades'] = (sum(student['grades']) / len(student['grades']))
            score_max.append(student['grades'])
        else:
            student['grades'] = 0
            score_max.append(student['grades'])
         #if student['grades'] == max(score_max):
            
    for student in students:
        if student['grades'] == max(score_max):
            top_students.append(student)
    return top_students
        


# print(best_students(students))


# лучшее решение вариант 3, правильный.
def best_students(students):                                  # Объявили функцию
    top_students = []                                         # Объявили лист
    score_max = 0                                             # Объявили переменную int
    for student in students:                                  # Цикл по листу словарей. Где каждая итерация передаёт словарь по индексу от [0] до [5]
        #print(student)                                       # Вывод словарей по очереди
        grade = student['grades']                             # В переменную grade кладём значение 'grades' итерируемого студента
        if (grade) is not None:                               # Если переменная не является None, выполняем тело условия
            grade_this_student = (sum(grade) / len(grade))    # В новую переменную итерируемого студента вносим среднее значение
        else:
            grade_this_student = 0                            # Если переменная None присваиваем переменной 0
        if grade_this_student > score_max:                    # Если grade итерируемого больше переменной score_max 
            score_max = grade_this_student                    # То в Score_max записываем число из grade итерируемого
            top_students = [student]                          # И в переменную top_students кладем list [итерируемого словаря]
        elif grade_this_student == score_max:                 # Если grade итерируемого равняется score_max        
            top_students.append([student])                    # То в список студентов, добавляем [итерируемого студента] в list
            
    return top_students
        


print(best_students(students))