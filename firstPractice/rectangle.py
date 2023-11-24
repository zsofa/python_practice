# Írjon Python-programot, amely kiszámolja egy háromszög területét és kerületét.
# A háromszög oldalai: 15, 20 és 30 cm.

# Héron képlet

kerulet = 15 + 20 + 30
print(kerulet)
s = kerulet / 2

helper = s * ((s - 15) * (s - 20) * (s - 30))
terulet = helper ** (1/2)
print(terulet)
