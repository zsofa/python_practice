# Egy autószervizben napi nyolc órában javítanak autókat.  Az átlagos javítási idő 45 perc.
# Hány autót sikerül megjavítani egy átlagos napon, ha tudjuk, hogy egyszer van ebédszünet,
# és minden harmadik javítás után tartanak a szerelők kávészünetet?
# Kérje be bemenetről az ebédszünet és a kávészünetek hosszát!
# Használja a "while" és "break" szerkezeteket!


lunch_break = int(input())
coffee_break = int(input())
work_time_with_lunch = 480 - lunch_break

car_calc = 0
while work_time_with_lunch >= 0:

    if work_time_with_lunch < 45:
        break

    if car_calc % 3 == 0:
        work_time_with_lunch -= coffee_break

    car_calc += 1
    work_time_with_lunch -= 45

print(car_calc)
