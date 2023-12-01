# Az étteremben Julcsi hamburgert, a húga négy hot-dogot, az anyukája salátát, az apukája rántott húst vacsorázik.
# Az apukának nagyon ízlik a rántott hús, rendel még egy adagot.
# A hamburger ára 4000 Ft, a hot-dogé 1500 Ft. A saláta 7000 Ft-ba kerül, a rántott hús 13000-be.
# Számítsa ki, mennyit fizetnek összesen, ha 10% felszolgálói díj is van, és az egyik hot-dogot ajándékba kapják!
# Az eredményt egész számként írassa ki!

hamburger = 4000
hot_dog = 1500 * 3
salad = 7000
meat = 13000 * 2

price = hamburger + hot_dog + salad + meat
result = price + (price * 0.1)
print(int(result))

