# Írjon Python-programot, amely kiszámolja egy háromszög területét és kerületét.
# A háromszög oldalai: 15, 20 és 30 cm.

# Héron képlet

perimeter = 15 + 20 + 30
print(perimeter)
s = perimeter / 2

helper = s * ((s - 15) * (s - 20) * (s - 30))
area = helper ** (1/2)
print(area)
