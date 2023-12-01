# Készítsen programot, ami a felhasználótól bekéri egy kör sugarát, majd kiszámítja a kör kerületét és területét.
# A kimeneten először a kerület, majd sortöréssel elválasztva a terület eredménye jelenjen meg.
# A PI értékét 5 tizedesjegyig adja meg!
import math

radius = int(input())

# Limit the float value to 5 decimal points
pi = round(math.pi, 5)
perimeter = 2 * pi * radius
area = (radius ** 2) * pi
print(perimeter, area, sep='\n')