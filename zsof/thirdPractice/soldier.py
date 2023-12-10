# Egy csatatéren egy tank lő egy katonára. A katona életerejét a bemeneten adja meg!
# A tank minden körben megsebzi a katonát. A sebzés mértékét a bemeneten adja meg!
# Addig lőjön a tank a katonára, míg az meg nem hal!
# Minden körben írja ki a katona maradék életerejét, végül a csata kimenetét!

max_life_power = int(input())
harm_per_round = int(input())

while max_life_power > 0:
    max_life_power -= harm_per_round

    if max_life_power <= 0:
        print("A katona eletereje most:", 0)
        print("A katona meghalt, a tank nyert!")
        break

    print("A katona eletereje most:", max_life_power)
    