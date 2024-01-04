def terulet_szamolas(pontok):
    x1, y1 = pontok[0]
    x2, y2 = pontok[1]
    x3, y3 = pontok[2]

    terulet = 0.5 * abs(x1*y2 + x2*y3 + x3*y1 - x1*y3 - x2*y1 - x3*y2)
    return terulet

# A poligon sarkpontjainak koordinátái
sarkpontok = [(0, 0), (1, 0), (0, 1)]

# Terület kiszámolása
poligon_terulet = terulet_szamolas(sarkpontok)

print(f"A poligon területe: {poligon_terulet}")