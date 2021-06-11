"""

The original Caesar cipher only changes the letters of a text and not the symbols or the punctuation.

In the code below, we shift the alphabet 13 positions to the right because we want to create the Rot13,
then we create a new alphabet the 'shifted_alphabet'.

If we have space which is the first 'if' statement we don't change it all.
If we have a lower case letter we change it with the new lower letter.
Some on the final else statement, but this time it works for the upper case letter.

"""

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

key = 13
message = input('Type your message:')
choice = int(input('Type 1. For Encryption or 2. For Decryption:'))


def ROT13_encryption(message):
    shifted_alphabet = alphabet[key:] + alphabet[:key]
    cipher_text = " "

    for letter in range(len(message)):
        char = message[letter]
        position = alphabet.find(char.upper())

        if position == -1:
            cipher_text += char
        elif char.islower():
            cipher_text += shifted_alphabet[position].lower()
        else:
            cipher_text += shifted_alphabet[position]

    return cipher_text


def ROT13_decryption(message):
    shifted_alphabet = alphabet[-key:] + alphabet[:-key]
    cipher_text = " "

    for letter in range(len(message)):
        char = message[letter]
        position = alphabet.find(char.upper())

        if position == -1:
            cipher_text += char
        elif char.islower():
            cipher_text += shifted_alphabet[position].lower()
        else:
            cipher_text += shifted_alphabet[position]

    return cipher_text


def rot13(message ,choice):

    if choice == 1:
        print('-------Encryption------')
        print(ROT13_encryption(message))
    elif choice == 2:
        print('-------Decryption-------')
        print(ROT13_decryption(message))
    else:
        print('Type your choice right this time')


rot13(message,choice)
