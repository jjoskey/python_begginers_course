import json

book = {
    'title': '1984',
    'author': 'George Orwell',
    'isbn': '978-0451524935',
    'uuid': 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11',
    'count': 30,
    'genres': ['dystopia']
}

json_string = json.dumps(book)

print(type(json_string))
print(json_string)

json_string_1 = {"title": "1984", "author": "George Orwell", "isbn": "978-0451524935", "uuid": "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"}

book = json.loads(json_string)
print(type(json_string_1))
print(json_string_1)