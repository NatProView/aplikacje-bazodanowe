# Zad. 8 Stwórz sªownik, zawieraj¡cy cz¦stotliwo±ci wyst¡pie« liter w zadanym tek±cie.

my_text = "A quick brown fox jumps over the lazy dog aa bbb zz".lower()

alphabet = list("AĄBCĆDEĘFGHIJKLMNŃOÓPQRSŚTUVWXYZŻŹ".lower())

letter_count = {}
for letter in alphabet:
    letter_count[letter] = 0

for letter in my_text:
    if letter in alphabet:
        letter_count[letter] += 1

print(letter_count)