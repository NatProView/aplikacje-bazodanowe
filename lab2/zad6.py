to_cipher = "MĘŻNY BĄDŹ, CHROŃ PUŁK TWÓJ I SZEŚĆ FLAG"
print(to_cipher)

alphabet = list("AĄBCĆDEĘFGHIJKLMNŃOÓPQRSŚTUVWXYZŻŹ")
alphabet_moved = list("CĆDEĘFGHIJKLMNŃOÓPQRSŚTUVWXYZŻŹAĄB")
cipher = dict(zip(alphabet, alphabet_moved))
print(cipher)

end_string = ""
for letter in to_cipher:
    if letter in alphabet:
        end_string += str(cipher.get(letter))
    else:
        end_string += " "

print(end_string)