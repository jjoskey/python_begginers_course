fruits = ['apple', 'banana', 'cherry']
print(fruits)          # Выводит список
print(len(fruits))     # Выводит кол-во элементов в списке
print()

element1 = 'apple'
element2 = 'banana'
element3 = 'cherry'
fruits_1 = [element1, element2, element3]
print(fruits_1)
print()


print('В списках могут хранится str, int, float, bool, list')
my_list = ['apple', 1, 1.5, True, [1, 2, 3]]
print(my_list)
print()

print('Сравнение списков')    # Сравнение элементов происходит по их индексам
my_ls1 = [1, 2, 3]
my_ls2 = [1, 3, 2]
my_ls3 = [1, 2, 3]
print(my_ls1 == my_ls2)   # Сравниваем списки вывод: False
print(my_ls1 == my_ls3)   # Сравниваем списки вывод: True
print()


print('Вывод bool при пустом списке и при списке со значением')
print(bool([]))
print(bool([0]))   # Даже если значение в списке цифра 0, то выведет True
print()


print('Проверяем содержится то или иное значение в списке с помощью in')    # Регистр важен
fruits_2 = ['apple', 'banana', 'cherry']
print('banana' in fruits_2)   # Вывод True
print('lemon' in fruits_2)    # Вывод False
print()


print('Передаем переменную str в список, она разбивается на отдельные символы')
word = 'hello my little friend'
my_ls4 = list(word)
print(my_ls4)
print()


print('Сложение списков друг с другом')
my_ls5 = [1, 2, 3]
my_ls6 = [4, 5, 6]
my_ls5_plus_ls6 = my_ls5 + my_ls6
print(my_ls5_plus_ls6)
print()


print('Добавляем элементы в список')
fruits_3 = ['apple', 'banana', 'cherry']
fruits_3.append('watermelon')   # Добавляем элемент
print(fruits_3)
print()


print('Метод list.pop(index) убирает из списка по индексу и сохраняет в переменную если она есть.')
fruits_4 = ['apple', 'banana', 'cherry']
fruit = fruits_4.pop(0)   # Метод убирает из списка по индексу и сохраняет в переменную. Default index [-1]
print(fruit)
print(fruits_4)
print()

print('Добавляем в список элементы других коллекций методом list.extend()')
# Добавляет элементы любой коллекции не удаляя из неё элементы.
fruits_5 = ['apple', 'banana', 'cherry']    # Первоначальный список
fruits_6 = ['fig', 'grape', 'watermelon']   # Второй список, строк
list_int = [5, 6, 7]        # Список цифр
tuple_int = (1, 4, 8)       # Кортеж цифр
set_1 = set('Goody')         # Set со строкой типа str
fruits_5.extend(list_int)   # Добавляет элементы списка цифр
fruits_5.extend(tuple_int)   # Добавляет элементы кортеж цифр
fruits_5.extend(fruits_6)   # Добавляет элементы списка строк
fruits_5.extend(set_1)      # Добавляет элементы множества set
print(fruits_5)
print(fruits_6)
print()


print('Разворачиваем список')
fruits_7 = ['apple', 'banana', 'watermelon', 'cherry']
print(fruits_7)
fruits_7.reverse()
print(fruits_7)
print()

 
print('Сортируем список методом list.sort() и list.sort(reverse = True)')
my_ls7 = [9, 600, 85, 111, 25, 400, 320, 1]
my_ls7.sort()                 # Сортируем список
print(my_ls7)                 # Выводим список
my_ls7.sort(reverse = True)   # Сортируем в обратном порядке
print(my_ls7)                 # Выводим список
print()


print("Используем для разделения строки метод .split() и для соединения метод ' '.join()")
my_string_1 = 'I Love the blue sky'
my_ls8 = my_string_1.split(' ')   # Разделяем строку str через разделитель пробел (' ').
print(my_ls8)
my_string_2 = ' '.join(my_ls8)    # Соединяем список слов используя разделитель пробел ' '.
print(my_string_2)
print()

print('Выводим из списка int максимальное число, минимально число и сумму чисел')
my_ls9 = [4, 67, 77, 34, 23, 2809, 5650]
print(my_ls9)
print(max(my_ls9))
print(min(my_ls9))
print(sum(my_ls9))
alf = 'zxcvbnmasdfghjklqwertyuiopAZ'
my_ls10 = list(alf)
print("максимальная буква", max(alf))
print('минимальная буква', min(alf))