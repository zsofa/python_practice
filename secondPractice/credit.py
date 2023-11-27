# Bemegy egy boltba és vásárol pár édességet.
# A csoki darabja 600 Ft, a gumicukor 400, a keksz 550, egy doboz sütemény 1200.
# 10.000 Ft van önnél. Mennyi pénze marad, ha még borravalót (tetszőleges) is ad?
# A megvásárolt mennyiségeket és a borravalót konzolról kérjük be!
# Ha túllépte az önnél lévő pénzmennyiséget, akkor hitelre vásárol.

max_money = 10000
chocolate_per_piece = 600
gummy_bear_per_piece = 400
cracker_per_piece = 550
biscuit_box = 1200
purchased_chocolate_piece = int(input("Insert the amount of chocolate: "))
purchased_gummy_bear_piece = int(input("Insert the amount of gummy bear: "))
purchased_cracker_piece = int(input("Insert the amount of cracker: "))
purchased_biscuit_box_piece = int(input("Insert the amount of biscuit box: "))
tip = int(input("Insert the amount of tip in Ft: "))

