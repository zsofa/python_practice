# bemenet: két vektor
# ha az egyik bemenetben nincs meg a 3 koordináta akkor az adott koordinátában szereplő számok
# átlagának kell lennie a 3.nak
# kimenet: két vektor skaláris szorzata

def complete_vector(v):
    if len(v) == 3:
        return v
    else:
        avg = sum(v) / len(v)
        return v + [avg] * (3 - len(v))


def scalar_multiplication(v1, v2):
    vector1 = complete_vector(v1)
    vector2 = complete_vector(v2)

    return sum(x * y for x, y in zip(vector1, vector2))


print(scalar_multiplication([2, 3], [3, 4, 5]))
