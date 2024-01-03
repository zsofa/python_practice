# Kérjünk be a felhasználótól egy tetszőleges filmcímet, és nézzük meg, szerepelt-e benne 'a' karakter!
#
# Elvárt kimenet:
# "Az 'a' karakter szerepel, és eloszor az elso feleben szerepelt." VAGY
# "Az 'a' karakter szerepel, de a masodik feleben szerepelt." VAGY
# "Sajnos az 'a' karakter nem szerepelt a szovegben."

title = input()

if 'a' in title:
    index = title.index('a')
    if index < len(title) / 2:
        print('Az \'a\' karakter szerepel, es eloszor az elso feleben szerepelt.')
    else:
        print('Az \'a\' karakter szerepel, de a masodik feleben szerepelt.')
else:
    print('Sajnos az \'a\' karakter nem szerepelt a szovegben.')
