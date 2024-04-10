fruits = ['banana', 'apple', 'cherry', 'date']
sorted_fruits = sorted(fruits)   
print(sorted_fruits)   # Вывод ['apple', 'banana', 'cherry', 'date']
sorted_fruits = sorted(fruits, reverse=True)   
print(sorted_fruits)   # Вывод ['date', 'cherry', 'banana', 'apple']


fruits = ['banana', 'apple', 'cherry', 'date']
def sort_by_len(element : str) -> int:
    return len(element)

sorted_fruits = sorted(fruits, key=sort_by_len)   
print(sorted_fruits)   # Вывод ['date', 'apple', 'banana', 'cherry']


people =  [
    {'name': 'Alice', 'age': 25},
    {'name': 'Nik', 'age': 21},
    {'name': 'Nina', 'age': 35},
    {'name': 'Anna', 'age': 21},
    {'name': 'Micasa', 'age': 25}   
]

def sort_by_age(person: dict) -> int:
    return person['age']

sorted_people_age = sorted(people, key=sort_by_age)
print(sorted_people_age)   # Вывод [{'name': 'Nik', 'age': 21}, {'name': 'Anna', 'age': 21}, {'name': 'Alice', 'age': 25}, {'name': 'Micasa', 'age': 25}, {'name': 'Nina', 'age': 35}]



def sort_by_age_name(element: dict) -> tuple[int, str]:
    return element['age'], element['name']

sorted_people_age_name = sorted(people, key=sort_by_age_name)
print(sorted_people_age_name)   # Вывод [{'name': 'Anna', 'age': 21}, {'name': 'Nik', 'age': 21}, {'name': 'Alice', 'age': 25}, {'name': 'Micasa', 'age': 25}, {'name': 'Nina', 'age': 35}]

# FILTER # FILTER # FILTER # FILTER # FILTER # FILTER # FILTER # FILTER # FILTER # FILTER # FILTER # FILTER 
# FILTER # FILTER # FILTER # FILTER # FILTER # FILTER # FILTER # FILTER # FILTER # FILTER # FILTER # FILTER 
# FILTER # FILTER # FILTER # FILTER # FILTER # FILTER # FILTER # FILTER # FILTER # FILTER # FILTER # FILTER 

def is_even(n: int) -> bool:
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

filtered_numbers = filter(is_even, numbers)
print(type(filtered_numbers))   # Вывод <class 'filter'>
print(filtered_numbers)   # Вывод <filter object at 0x0000019A75FFCC10>
# Обернем в лист
filtered_numbers = list(filter(is_even, numbers))
print(type(filtered_numbers))   # Вывод <class 'list'>
print(filtered_numbers)   # Вывод [2, 4, 6, 8]



people =  [
    {'name': 'Alice', 'age': 25},
    {'name': 'Nik', 'age': 15},
    {'name': 'Nina', 'age': 35},
    {'name': 'Anna', 'age': 14},
    {'name': 'Micasa', 'age': 18} 
]

def is_adult(person: dict) -> bool:
    return person['age'] >= 18

filtered_age_people = list(filter(is_adult, people))   # Фильтруем, оборачиваем в лист
filtered_age_people = sorted(filtered_age_people, key=sort_by_age)    # Сортируем по возрасту
print(filtered_age_people)   # Вывод [{'name': 'Micasa', 'age': 18}, {'name': 'Alice', 'age': 25}, {'name': 'Nina', 'age': 35}]
