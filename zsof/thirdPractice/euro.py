# Kérjük be a konzolról az aktuális Forint - Euró árfolyamot!
# Ennek alapján készítsünk átváltási táblázatot, ami 1-től 200-ig, 25-ös lépésközzel kiírja a megfelelő Euró és Forint értékeket!

current_euro_huf_rate = int(input())
x = 25
print('Ft', 'Euro', sep='\t')
print(1, 1 * current_euro_huf_rate, sep='\t')
while x <= 200:
    print(x, x * current_euro_huf_rate, sep='\t')
    x = x + 25




