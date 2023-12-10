# A közútkezelő megbízásából forgalomszámlálást végez az egyik forgalmas útszakaszon.
# Kérje be konzolon, hogy hány kamion haladt el az elmúlt órában! Azt is, hogy hány személyautó!
# Összesen hány egyéb jármű haladt át az útszakaszon, ha tudjuk, hogy abban az órában 250 jármű haladt át?
# Írassa ki a látott járműveket egy sorban, "/" jellel elválasztva, az elvárt kimenet szerint!

kamion = int(input())
auto = int(input())

print(f'{kamion} kamion/{auto} szemelyauto/{250-kamion-auto} egyeb jarmu')
