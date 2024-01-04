# Kérjünk be a felhasználótól két szót, írassuk ki, egyforma hosszúak-e!
# Ha nem, írassuk ki, melyik szó hosszabb, és hány karakterrel!

first = input()
second = input()

firstLenght = len(first)
secondLenght = len(second)

diff = firstLenght - secondLenght

if diff == 0:
    print('A ket szo egyforma hosszu.')

if diff < 0:
    print(f'A ket szo kozul a {second} a hosszabb, {abs(diff)} karakterrel.')

if diff > 0:
    print(f'A ket szo kozul a {first} a hosszabb, {diff} karakterrel.')
