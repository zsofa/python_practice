# Írjunk programot, ami bekér egy mondatot a felhasználótól,
# majd kiírja ugyanazt a mondatot úgy, hogy minden szó kezdőbetűje nagybetű legyen!

text = str(input())
words = text.split()
capitalized_words = [word.capitalize() for word in words]
result = ' '.join(capitalized_words)
print(result)
