# Magyarországon a személyi számok 11 számjegyből állnak.
# Kérjünk be a felhasználótól egy személyi számot, és ellenőrizzük, valódi-e, ha tudjuk,
# hogy:  a 11. számjegyet úgy számoljuk ki, hogy az első számjegyet megszorozzuk 1-gyel,
# a másodikat 2-vel, s így tovább 10-ig. A szorzatokat összeadjuk és az eredményt elosztjuk 11-gyel.
# A maradék lesz a 11. számjegy.
# Írjuk ki, valódi-e a személyi szám vagy sem!

id = input()

sum = 0
idx = 0
lastLetter = None

for letter in id:
    idx += 1
    sum += int(letter) * idx
    lastLetter = letter

sum %= 11

if idx != 11:
    print('A megadott azonosito nem 11 szamjegybol all.')
    exit()

if sum == int(lastLetter):
    print('A szemelyi azonosito valodi.')

if sum != int(lastLetter):
    print('A szemelyi azonosito nem valodi.')
