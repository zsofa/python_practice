# Egy hangya a saját súlyának 5000-szeresét bírja el. A hangya súlya 0,002 g.
# Hány hangyára van szükség egy doboz kóla megmozdításához, ha annak súlya 400 gramm?

import math

antForce = 0.002 * 5000
coke = 400

print(math.ceil(coke / antForce))
