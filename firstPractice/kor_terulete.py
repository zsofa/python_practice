# Egy kerek asztal átmérője másfél méter.
# Mekkora területet foglal el? A PI-t két tizedesjegyig adja meg (3.14)!

# 1. terület = átmérő a négyzetenh * PI / 4
d = 1.5
PI = 3.14
result1 = ((d ** 2) * PI) / 4

# 2. terület = sugár a négyzeten * PI
r = d/2
result2 = PI * (r ** 2)
print(result2)
