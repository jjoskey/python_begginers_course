print('Объявим tuple переберём в цикле for и проверим на истинность, сделаем вывод по индексу')
user_roles = ('admin', 'editor', 'viewer')
for role in user_roles:
    print(role)
print('admin' in user_roles)
print('writer' in user_roles)
print(user_roles[0])
print()


print('Первый tuple хоть и в скобках, но без запятой это не tuple')
not_tuple = ('Gid')
print(type(not_tuple))   # Не tuple, один элемент
my_tuple = ('gid',)
print(type(my_tuple))    # Это tuple, запятой мы показываем это
print()


print('Распаковываем кортеж, важно, что бы кортеж был равен кол-ву переменных')
role_1, role_2, role_3 = user_roles
print(role_1)
print(role_2)
print(role_3)
print()


print('Распаковываем кортеж где второй элемент пропущен символом _')
role_4, _, role_6 = user_roles
print(role_4)
print(role_6)
print()


print('Распаковываем список, важно, что бы список был равен кол-ву переменных')
list_user_roles = ['admin', 'editor', 'viewer']
role_7, role_8, role_9 = user_roles
print(role_7)
print(role_8)
print(role_9)
print()