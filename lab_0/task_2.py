password = input()
length = len(password)
letters = password.isalpha()
numbers = password.isdigit()
if length < 16:
    print("Слишком короткий")
elif letters or numbers:
    print("Слабый пароль")
else: 
    print("Надежный пароль")
