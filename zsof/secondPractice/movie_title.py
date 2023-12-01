# Kérjünk be a felhasználótól egy tetszőleges filmcímet, és nézzük meg, szerepelt-e benne 'a' karakter!
#
# Elvárt kimenet:
# "Az 'a' karakter szerepel, és eloszor az elso feleben szerepelt." VAGY
# "Az 'a' karakter szerepel, de a masodik feleben szerepelt." VAGY
# "Sajnos az 'a' karakter nem szerepelt a szovegben."

movie_title = str(input())

half = len(movie_title) + 1 / 2

if 'a' in movie_title:
    print(movie_title.index('a'))
    first_part = movie_title.index('a') < len(movie_title) / 2
    if first_part:
        print("Az 'a' karakter szerepel, és eloszor az elso feleben szerepelt.")
    else:
        print("Az 'a' karakter szerepel, de a masodik feleben szerepelt.")

else:
    print("Sajnos az 'a' karakter nem szerepelt a szovegben.")


