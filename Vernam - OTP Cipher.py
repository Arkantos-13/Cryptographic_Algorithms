"""
Import the necessary modules that we are going to use later
We need the module string in order to create the secret key and the module secrets
because we want the choice of the encrypted letters and digits to be encrypted.
Other methods as random.choice choices are not encrypted and it's quite easy to find out the key because they are based
on mathematical equations.
"""
import string
import secrets


"""
Get the secret message from the user, in order to convert it
"""

text = input('Please type your secret message here: ')


"""
Here we only need as input the plaintext
because we create the key inside the def Vernam_Encryption in order to be unique each time and encrypted
"""


def Vernam_Encryption(text):
    
    """
    One Time Password - OTP
    Create a secret key, each time with the same length of the message
    """
    key_encryption = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation)
                             for _ in range(len(text)))

    print('This is the secret key i used to convert your message: ', key_encryption)
    """
    Now we make XOR '^' the letters of the original text and the letters of out secret key
    """
    encrypted_message = ''.join([chr(ord(a) ^ ord(b)) for a,b in zip(text,key_encryption)])

    print('This is the encrypted message: ', encrypted_message)


"""
In order to decrypt the message we must have both the encrypted message and the key that it was encrypted
"""


def Vernam_Decryption(text,key):

    decrypted_message = ''.join([chr(ord(a) ^ ord(b)) for a,b in zip(text,key)])

    print('This is the decrypted message: ',decrypted_message)


def Vernam_Cipher(text):

    choice_user = int(input('Please type: \n'
                            '1. For Encryption or 2. For Decryption '))

    if choice_user == 1:
        Vernam_Encryption(text)
    elif choice_user == 2:
        """
        If the user wants to decrypt a message, he must have the secret key in order to achieve it
        That's why we ask it now and we don't create it
        """
        key = input('Please type the secret key you have: ')
        Vernam_Decryption(text,key)
    else:
        print('Try again :) ')


Vernam_Cipher(text)

