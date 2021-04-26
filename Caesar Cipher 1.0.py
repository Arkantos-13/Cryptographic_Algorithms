# Import the necessary module
import string

# This is the alphabet that we will use in order to convert the texts
alphabets = string.ascii_uppercase, string.ascii_lowercase, string.digits, string.punctuation
print(alphabets)

def encrypt_caesar(plain_text, shift):
    def shift_alphabet_encrypt(alphabets):
        return alphabets[shift:] + alphabets[:shift]

    shifted_alphabets = tuple(map(shift_alphabet_encrypt, alphabets))
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet = ''.join(shifted_alphabets)
    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    return plain_text.translate(table)


def decrypt_caesar(plain_text, shift):
    def shift_alphabet_encrypt(alphabets):
        return alphabets[-shift:] + alphabets[:-shift]

    shifted_alphabets = tuple(map(shift_alphabet_encrypt, alphabets))
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet = ''.join(shifted_alphabets)
    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    return plain_text.translate(table)


def Caesar():

    choice_of_user = int(input('P1ease choose one of the following belong: \n Enter 1. '  
                               'For Encryption:\n Enter 2. For Decryption: \n '
                               'Enter 3. For Brute Force Attack: \n '))


    if (choice_of_user ==1) | (choice_of_user ==2):

        # Info of the User
        plain_text = input('Please type your text that you want to Encrypt/Decrypt: \n')
        shift = int(input('Please type your key number (0-25) so to encrypt/decrypt the message: \n'))

        if choice_of_user == 1:
            print('You chose the number', choice_of_user, 'so you just want to encrypt your message:')
            print('The encrypted message is: ', encrypt_caesar(plain_text, shift))

        elif choice_of_user == 2:
            print('You chose the number', choice_of_user, 'so you just want to decrypt your message:')
            print('The decrypted message is: ', decrypt_caesar(plain_text, shift))

    elif choice_of_user == 3:
        # BRUTE FORCE ATTACK
        message_to_break = input('Type your message you want to apply Brute Force Attack: ')
        print('Your original message is somewhere below: \n')

        for i in range(26):
            print(' shift{:2} : {}'.format(i, decrypt_caesar(message_to_break, shift=i)))

    else:
        print('\n', 'Please type valid input')


Caesar()
