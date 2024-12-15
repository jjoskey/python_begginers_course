my_string = "Hello, world!"
my_string = 'Hello, world!'
my_string = """
Python is an incredibly versatile programming language that has rapidly gained popularity 
and recognition in the world of technology. It is known for its simplicity, readability, 
and ease of learning, making it an ideal language for beginners.
"""


first_name = "Alice"
last_name = "Smith"
full_name = first_name + " " + last_name
print(full_name)  # Output: Alice Smith
length = len(full_name)
print(length)  # Output: 11


print(len(""))  # Output: 0


my_integer = 100
my_string = str(my_integer)
print(my_string, type(my_string))  # Outputs: 100 <class 'str'>


my_integer = int("10")
print(type(my_integer), my_integer)  # Outputs: <class 'int'> 10
# my_integer = int("Yo!")  # raise error


my_string = input("Enter a number: ")
print(type(my_string), my_string)  # Outputs: <class 'str'>
my_integer = int(my_string)
print(type(my_integer), my_integer)  # Outputs: 10


big_integer = 2 ** 1000
print(len(str(big_integer)))


my_string = "Hello, world!"
print("Hello" in my_string)  # Outputs: True
print("hello" in my_string)  # Outputs: False
