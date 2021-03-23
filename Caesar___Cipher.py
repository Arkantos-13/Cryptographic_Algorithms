# Import the necessary module
import string

# This is the alphabet that we will use in order to conver the texts
alphabets = string.ascii_uppercase, string.ascii_lowercase, string.digits, string.punctuation

# Info of the User
plain_text = input('Please type your text that you want to Encrypt/Decrypt:')
shift = int(input('Please type your key number (0-25) so to encrypt/decrypt the message:'))


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

    choice_of_user = int(input('P1ease choose one of the following belong: \n Enter 1.' 
                               'For Encryption:\n Enter 2. For Decryption: \n '))

    if choice_of_user == 1:
        print('You chose the number', choice_of_user, 'so you just want to encrypt your message:')
        print('\n The encrypted message is: ', encrypt_caesar(plain_text, shift))
    elif choice_of_user == 2:
        print('\n You chose the number', choice_of_user, 'so you just want to decrypt your message:')
        print('\n The decrypted message is: ', decrypt_caesar(plain_text, shift))
    else:
        print('\n', 'Please type valid input')


Caesar()
