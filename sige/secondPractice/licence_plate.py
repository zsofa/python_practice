# Írjunk egy rendszámellenőrző Python-programot! Tudjuk, hogy a hagyományos rendszám formátuma
# három betűből, egy kötőjelből és három számból áll, pl. ABC-123.
# Kérjünk be egy rendszámot a felhasználótól, és írjuk ki, megfelelő-e a rendszám!
# Ha nem, azt is írjuk ki, miért nem!

plate = input()

if len(plate) > 7:
    print("Helytelen rendszam hossz.")
    exit()

for i, char in enumerate(plate):
    if i == 3 and char != '-':
        print("A negyedik karakternek kotojelnek kell lennie.")
        exit()
    if i > 3 and not char.isnumeric():
        print("Az utolso harom karakternek szamjegyeknek kell lenniuk.")
        exit()
    if i > 6:
        print("Helytelen rendszam hossz.")
        exit()

print("A megadott rendszam helyes formatumu.")
