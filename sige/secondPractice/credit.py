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
