# Magyarországon a személyi számok 11 számjegyből állnak.
# Kérjünk be a felhasználótól egy személyi számot, és ellenőrizzük, valódi-e, ha tudjuk,
# hogy:  a 11. számjegyet úgy számoljuk ki, hogy az első számjegyet megszorozzuk 1-gyel,
# a másodikat 2-vel, s így tovább 10-ig. A szorzatokat összeadjuk és az eredményt elosztjuk 11-gyel.
# A maradék lesz a 11. számjegy.
# Írjuk ki, valódi-e a személyi szám vagy sem!

id_num = str(input("Személyi szám: "))


def run():
    if len(id_num) != 11 or not id_num.isdigit():
        print("A megadott azonosito nem 11 szamjegybol all.")
    elif is_id(id_num):
        print("A szemelyi azonosito valodi.")
    else:
        print("A szemelyi azonosito nem valodi.")


def is_id(num):
    calc = 0
    for i in range(10):
        calc += int(num[i]) * (i + 1)

    print({calc})
    left = calc % 11
    print({left})
    return left == int(num[10])


run()


