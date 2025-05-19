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

def modify_string(original: str) -> str:
    original = "змінено"
    return original

str_var = "оригінал"
print(modify_string(str_var))  # виведе: змінено
print(str_var)                # виведе: оригінал

def modify_list(lst: list) -> None: # type: ignore
    lst.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # виведе: [1, 2, 3, 4]

def modify_list(lst: list) -> None:
    lst = lst.copy()
    lst.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # виведе: [1, 2, 3]

def string_to_codes(string: str) -> dict:
    # Ініціалізація словника для зберігання кодів
    codes = {}  
    # Перебір кожного символу в рядку
    for ch in string:  
        # Перевірка, чи символ вже є в словнику
        if ch not in codes:
            # Додавання пари символ-код в словник  
            codes[ch] = ord(ch)  
    return codes

result = string_to_codes("Hello world!")
print(result)
# Виведе: {'H': 72, 'e': 101, 'l': 108, 'o': 111, ' ': 32, 'w': 119, 'r': 114, 'd': 100, '!': 33}

x = 50

def func() -> None: # type: ignore
    x = 2
    print('Зміна локального x на', x)  # Зміна локального x на 2

func()
print('Глобальний x як і раніше', x)  # x як і раніше 50

def outer_func():
    enclosing_var = "Я змінна в функції, що охоплює"

    def inner_func():
        print("Всередині вкладеної функції:", enclosing_var)

    inner_func()

outer_func() #зміна enclosing  fun зсередини вкладеної fun, через nonlocal

def func_outer():
    x = 2

    def func_inner():
        nonlocal x
        x = 5

    func_inner()
    return x

result = func_outer()  # 5

x = 50

def func(): # type: ignore # type: ignore
    global x
    print('x дорівнює', x)  # x дорівнює 50
    x = 2
    print('Змінюємо глобальне значення x на', x)  # Змінюємо глобальне значення x на 2

func()
print('Значення x складає', x)# Значення x складає 2

def func(a, b=5, c=10):
    print('a дорівнює', a,', b дорівнює', b,', а c дорівнює', c)

# a дорівнює 3, b дорівнює 7, а c дорівнює 10
func(3, 7)

# a дорівнює 25, b дорівнює 5, а c дорівнює 24
func(25, c=24)

# a дорівнює 100, b дорівнює 5, а c дорівнює 50
func(c=50, a=100)

def say(message, times=1):
    print(message * times)

say('Привіт') 
say('Світ', 5)

def print_all_args(*args):
    for arg in args:
        print(arg)

print_all_args(1, 'hello', True)

def concatenate(*args) -> str:
    result = ""
    for arg in args:
        result += arg
    return result

print(concatenate("Hello", " ", "world", "!"))

def factorial(n): # type: ignore
    if n == 0: # базовий випадок
        return 1
    else:
        return n * factorial(n-1) # рекурсивний випадок

print(factorial(5)) # виведе 120

def fibonacci(n):
    if n <= 1: # базовий випадок
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2) # рекурсивний випадок

print(fibonacci(10)) # виведе 55

def factorial(n):
    print("Виклик функції factorial з n = ", n)
    if n == 1:
        print("Базовий випадок, n = 1, повернення 1")
        return 1
    else:
        result = n * factorial(n-1)
        print("Повернення результату для n = ", n, ": ", result)
        return result

print(factorial(5))
