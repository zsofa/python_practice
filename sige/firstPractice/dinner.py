# Az étteremben Julcsi hamburgert, a húga négy hot-dogot, az anyukája salátát, az apukája rántott húst vacsorázik.
# Az apukának nagyon ízlik a rántott hús, rendel még egy adagot.
# A hamburger ára 4000 Ft, a hot-dogé 1500 Ft. A saláta 7000 Ft-ba kerül, a rántott hús 13000-be.
# Számítsa ki, mennyit fizetnek összesen, ha 10% felszolgálói díj is van, és az egyik hot-dogot ajándékba kapják!
# Az eredményt egész számként írassa ki!

julcsi = 4000
sister = 3 * 1500
mother = 7000
father = 13000 * 2

sum = julcsi + sister + mother + father

sum += sum * 0.1

print(int(sum))
