# Írjunk egy rendszámellenőrző Python-programot! Tudjuk, hogy a hagyományos rendszám formátuma
# három betűből, egy kötőjelből és három számból áll, pl. ABC-123.
# Kérjünk be egy rendszámot a felhasználótól, és írjuk ki, megfelelő-e a rendszám!
# Ha nem, azt is írjuk ki, miért nem!

licence_plate = str(input())

if len(licence_plate) == 7:
    if licence_plate[3] == '-':
        if licence_plate[:3].isalpha():
            if licence_plate[4:].isdigit():
                print("A megadott rendszam helyes formatumu.")
            else:
                print("Az utolso harom karakternek szamjegyeknek kell lenniuk.")
        else:
            print("Az első három karakternek betuknek kell lenniuk.")
    else:
        print("A negyedik karakternek kotojelnek kell lennie.")
else:
    print("Helytelen rendszam hossz.")
