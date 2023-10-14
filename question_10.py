def triple_number(x):
    return 3 * x
numbers = []
max=int(input('enter the number of items in list'))
for i in range(max):
    num=int(input(f'enter {i+1} value '))
    numbers.append(num)
tripled_numbers = list(map(triple_number, numbers))
print("Original Numbers:", numbers)
print("Tripled Numbers:", tripled_numbers)
"""
expected output
enter the number of items in list5
enter 1 value 1
enter 2 value 2
enter 3 value 3
enter 4 value 4
enter 5 value 5
Original Numbers: [1, 2, 3, 4, 5]
Tripled Numbers: [3, 6, 9, 12, 15]
"""