# Valósítsa meg az email_checker(email) függvény, ahol email egy bemeneti str, amelyről el kell dönteni, hogy helyes email címet tartalmaz vagy sem. Ennek tényét logikai értékként adja vissza a függvény.
#
# Egy email felépítése legyen a következő: {felhasználónév}@{másodlagos domain}.{elsődleges domain}
#
# A valóságtól némileg egyszerűsítve egy email címet most tekintsünk akkor helyesnek, ha:
#
# A felhasználónév (@ karakter előtti szakasz) csak az angol ábécé betűit tartalmazza.
# A domain (@ karakter utáni szakasz) két részből áll: elsődleges domain és másodlagos domain. A másodlagos domain a @ karakter után az első pontig tartó szakasz legyen. Ugyanezen pont utáni szakasz pedig az elsődleges domain.
# Az elsődleges domain az angol ábécé karaktereit és maximum egy darab pontot tartalmazhat.
# A másodlagos domain csak az angol ábécé karaktereit tartalmazhatja.
# Elfordulhat, hogy az email cím előtt vagy után fehér karakterek találhatóak, ezeket vegye figyelmen kívül.

def email_checker(email):
    email = email.strip()
    if "@" not in email:
        return False
    if "." not in email:
        return False

    splitted = email.split("@")
    if len(splitted) > 2:
        return False

    username = splitted[0]

    if not username.isalpha():
        return False

    domain = splitted[1]
    splitted = domain.split(".")
    if len(splitted) > 3:
        return False

    first_domain = splitted[0]
    second_domain = splitted[1]

    if not first_domain.isalpha():
        return False

    return second_domain.isalpha()


print(email_checker("info@em@il.com"))

