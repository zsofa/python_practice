# A közútkezelő megbízásából forgalomszámlálást végez az egyik forgalmas útszakaszon.
# Kérje be konzolon, hogy hány kamion haladt el az elmúlt órában! Azt is, hogy hány személyautó!
# Összesen hány egyéb jármű haladt át az útszakaszon, ha tudjuk, hogy abban az órában 250 jármű haladt át?
# Írassa ki a látott járműveket egy sorban, "/" jellel elválasztva, az elvárt kimenet szerint!

truck = int(input("Number of trucks: "))
car = int(input("Number of cars: "))
max_vehicle = 250
truck_car = truck + car
other = max_vehicle - truck_car

print(str(truck) + " kamion", str(car) + " szemelyauto ", str(other) + " egyeb jarmu", sep="/")
