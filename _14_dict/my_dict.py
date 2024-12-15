print('Вывод объявленного словаря')
person = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}
print(person)
print()


print('Добавляем в словарь key:value')
person['job'] = 'Engineer'
print(person)
print()


print('Объявляем словарь по другому')
person_2 = {}
person_2['name'] = 'Lise'
person_2['age'] = 21
person_2['city'] = 'Nevada'
print(person_2)
print()


print('Вывод значения по ключу')
print(person_2['city'])   # <--- Вывод города
# print(person_2['country'])   <--- Запрос неизвестного ключа выдаст ошибку KeyError
print(person_2.get('city'))   # <--- Тоже вывод города
print(person_2.get('country'))   # <--- Вывод страны, выведет None, так как нет ключа
print(person_2.get('country', 'USA'))   # <--- Выведет USA так как ключа нет, но указано значение по умолчанию
print(person_2.get('city', 'Colorado'))   # <--- Выведет Nevada, хоть и указано значение по умолчанию, но такой ключ в словаре есть
print()


print('Вывод ключей и значений через циклы')
for k in person_2:   # Вывод только ключей
    print(k)
for k in person_2:   # Вывод только ключей
    print(person[k])
print()
# Распаковка key:value в виде tuple
for item in person_2.items():
    print(item, '    <----->    ', type(item))
    key, value = item   # Распаковка кортежа из item - key: value
    print(key, value)   # Вывод распакованного кортежа
print()
# Распаковка сразу по key:value
for key, value in person_2.items():
    print(key)
    print(value)
print()
# Итерация только по key
for key in person_2.keys():
    print(key)
print()
# Итерация только по value
for value in person_2.values():
    print(value)
print()


print('Сравнение словарей, порядок key не важен ключи всегда уникальные')
person_3 = {
    'name': 'Rick',
    'age': 24,
    'city': 'Dublin'
}
person_4 = {
    'city': 'Dublin',
    'age': 25,
    'name': 'Rick'
}
person_5 = {
    'name': 'Kate',
    'age': 24,
    'city': 'Denver'
}
x = [25]
if person_3['age'] == max(x):
    print(person_3)
else:
    print(person_4)
# print(person_3 == person_4)   # Вывод True так как key and value одинаковые, равные
# print(person_3 == person_5)   # Вывод False так как value разные либо разные ключи
# print()


print('Объединение двух словарей')
person_6 = {
    'name': 'Kate',
    'age': 24,
    'city': 'Denver'
}
print(person_6)
additional_person_info = {
    'job': 'Engineer',
    'age': 25,
    'married': True,
    'city': 'Nevada'
}

person_6.update(additional_person_info)   # Метод добавляет в первый словарь недостающие key и заменяет у имеющихся key значения на новые
# person_6 = person_6 | additional_person_info   # Метод идентичен верхнему, просто другой синтаксис
print(person_6)


