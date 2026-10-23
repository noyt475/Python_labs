import random
rand = random.randint(1, 100)

num = 0

while num != rand:
    print("Введите число: ")
    num = int(input())
    if num < rand:
        print("Больше")
    elif num > rand:
        print("Меньше")
    else:
         print("Код подобран!")
