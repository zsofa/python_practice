# Készítsen programot, ami a felhasználótól bekéri egy téglalap két oldalhosszát,
# majd kiszámítja a téglalap kerületét és területét. A kimeneten először a kerület,
# majd sortöréssel elválasztva a terület eredménye jelenjen meg.
# Tájékoztató üzenetekkel nem kell ellátni a programot.

side1 = float(input())
side2 = float(input())

print(2*(side1 + side2), side1*side2, sep="\n")