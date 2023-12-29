# Valósítson meg shopping(prices) függvényt. A függvény bemenetként boltok listáját kapja. Minden bolt egy-egy szótár, ahol a kulcsok termékek nevei, az értékek pedig a termékhez tartozó árakat jelölik. A célunk, hogy venni szeretnénk tejet, kenyeret és tojást. Mindegyikből egyet-egyet. Nézzük meg, hogy a 3 terméket melyik boltban célszerű megvenni. A célunk, hogy minél kevesebbet költsünk.
#
# A függvény visszatérési értéke 2 tagból álljon:
#
# Annak a boltnak az indexe a prices listában, ahol a 3 terméket célszerű megvásárolni.
# A vásárlás összértéke.
# Feltételezheti, hogy "tej", "kenyér" és "tojás" minden boltban kapható és a prices lista mindig legalább 1 elemű. Ha egyszerre több boltban is a legolcsóbban jönnénk ki, akkor azt válasszuk, amelynek kisebb a prices listában az indexe.


def shopping(prices):
    best_shop_index = 0
    min_cost = float('inf')

    for i, shop in enumerate(prices):
        if "tej" and "tojás" and "kenyér" in shop:
            total_cost = shop["tej"] + shop["tojás"] + shop["kenyér"]

            if total_cost < min_cost or (total_cost == min_cost and i < best_shop_index):
                min_cost = total_cost
                best_shop_index = i

    return best_shop_index, min_cost