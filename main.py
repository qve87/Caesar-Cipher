"""
Caesar Cipher - simple application to encrypt and decrypt word by shifting each letter by n position
"""

from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)


def encrypt(sentence, shift_number):
    """
    Function encrypts single word.
    :param sentence: users word to encrypt
    :param shift_number: shifting position
    :return: encrypted word
    """
    encrypted_word = ""
    for char in sentence:
        index_number = alphabet.index(char)
        position = (index_number + shift_number) % 26
        encrypted_word += alphabet[position]

    return encrypted_word


def decrypt(encrypted_word, shift_number):
    """
    Function encrypts single word.
    :param encrypted_word: encrypted word
    :param shift_number: shifting number
    :return: decrypted word
    """
    decrypted_word = ""
    for char in encrypted_word:
        index_number = alphabet.index(char)
        decrypted_word += alphabet[(index_number - shift_number) % 26]

    return decrypted_word


game_on = True

while game_on:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if direction != "encode" and direction != "decode":
        print("Type correct word\n")
        continue

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        print(encrypt(text, shift))
    else:
        print(decrypt(text, shift))

    while True:

        try_again = input("Do you want to try again? y/n: \n").lower()

        if try_again not in "yn":
            print("Please type the correct letter. (y/n)\n")

        elif try_again == "n":
            print("Thanks for playing\n")
            game_on = False
            break
        else:
            break


