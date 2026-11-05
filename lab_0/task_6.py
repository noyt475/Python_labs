date = input("Введите дату рождения, День.Месяц: ");
day, month = date.split('.')
day = int(day)
month = int(month)

months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if month < 1 or month > 12 or day > months[month] or day < 1:
    print("Неверная дата.")
    exit()

zodiacs = [
    ("Водолей", 1, 20, 2, 18),
    ("Рыбы", 2, 19, 3, 20),
    ("Овен", 3, 21, 4, 19),
    ("Телец", 4, 20, 5, 20),
    ("Близнецы", 5, 21, 6, 20),
    ("Рак", 6, 21, 7, 22),
    ("Лев", 7, 23, 8, 22),
    ("Дева", 8, 23, 9, 22),
    ("Весы", 9, 23, 10, 22),
    ("Скорпион", 10, 23, 11, 21),
    ("Стрелец", 11, 22, 12, 21),
    ("Козерог", 12, 22, 1, 19)
]

for name, start_month, start_day, end_month, end_day in zodiacs:
    if (month == start_month and day >= start_day or 
    month == end_month and day <= end_day):
        print(f"{name}") 


# print("Ваш знак зодиака: ")
# if (month == 1 and day >= 20) or (month == 2 and day <= 18):
#     print("Водолей.")
# elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
#     print("Рыбы.")
# elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
#     print("Овен.")
# elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
#     print("Телец.")
# elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
#     print("Близнецы.")
# elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
#     print("Рак.")
# elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
#     print("Лев.")
# elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
#     print("Дева.")
# elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
#     print("Весы.!")
# elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
#     print("Скорпион.")
# elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
#     print("Стрелец.")
# else: 
#     print("Козерог.")

