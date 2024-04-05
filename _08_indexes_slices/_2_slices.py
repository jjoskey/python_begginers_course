numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[0:5])             # Outputs: [0, 1, 2, 3, 4]
new_numbers = numbers[0:5]      # Save in new_numbers slice [0:5]
print(new_numbers)              # Outputs: [0, 1, 2, 3, 4]
print(numbers[0:10])            # Outputs: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[0:len(numbers)])  # Outputs: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[:])               # Outputs: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[:5])              # Outputs: [0, 1, 2, 3, 4]
print(numbers[5:])              # Outputs: [5, 6, 7, 8, 9]
print(numbers[0:10:2])          # Outputs: [0, 2, 4, 6, 8]
print(numbers[::2])             # Outputs: [0, 2, 4, 6, 8]
print(numbers[3:2])             # Outputs: []
print(numbers[0:20])            # Outputs: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[-5:-1])           # Outputs: [5, 6, 7, 8]
print(numbers[::-1])            # Outputs: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


string = "Hello, world!"
print(string[0:5])   # Outputs: 'Hello'
print(string[7:])    # Outputs: 'world!'
print(string[::2])   # Outputs: 'Hlo ol!'
print(string[::-1])  # Outputs: '!dlrow ,olleH'
print(string[2:1])   # Outputs: ''fd
