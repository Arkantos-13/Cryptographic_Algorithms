"""
Here is the greek alphabet.
The code should work for every language if you change the alphabet
"""
alphabets = 'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ'

"""
First we will make the encryption version of the cipher
"""
def encryption(plain_text,shift):
    shifted_alphabet = alphabets[shift:] + alphabets[:shift]
    cipher_text = " "

    for letter in range(len(plain_text)):
        char = plain_text[letter]
        position = alphabets.find(char.upper())

        # It creates the spaces between the words in the plaintext
        if position == -1:
            cipher_text += char
        else:
            cipher_text += shifted_alphabet[position]

    return cipher_text

"""
Now, we will make the decryption version of our cipher
"""
def decryption(plain_text, shift):
    shifted_alphabet = alphabets[-shift:] + alphabets[:-shift]
    cipher_text = " "

    for letter in range(len(plain_text)):

        char = plain_text[letter]
        position = alphabets.find(char.upper())

        # It creates the spaces between the words in the plaintext
        if position == -1:
            cipher_text += char
        else:
            cipher_text += shifted_alphabet[position]

    return cipher_text


def Caesar():

    choice_of_user = int(input('P1ease choose one of the following belong: \n Enter 1. '  
                               'For Encryption:\n Enter 2. For Decryption: \n '
                               'Enter 3. For Brute Force Attack: \n '))

    if (choice_of_user == 1) | (choice_of_user == 2):

        # Info of the User
        plain_text = input('Please type your text that you want to Encrypt/Decrypt: \n')
        shift = int(input('Please type your key number (0-25) so to encrypt/decrypt the message: \n'))

        if choice_of_user == 1:
            print('You chose the number', choice_of_user, 'so you just want to encrypt your message:')
            print('The encrypted message is: ', encryption(plain_text, shift))

        elif choice_of_user == 2:
            print('You chose the number', choice_of_user, 'so you just want to decrypt your message:')
            print('The decrypted message is: ', decryption(plain_text, shift))

    elif choice_of_user == 3:

        # BRUTE FORCE ATTACK
        message_to_break = input('Type your message you want to apply Brute Force Attack: ')
        print('Your original message is somewhere below: \n')

        for i in range(26):
            print(' shift{:2} : {}'.format(i, decryption(message_to_break, shift=i)))

    else:
        print('\n', 'Please type valid input')


Caesar()

