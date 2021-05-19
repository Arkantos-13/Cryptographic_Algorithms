"""
Import the modules we will use in this cipher
"""


import string
import secrets

# Get the secret message from the user, in order to convert it
plaintext = input('Please type your secret message: ')


"""
Here we only need as input the plaintext
because we create the key in the def in order to be unique each time
"""


def Vernam_Encryption(plaintext):

    # Create a secret key each time with the same length of the message
    key_encryption = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation)
                             for k in range(len(plaintext)))

    print('This is the secret key i used to convert your message: ', key_encryption)

    encrypted_message = ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(plaintext,key_encryption))

    print('This is the encrypted message: ', encrypted_message)

    
"""
In order to decrypt the message we must have both the encrypted message and the key that it was encrypted
"""


def Vernam_Decryption(plaintext,key):

    decrypted_message = ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(plaintext,key))

    print('This is the decrypted message: ',decrypted_message)


def Vernam_Cipher(plaintext):

    choice_user = int(input('Please type 1. For Encryption or 2. For Decryption '))

    if choice_user == 1:
        Vernam_Encryption(plaintext)

    elif choice_user == 2:
        key = input('Please type the secret key you have: ')
        Vernam_Decryption(plaintext,key)

    else:
        print('Try again')


Vernam_Cipher(plaintext)

