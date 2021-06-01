"""
Implementation of the classic Caesar cipher
It only transports uppercase and lowercase letters
"""

# Import the necessary module in order to create our new alphabet
import string

# This is the new alphabet that we will use in order to convert any text
alphabets = string.ascii_uppercase, string.ascii_lowercase




def encrypt_caesar(plain_text, shift):
    def shift_alphabet_encrypt(alphabet):
        return alphabet[shift:] + alphabet[:shift]

    shifted_alphabets = tuple(map(shift_alphabet_encrypt, alphabets))
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet = ''.join(shifted_alphabets)
    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    return plain_text.translate(table)


def decrypt_caesar(plain_text, shift):
    def shift_alphabet_encrypt(alphabet):
        return alphabet[-shift:] + alphabet[:-shift]

    shifted_alphabets = tuple(map(shift_alphabet_encrypt, alphabets))
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet = ''.join(shifted_alphabets)
    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    return plain_text.translate(table)


def Caesar():

    """
    The information of the each have to type each time
    """

    choice_of_user = int(input('Please choose one of the following belong: \n'
                               'Enter 1. For Encryption: \n' 
                               'Enter 2. For Decryption: \n'))

    plain_text = input('Please type your text that you want to Encrypt/Decrypt:')

    shift = int(input('Please type your key number (0-25) so to encrypt/decrypt the message:'))

    if choice_of_user == 1:
        print('You chose the number', choice_of_user, 'so you just want to encrypt your message:'
              'The encrypted message is:', encrypt_caesar(plain_text, shift))
    elif choice_of_user == 2:
        print('You chose the number', choice_of_user, 'so you just want to decrypt your message:'
              'The decrypted message is: ', decrypt_caesar(plain_text, shift))
    else:
        print('Please type a valid input and try again')


Caesar()
