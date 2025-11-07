text = input()
lenght = len(text)
if lenght < 2:
    print("Чудовищно мало")
elif lenght >= 2 and lenght < 5:
    print("Очень мало")
elif lenght >= 5 and lenght < 10:
    print("Мало")
elif (lenght >= 10 and lenght < 30) or lenght == 10:
    print("Ok")
elif (lenght >= 30 and lenght < 100) or lenght == 30:
    print("Много")
elif lenght >= 100:
    print("Чудовищно много")