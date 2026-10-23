fio = input()
surname, name, patronymic = fio.split()
surname = surname.capitalize()
name = name[0].upper()
patronymic = patronymic[0].upper()
result = f"{surname} {name}.{patronymic}."
print(result)