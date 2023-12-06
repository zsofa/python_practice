# Készítsen programot, ami a felhasználótól bekéri egy kör sugarát, majd kiszámítja a kör kerületét és területét.
# A kimeneten először a kerület, majd sortöréssel elválasztva a terület eredménye jelenjen meg.
# A PI értékét 5 tizedesjegyig adja meg!

import math

pi = round(math.pi, 5)
r = int(input())

K = pi*2*r
T = r**2*pi

print(K)
print(T)
