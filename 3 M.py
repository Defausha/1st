#Для отримання поточної дати і часу використовується метод datetime.now()
import datetime
now = datetime.datetime.now()
print(now)

#У результаті виклику методу now() ми отримуємо об'єкт datetime, у якого є ряд корисних атрибутів:
from datetime import datetime

current_datetime = datetime.now()

print(current_datetime.year)
print(current_datetime.month)
print(current_datetime.day)
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.second)
print(current_datetime.microsecond)
print(current_datetime.tzinfo)

#щоб отримати дату (без часу) та час (без дати):
current_date = current_datetime.date()
current_time = current_datetime.time()

print(current_date)
print(current_time)

#об'єднати дату та час можна за допомогою методу combine():
import datetime

# Створення об'єктів date і time
date_part = datetime.date(2023, 12, 14)
time_part = datetime.time(12, 30, 15)

# Комбінування дати і часу в один об'єкт datetime
combined_datetime = datetime.datetime.combine(date_part, time_part)

print(combined_datetime)  # Виведе "2023-12-14 12:30:15"

# Для створення об'єкта datetime з певною датою:
specific_datetime = datetime.datetime(2023, 12, 14, 12, 30, 15)
print(specific_datetime)  # Виведе "2023-12-14 12:30:15"

# Метод weekday()
from datetime import datetime

# Створення об'єкта datetime
now = datetime.now()

# Отримання номера дня тижня
day_of_week = now.weekday()

# Поверне число від 0 (понеділок) до 6 (неділя)
print(f"Сьогодні: {day_of_week}")  

# Порівняння двох об'єктів datetime
from datetime import datetime

# Створення двох об'єктів datetime
datetime1 = datetime(2023, 3, 14, 12, 0)
datetime2 = datetime(2023, 3, 15, 12, 0)

# Порівняння дат
print(datetime1 == datetime2)  # False, тому що дати не однакові
print(datetime1 != datetime2)  # True, тому що дати різні
print(datetime1 < datetime2)   # True, тому що datetime1 передує datetime2
print(datetime1 > datetime2)   # False, тому що datetime1 не наступає за datetime2
print(datetime1 <= datetime2)  # True, тому що datetime1 не більше datetime2
print(datetime1 >= datetime2)  # False, тому що datetime1 не більше або рівно datetime2

# Об'єкт timedelta можна створити, задаючи тижні, дні, години, хвилини, секунди, мілісекунди і 
# мікросекунди, передавши один або кілька з таких параметрів:
from datetime import timedelta
delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)
print(delta)
# Об'єкт timedelta можна використовувати для арифметичних операцій з об'єктами datetime:
from datetime import datetime, timedelta

# Створення об'єкта datetime
now = datetime.now()

# Додавання timedelta до datetime
future_date = now + delta
print(f"Сьогодні: {now}")
print(f"Дата через 50 днів: {future_date}")

# Віднімання timedelta від datetime
past_date = now - delta
print(f"Дата 50 днів тому: {past_date}")
# Для отримання різниці між двома об'єктами datetime можна використовувати оператор віднімання:
from datetime import datetime

# Створення двох об'єктів datetime
datetime1 = datetime(2023, 3, 14, 12, 0)
datetime2 = datetime(2023, 3, 15, 12, 0)

# Отримання різниці між двома об'єктами datetime
difference = datetime2 - datetime1
print(f"Різниця: {difference}")
# Різниця буде об'єктом timedelta, який містить кількість днів, секунд і мікросекунд між двома датами
print(f"Днів: {difference.days}, Секунд: {difference.seconds}, Мікросекунд: {difference.microseconds}")

# Метод toordinal()
from datetime import datetime

# Створення об'єкта datetime
date = datetime(2023, 3, 14, 12, 0)

# Отримання порядкового номера дати
ordinal = date.toordinal()
print(f"Порядковий номер дати: {ordinal}")

# Метод fromordinal()
from datetime import datetime

# Створення об'єкта datetime з порядковим номером
date_from_ordinal = datetime.fromordinal(ordinal)
print(f"Дата з порядкового номера: {date_from_ordinal}")

# Метод strftime() для форматування дати і часу
from datetime import datetime

# Створення об'єкта datetime
now = datetime.now()

# Форматування дати і часу
formatted_date = now.strftime("%Y-%m-%d")
formatted_time = now.strftime("%H:%M:%S")

print(f"Сьогоднішня дата: {formatted_date}")
print(f"Поточний час: {formatted_time}")

# Метод strptime() для парсингу рядка в об'єкт datetime
from datetime import datetime

# Рядок з датою і часом
date_string = "2023-12-14 12:30:15"

# Парсинг рядка в об'єкт datetime
parsed_datetime = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

print(f"Порядковий номер дати: {parsed_datetime.toordinal()}")

# %Y - рік з чотирма цифрами (наприклад, 2023).
# %y - рік з двома цифрами (наприклад, 23).
# %m - місяць як номер (наприклад, 03 для березня).
# %d - день місяця як номер (наприклад, 14).
# %H - година (24-годинний формат) (наприклад, 15).
# %I - година (12-годинний формат) (наприклад, 03).
# %M - хвилини (наприклад, 05).
# %S - секунди (наприклад, 09).
# %A - повна назва дня тижня (наприклад, Tuesday).
# %a - скорочена назва дня тижня (наприклад, Tue).
# %B - повна назва місяця (наприклад, March).
# %b або %h - скорочена назва місяця (наприклад, Mar).
# %p - AM або PM для 12-годинного формату.

# Метод timestamp() для отримання часу в секундах з початку епохи
from datetime import datetime

# Створення об'єкта datetime
now = datetime.now()

# Отримання часу в секундах з початку епохи
timestamp = now.timestamp()
print(f"Час в секундах з початку епохи: {timestamp}")

# Метод fromtimestamp() для створення об'єкта datetime з часу в секундах
from datetime import datetime

# Створення об'єкта datetime з часу в секундах
date_from_timestamp = datetime.fromtimestamp(timestamp)
print(f"Дата з часу в секундах: {date_from_timestamp}")