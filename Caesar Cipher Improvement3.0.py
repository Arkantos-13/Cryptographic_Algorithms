"""
Another way to create an evolution of the Caesar Cipher
"""

"""
The information that a user have to type each time
"""

mode = int(input('Enter 1. For Encryption: \n'
                 'Enter 2. For Decryption: \n'
                 ))

message = input("Please type your message here: \n")
key = int(input("Please type the number of shifts you would like to make : \n"))

def Encryption_Caesar(message, key):
    encrypted_message = ' '

    for letter in message:
        # Here we check if a letter is uppercase and then we transport it
        if letter.isupper():

            letter_index = ord(letter) - ord('A')
            letter_shifted = (letter_index + key) % 26 + ord('A')

            letter_new = chr(letter_shifted)
            encrypted_message += letter_new

        # Here we check if a letter is lowercase
        elif letter.islower():

            # check if it's an lowercase character and then we transport it
            letter_index = ord(letter) - ord('a')
            letter_shifted = (letter_index + key) % 26 + ord('a')

            letter_new = chr(letter_shifted)
            encrypted_message += letter_new

        # Here we check if we have a digit and then we transport it
        elif letter.isdigit():

            """
            If it's a number then we shift it the key value
            For example if we have the number 3 and our key is 5 then the new number will be 8
            """

            letter_new = (int(letter) + key) % 10
            encrypted_message += str(letter_new)

        elif letter.isspace():

            encrypted_message += ' '

        # Here we check if we have a punctuation and then we transport it
        else:

            """"
            The total number of the punctuation are 32
            It shifts the punctuation key values according to ASCII table
            If you are confused check the ASCII table
            """

            letter_index = ord(letter) - ord('!')
            letter_shifted = (letter_index + key) % 32 + ord('!')
            letter_new = chr(letter_shifted)
            encrypted_message += letter_new

    return encrypted_message


def Decryption_Caesar(message, key):
    decrypted_message = ' '

    for letter in message:

        if letter.isupper():

            # check if it's an uppercase character and then we transport it
            letter_index = ord(letter) - ord('A')
            letter_shifted = (letter_index - key) % 26 + ord('A')

            letter_new = chr(letter_shifted)
            decrypted_message += letter_new

        elif letter.islower():

            # check if it's an lowercase character and then we transport it
            letter_index = ord(letter) - ord('a')
            letter_shifted = (letter_index - key) % 26 + ord('a')

            letter_new = chr(letter_shifted)
            decrypted_message += letter_new

        elif letter.isdigit():

            """
            Check if it's a number
            If it's a number then it shift it the key value
            For example if we have the number 3 and our key is 5 then the new number will be 8
            """

            letter_new = (int(letter) - key) % 10
            decrypted_message += str(letter_new)

        elif letter.isspace():

            decrypted_message += ' '

        else:

            """
            Check if it's a punctuation
            The total number of the punctuation are 32
            If it's a number then it shift it the key value
            If you are confused check the ascii table
            """

            letter_index = ord(letter) - ord('!')
            letter_shifted = (letter_index - key) % 32 + ord('!')
            letter_new = chr(letter_shifted)
            decrypted_message += letter_new

    return decrypted_message

def Caesar(message, key, mode):

    if mode == 1:
        print('Your encrypted message is the following below:', Encryption_Caesar(message,key))

    elif mode ==2:
        print('Your encrypted message is the following below:', Decryption_Caesar(message,key))
    else:
        print('Please type a right choice and run me again')


Caesar(message,key,mode)
