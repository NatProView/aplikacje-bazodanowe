def cipher(dictionary, to_cipher):
    end_string = ""
    for letter in to_cipher:
        if letter in alphabet:
            end_string += str(dictionary.get(letter))
        else:
            end_string += " "
    return end_string
    
to_cipher = "MĘŻNY BĄDŹ, CHROŃ PUŁK TWÓJ I SZEŚĆ FLAG"
print(to_cipher)
alphabet = list("AĄBCĆDEĘFGHIJKLMNŃOÓPQRSŚTUVWXYZŻŹ")
alphabet_moved = list("CĆDEĘFGHIJKLMNŃOÓPQRSŚTUVWXYZŻŹAĄB")
cipher_dict = dict(zip(alphabet, alphabet_moved))
print(cipher_dict)

ciphered = cipher(cipher_dict, to_cipher)
print(ciphered)

print(cipher(dict(zip(alphabet_moved, alphabet)), ciphered))


