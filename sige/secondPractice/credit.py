# Bemegy egy boltba és vásárol pár édességet.
# A csoki darabja 600 Ft, a gumicukor 400, a keksz 550, egy doboz sütemény 1200.
# 10.000 Ft van önnél. Mennyi pénze marad, ha még borravalót (tetszőleges) is ad?
# A megvásárolt mennyiségeket és a borravalót konzolról kérjük be!
# Ha túllépte az önnél lévő pénzmennyiséget, akkor hitelre vásárol.

csoki = int(input('Hany csokit vasarol? '))
cukor = int(input('Hany gumicukrot vasarol? '))
keksz = int(input('Hany kekszet vasarol? '))
suti = int(input('Hany doboz sutemenyt vasarol? '))
borravalo = int(input('Mennyi borravalot ad? '))

money = 10000

result = (money -
          (csoki * 600 + cukor * 400 + keksz * 550 + suti * 1200 + borravalo))

if result < 0:
    print(f'Hitelre vasarolt: {abs(result)} Ft ertekben')
else:
    print(f'Megmarad: {result} Ft')
