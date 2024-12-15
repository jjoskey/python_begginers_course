my_set = {1, 2, 3, 4, 5, 6}

my_set1 = set()
for i in range(5):
    my_set1.add(i)
my_set1.remove(2)    # Удалили двойку
print(my_set1)   # Вывод {0, 1, 3, 4}


my_set2 = {1, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5}
print(my_set2)   # Вывод {1, 2, 3, 4, 5}


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6 ,7 ,8}
# Объединение сетов - складывает два множества
print(set1.union(set2))   # Вывод {1, 2, 3, 4, 5, 6, 7, 8}
# Пересичение сетов - общие значения двух множеств
print(set1.intersection(set2))   # Вывод {4, 5}
# Различие сетов - элементы множества которые отсутсвуют во втором множестве
print(set1.difference(set2))   # Вывод {1, 2, 3}

squares = {x ** 2 for x in range(10)}
print(squares)

print({1, 2, 3} == {3, 2, 1})   # Вывод True


numbers = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7]
#unique_numbers = set(numbers)
#unique_numbers = list(unique_numbers)
unique_numbers = list(set(numbers))   # Преобразовываем множество сразу в лист
print(unique_numbers)
