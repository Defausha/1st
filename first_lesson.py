# Правильне іменування змінних
name = "John"
age = 25
is_student = True

# Правильне використання констант
PI = 3.14159
MAX_VALUE = 100
DEFAULT_NAME = "John Doe"

# Правильне іменування змінних з використанням змінних з інших змінних
width = 10
height = 5
area = width * height

# Неправильне іменування змінних
n = "John"  # непояснююче ім'я змінної
x = True    # непояснююче ім'я змінної
f = 10.5    # непояснююче ім'я змінної

# Неправильне іменування змінної з використанням цифр та спецсимволів
2variable = "Invalid"   # початок змінної з цифри
$price = 100            # початок змінної зі спецсимволу

# Неправильне іменування змінних з використанням зарезервованих слів
class = "Invalid"       # зарезервоване слово використовується як назва змінної
if = True               # зарезервоване слово використовується як назва змінної

name = 'Alice'
age = 30

message = f'My name is {name}. I am {age/2} years old'
print(message)

print(f'My name is {name}. I am {age/2} years old')

message = 'Test 2. My name is {}. I am {} years old'.format(name, age)
print(message)

message = 'Test 3. My name is %s. I am %d years old' % (name, age)
print(message)

message = 'Test 4. My name is ' + name + '. I am ' + str(age) + ' years old'
print(message)

# Логічні вирази
value_one = 5
value_two = 7

print('Equal', value_one == value_two)
print('Not Equal', value_one != value_two)
print('Greater', value_one > value_two)
print('Lower', value_one < value_two)
print('Greater Equal', value_one >= value_two)
print('Lower Equal', value_one <= value_two)

# Оператори присвоєння
value_one = 5
value_two = 7
value_three = -19

"""
57 -> 57
-99 -> 99
"""

summary = 0
summary += abs(value_one) # abs - модуль числа
print(summary)
summary += abs(value_two)
print(summary)
summary += abs(value_three)
print(summary)

#Перевірка ідентичності
sentence_one = "Hello world"
sentence_two = "Hello " + "world"
# Відображення змінних
print(sentence_one, sentence_two, sep='\n')

# Перевірка рівності і ідентичності
print(f'Are sentence equal? {sentence_one == sentence_two}')
print(f'Are sentence identical? {sentence_one is sentence_two}') # is - перевірка ідентичності об'єктів
#виведить, що вони не ідентичні

# Перевірка місця збереження у памяті
print(f'Path of sentence in memory {id(sentence_one)}')
print(f'Path of sentence in memory {id(sentence_two)}')
# виведе різні адреси, бо це різні об'єкти

#Задача

'''
Скласти програму визначення номера під'їзду та поверху квартири за заданим номером квартири. 
У будинку 5 поверхів і 4 квартири на поверсі.
'''
FLOORS = 5
APARTMENTS_PER_FLOOR = 4

apartment_number = int(input('Enter apartment number: ')) 
apartments_per_entrance = FLOORS * APARTMENTS_PER_FLOOR
entrance_number = (apartment_number - 1) // apartments_per_entrance + 1 # -1/+1 викор. для приведення до 0-індексації (людських чисел) 
floor_number = ((apartment_number - 1) % apartments_per_entrance) // APARTMENTS_PER_FLOOR + 1 # % дає залишок від ділення (прикл.: 17 % 20 = 3), // - цілочисельне ділення (33 // 4 = 8, але цифра простого ділення була б 8.25)
print(f"Entrance number {entrance_number}, Floor number {floor_number}")