# Írjon Python-programot, amely kiszámolja egy háromszög területét és kerületét.
# A háromszög oldalai: 15, 20 és 30 cm.

# Heron keplet, Zsofitol lopva

a = 15
b = 20
c = 30

perimeter = a + b + c
heron = perimeter / 2

area = (heron * ((heron - 15) * (heron - 20) * (heron - 30))) ** 0.5

print(area)
print(perimeter)
