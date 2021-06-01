"""
This code works as the original Caesar Cipher and use only the uppercase letters.
In other words it changes only the letters of a text and anything else.
If you want to change the numbers and the punctuations of a plain text
you can view my other Caesar Ciphers that i have uploaded.

Here is the greek alphabet.
The code should work for every language if you change the alphabet.
"""

alphabets = 'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ'

"""
Here you can view the Encryption algorithm of the Caesar Cipher
"""

def encryption(plain_text,shift):

    # Here we create the new shifted alphabet that we will use
    shifted_alphabet = alphabets[shift:] + alphabets[:shift]
    cipher_text = " "

    for letter in range(len(plain_text)):
        char = plain_text[letter]
        position = alphabets.find(char.upper())

        # It creates the spaces between the words from the plaintext
        if position == -1:
            cipher_text += char

        # It changes the letters from the new shifted_alphabet
        else:
            cipher_text += shifted_alphabet[position]

    return cipher_text

"""
Here you can view the Decryption algorithm of the Caesar Cipher
"""

def decryption(plain_text, shift):

    # Here we create the new shifted alphabet that we will use
    shifted_alphabet = alphabets[-shift:] + alphabets[:-shift]
    cipher_text = " "

    for letter in range(len(plain_text)):

        char = plain_text[letter]
        position = alphabets.find(char.upper())

        # It creates the spaces between the words from the plaintext
        if position == -1:
            cipher_text += char

        # It changes the letter from the new shifted_alphabet
        else:
            cipher_text += shifted_alphabet[position]

    return cipher_text

"""
The final code
"""

def Caesar():
    # The choices that we give to the user
    choice_of_user = int(input('Please choose one of the following belongs: \n '
                               'Enter 1. For Encryption:\n '
                               'Enter 2. For Decryption: \n '
                               'Enter 3. For Brute Force Attack: \n '))

    if (choice_of_user == 1) | (choice_of_user == 2):

        # Information that the user have to type each time
        plain_text = input('Please type your text that you want to Encrypt/Decrypt: \n')
        shift = int(input('Please type your key number (0-23) so to encrypt/decrypt the message: \n'))

        if choice_of_user == 1:
            print('You chose the number', choice_of_user, 'so you just want to encrypt your message:'
                  'The encrypted message is: ', encryption(plain_text, shift))

        else:
            print('You chose the number', choice_of_user, 'so you just want to decrypt your message:'
                  'The decrypted message is: ', decryption(plain_text, shift))

    elif choice_of_user == 3:

        """
        BRUTE FORCE ATTACK ON THE CIPHER
        
        You can break any encrypted message without knowing the secret key
        """
        message_to_break = input('Type your message you want to apply Brute Force Attack: ')
        print('Your original message is somewhere below: \n')

        """
        In other words here we try all the possible combination and print it out
        The range depends from the length of the alphabet
        """

        for i in range(24):
            print(' shift{:2} : {}'.format(i, decryption(message_to_break, shift=i)))

    else:
        print('Please type a valid input and try again')


Caesar()

