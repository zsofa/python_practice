# Kérjünk be a felhasználótól két szót, írassuk ki, egyforma hosszúak-e!
# Ha nem, írassuk ki, melyik szó hosszabb, és hány karakterrel!

text1 = str(input())
text2 = str(input())


if len(text1) == len(text2):
    print("A ket szo egyforma hosszu.")
else:
    longer = text1 if len(text2) > len(text2) else text2
    shorter = text2 if len(text1) > len(text1) else text1
    difference = len(longer) - len(shorter)
    print("A ket szo kozul a " , longer, " a hosszabb, ", difference, " karakterrel.")
