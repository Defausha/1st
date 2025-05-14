print("Hello, world")
print("How are you doing toay?")
num = 15  # приклад значення для num

if num > 10:
    print("num більше за 10")
else:
    print("num не більше за 10")

money = 0
if money:
    print(f"You have {money} on your bank account")
else:
    print("You have no money and no debts")

result = None
if result:
    print(result)
else:
    print("Result is None, do something")

x = [1, 2, 3]
y = x
c = [1, 2, 3]

print(x is y)  # True
print(x is c)  # False

# Задаємо конкретне число
num = int(15)  

# Перевіряємо кратність
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)

def determine_quadrant(x, y):
    if x >= 0:
        if y >= 0:  # x > 0, y > 0
            print("Перша чверть")
        else:  # x > 0, y < 0
            print("Четверта чверть")
    else:
        if y >= 0:  # x < 0, y > 0
            print("Друга чверть")
        else:  # x < 0, y < 0
            print("Третя чверть")

fruit = "apple"

match fruit:
    case "apple":
        print("This is an apple.")
    case "banana":
        print("This is x banana.")
    case "orange":
        print("This is an orange.")
    case _:
        print("Unknown fruit.")

pets = ["dog", "fish", "cat"]

match pets:
    case ["dog", "cat", _]:
        # Випадок, коли є і собака, і кіт
        print("There's x dog and x cat.")
    case ["dog", _, _]:
        # Випадок, коли є тільки собака
        print("There's x dog.")
    case _:
        # Випадок для інших комбінацій
        print("No dogs.")

k = 0
while k < 10:
    k = k + 1
    print(k)

x = 0
while x < 6:
    x = x + 1
    if not x % 2:
        continue
    print(x)

for i in range(5):
    print(i)

for i in range(2, 10):
    print(i)

for i in range(0, 10, 2):
    print(i)

for i in range(0, 10, 5):
    print(i)

some_list = ["apple", "banana", "cherry"]
for index, value in enumerate(some_list):
    print(index, value)

list1 = ["зелене", "стигла", "червоний"]
list2 = ["яблуко", "вишня", "томат"]
for number, letter in zip(list1, list2):
    print(number, letter)

numbers = {
    1: "one",
    2: "two",
    3: "three"
}

for key in numbers:
    print(key)

for key in numbers.keys():
    print(key)

for val in numbers.values():
    print(val)

for key, value in numbers.items():
    print(key, value)

val = 'x'
try:
    val = int(val)
except ValueError:
    print(f"val {val} is not x number")
else:
    print(val > 0)
finally:
    print("This will be printed anyway")

def say_hello():
		# тіло функції
    print('Привіт, Світ!')

# Кінець функції say_hello()

# виклик функції
say_hello()

# ще один виклик функції
say_hello()

def print_max(x, y):
    if x > y:
        print(x, 'максимально')
    elif x == y:
        print(x, 'дорівнює', y)
    else:
        print(y, 'максимально')

x = 10
y = 7
print_max(x, y)  # передача змінних як аргументів

def add_numbers(num1: int, num2: int) -> int:
    sum = num1 + num2
    return sum

result = add_numbers(5, 10)
print(result)  # Виведе: 15

def greet(name: str) -> str:
    return f"Привіт, {name}!"

greeting = greet("Олексій")
print(greeting)  # Виведе: Привіт, Олексій!

def is_even(num: int) -> bool:
    return num % 2 == 0

check_even = is_even(4)
print(check_even)  # Виведе: True
