word = input()
drow = word[::-1]
if word == drow:
    print("Палиндром — подозрительный маркер")
else:
    print("Обычное слово")
 