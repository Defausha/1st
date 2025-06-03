# ВІДОБРАЖЕННЯ ТА ІНІЦІАЛІЗАЦІЯ ЗМІННИХ
name = 'John'  # string
age = 25  # integer
height = 1.67  # float
is_student = True  # False (boolean)
has_high_degree = None  # None

print(name)
print(age)
print(height)
print(is_student)
print(has_high_degree)

name, age = 'John', 25

print(name)
print(age)

name: str = 'John' # string
age: int = 25 # integer
height: float = 1.67 # float
is_student: bool = True # or False - boolean
has_high_degree: None = None # None - nothing

print(name)
print(age)
print(height)
print(is_student)
print(has_high_degree)

# ВІДОБРАЖЕННЯ КОМЕНТАРІВ
# Короткий коментар

fruit = 'apple'

"""
Тут може бути багато тексту, який необіхдний іншим
розробникам, щоб зрозуміти, що саме ви написали у своїй програмі
"""

print(fruit)

# ІМЕНУВАННЯ ЗМІННИХ
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

#ФОРМАТУВАННЯ ТА ВІДОБРАЖЕННЯ ЗМІННИХ
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

#ІНІЦАЛІАЛІЗАЦІЯ ЗМІННИХ ЗІ ЗНАЧЕННЯМИ З ІНШИХ ЗМІННИХ
width = 10
height = 5

# Обрахунок площі фігури
area = width * height
# Обрахунок периметру фігури
perimeter = 2 * (width + height)

print("Area", area)
print('Perimeter', perimeter)

#ПЕРЕВІРКА ТИПУ ЗМІННИХ
age = 25
weight = 25.0
room = '25'

# Перевірка типу даних
print(type(age), type(weight), type(room))

# Зміна типу даних
age = str(25)
weight = int(25.0)
room = float('25')

# Перевірка типу даних
print(type(age), type(weight), type(room))
print(age, weight, room)

# Що відбувається коли число має значення після коми і змінюється на ціле число?
age = 25.6
print(age, type(age))

Age = int(27.9)
print(Age, type(Age))

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

#СПИСКИ
#перший приклад
my_list = list()
my_list = []
my_list = [1, True, 2345, 457457, 'fruits', None]
print(my_list)

user = ['Oleh', 'Osadchuk']
print(user[0], user[1], sep='\t')

# другий приклад
my_list = [1, 2, 3, 5, 7, 346, 235, 235, 347, -435, -23, 0]
print(max(old_list), min(old_list))
my_list.append(16)
print(my_list)

# print(my_list[3])
my_list.insert(3, -100)
print(my_list)

my_list.pop()
print(my_list)

my_list.remove(-435)
print(my_list)

my_list.remove(235)
print(my_list)

my_list.pop(1)
print(my_list)

print(my_list.count(235))

print(len(my_list))

# третій приклад
my_list = [1, 2, 3, 5, 7, 346, 235, 235, 347, -435, -23, 0]

new_list = ['loop', 'start']

print(my_list, new_list, sep='\n')
my_list.extend(new_list)
print(my_list)

my_list.append(new_list)
print(my_list)

my_list.clear()
print(my_list)

# четвертий приклад
y_list = [1, 2, 3, 5, 7, 346, 235, 235, 347, -435, -23, 0]

print(my_list.index(347))
my_list.insert(my_list.index(347), 100000000)
print(my_list)

my_list[my_list.index(7)] = None
print(my_list)

my_list[10] = None
print(my_list)

# Копія списку
# перший приклад
old_list = [1, 2, 3, 5, 7, 346, 235, 235, 347, -435, -23, 0]

new_list = old_list
print(old_list, new_list, sep='\n')

new_list.append(6)
print(old_list, new_list, sep='\n')

# другий приклад
old_list = [1, 2, 3, 5, 7, 346, 235, 235, 347, -435, -23, 0]

new_list = old_list.copy()
print(old_list, new_list, sep='\n')

new_list.append(6)
print(old_list, new_list, sep='\n')

# Сортування списків
my_list = [1, 2, 3, 5, 7, 346, 235, 235, 347, -435, -23, 0]

sorted_list = sorted(my_list.copy())
print(sorted_list)

my_list.sort()
print(my_list)

my_list.sort(reverse=True)
print(my_list)

# Зрізаний список
my_list = [1, 2, 3, 5, 7, 346, 235, 235, 347, -435, -23, 0]

print(my_list[::-1]) # [0, -23, -435, 347, 235, 235, 346, 7, 5, 3, 2, 1]
print(my_list[-1]) # 0
print(my_list[3:]) # [5, 7, 346, 235, 235, 347, -435, -23, 0]
print(my_list[:6]) # [1, 2, 3, 5, 7, 346]
print(my_list[2:10]) # [3, 5, 7, 346, 235, 235, 347, -435]
print(my_list[:6:-1]) # [0, -23, -435, 347, 235]
print(my_list[:]) # [1, 2, 3, 5, 7, 346, 235, 235, 347, -435, -23, 0]
print(my_list[2:10:2]) # [3, 7, 235, 347]

my_list = [[1, 2, 3, 5], [7, 346, 235, 235], 347, -435, -23, 0]

print(my_list[1][1])
print(my_list[1][1:3])

# СЛОВНИКИ
# перший приклад
person = {'name': 'Oleh', "age": 22, "phone": "38(098)*********", 'student': False, 1243: ['test', 'failed']}
print(person)

print(person.get('name', 'Noname'))
print(person.get('phone', None))
print(person.get('lang', None))

print(person['age'])
print(person['lang']) #KeyError

# другий приклад
person = {'name': 'Oleh', "age": 22, "phone": "38(098)*********", 'student': False, 1243: ['test', 'failed']}
print(person)

new_data = {'location': 'Ukraine, Lviv', 'lang': "ukr"}
person.update(new_data)
print(person)
print(person.get('name', 'Noname'))
print(person.get('lang', None))

person.pop(1243)
print(person)

person["age"] = 100
print(person)

person['test'] = True
print(person)

person.update({(1, ): False})
print(person)

# Unite several dict into new one
dict_a = {'Alex':12, 'Olga':10}
dict_b = {'Boris':9, 'Kostya':10}
dict_c = {'Ira':11, 'Vova':6}

print(dict_a)
dict_a.update(dict_b)
print(dict_a)
dict_c.update(dict_a)
print(dict_c)

# об'єднання декількох словників через кому та їх сортування
dict_c.update(dict_a)
dict_c.update(dict_b)
print(dict_c)  # {'Ira': 11, 'Vova': 6, 'Alex': 12, 'Olga': 16, 'Boris': 9, 'Kostya': 10}

dict_c = dict(sorted(dict_c.items()))
print(dict_c)  # {'Alex': 12, 'Boris': 9, 'Ira': 11, 'Kostya': 10, 'Olga': 16, 'Vova': 6}

# заміна ключа
person = {'name': 'Oleh', "age": 22, "phone": "38(098)*********", 'student': False, 1243: ['test', 'failed']}
print(person)

person['test'] = person.pop(1243)
print(person)

test = person.pop('test')
print(test)

# МНОЖИНИ
# сортовані множини
my_list = [1, 2, 3, 5, 7, 346, 235, 235, 347, -435, -23, 0]
print(set(my_list))
print(sorted(set(my_list)))

# дії з множинами
my_set = {4, 6, 'test', 'Python', 100}
print(my_set)
my_set.add('Test')
print(my_set)

my_set.remove(6)
print(my_set)

my_set.discard('Test')
print(my_set)

my_set.discard(111)
print(my_set)

list_data_one = [1, 1, 2, 3, 5, 8, 13, 21, 7, 5, 100]
list_data_two = [11, 1, 21, 31, 15, 8, 13, 21, 7, 15, 101]

print(list(set(list_data_one) & set(list_data_two))) # in first and in second &(and)
print(list(set(list_data_one) | set(list_data_two))) # in first or in second |(or)
print(list(set(list_data_one) - set(list_data_two))) # in first and not in second -(minus)
print(list(set(list_data_one) ^ set(list_data_two))) # in first and not in second + in second and not in first

# Check if values in list is unique only
list_data_one = [1, 1, 2, 3, 5, 8, 13]
list_data_two = [11, 1, 21, 31, 15, 8]

print(len(list_data_one) == len(set(list_data_one)))
print(len(list_data_two) == len(set(list_data_two)))

# КОРТЕЖІ
my_tuple = (1, )
print(my_tuple, type(my_tuple))

my_tuple = (1)
print(my_tuple, type(my_tuple))

my_tuple = (1,2,3,4,5)
print(my_tuple, type(my_tuple))

# Tuple as dict keys
circle = {
    (0, 0): "Centre",
    (0, 1): "90",
    (1, 0): "0 or 360",
    (0, -1): "270",
    (-1, 0): "180",
}

print(circle.get((0, -1)))

# СТРОКИ
my_string = 'hello my liTTle friends!'

print(my_string) # hello my liTTle friends!
print(my_string.upper()) # HELLO MY LITTLE FRIENDS!
print(my_string.lower()) # hello my little friends!
print(my_string.startswith('hello')) # True
print(my_string.startswith('hi')) # False
print(my_string.endswith('!')) # True
print(my_string.endswith('.')) # False
print(my_string.title()) # Hello My Little Friends!
print(my_string.count('e')) # 3