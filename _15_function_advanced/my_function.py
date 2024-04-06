print('Через *args добавляем в фунцию n количество символов')
def add_all (*args):
    summury = 0
    for num in args:
        summury += num
    return summury
print(add_all(1, 2, 3, 5, 7))
print()


print('Добавляем два списка через * в функцию')
values = [1, 2, 3, 4, 5]
other_values = [6, 7, 8, 9, 10]
print(add_all(*values, *other_values))
print()


print('Вызов функции с аргументами **kwargs')
def introduce(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)

person_1 = {
    'name': 'Kate',
    'age': 24,
    'city': 'Denver'
}
introduce(**person_1)
print()


print('Вызов функции с аргументами **kwargs')
def func_with_all_arguments(x: int, y: int, *args, value: int = 6, **kwargs):
    print(x, y)
    print(args)
    print(value)
    print(kwargs)

func_with_all_arguments(1, 2, 3, 4, 5, **person_1)
print()

print('Функция возвращает модифицированный словарь и несколько значений return')
def modify_dict(old_dict: dict, **kwargs) -> tuple[dict, bool]:
    is_modified = False                  # По умолчанию is_modified = False

    for key, value in kwargs.items():    # Раскладываем второе значение на ключ значение
        # print(old_dict.get(key))       # Что выводится для наглядности
        if old_dict.get(key) != value:   # Если в старом словаре по ключу из второго словаря kwargs, значение не ровно значению полученному из kwargs
            old_dict[key] = value        # Тогда старый словарь[ключ из kwargs] мы записываем через = значение переданное из kwargs
            is_modified = True           # Переменная is_modified становится True

    return old_dict, is_modified


product = {'id': 1, 'name': 'Laptop', 'price': 999.99, 'in_stock': False}   

# Передаем в kwargs словарь с in_stock=True, а в старом он был False, значит словарь поменяется.
structure, modify = modify_dict(old_dict=product, in_stock=True)    # Записываем два return в две переменные
print(f'Словарь {structure} был ли модифицирован {modify}')
print(type(structure))