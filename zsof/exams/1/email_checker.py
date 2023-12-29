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

def check_english_chars(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeError:
        return False
    else:
        return s.isalpha()


def is_valid_username(username):
    if '.' in username:
        return False
    else:
        return check_english_chars(username)


def is_valid_domain(domain):
    if '.' not in domain:
        return False

    parts = domain.split('.')
    if len(parts) == 3:
        primary, primary_second_half, secondary = parts
        return check_english_chars(primary) and check_english_chars(primary_second_half) and check_english_chars(
            secondary)
    elif len(parts) == 2:
        primary, secondary = parts
        return check_english_chars(primary) and check_english_chars(secondary)
    else:
        return False


def email_checker(email):
    clean_email = email.strip()

    if '@' not in email:
        return False
    else:
        username, domain = clean_email.split('@', 1)
        return is_valid_username(username) and is_valid_domain(domain)


print(email_checker("info@gmailoj.com"))

