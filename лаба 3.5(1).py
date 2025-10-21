name = input()
if len(name) < 2:
    print("чудовищно мало")
elif len(name) <5:
    print("очень мало")
elif len(name) <10:
    print("мало")
elif len(name) <30:
    print("ок")
elif len(name) <100:
    print("много")
else:
    print("чудовищно много")