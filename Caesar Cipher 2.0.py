message = input("PLEASE TYPE YOUR MESSAGE BELOW:")
key = int(input("PLEASE TYPE THE NUMBER OF SHIFTS YOU WANT TO MAKE:"))
mode = int(input('''PLEASE CHOICE \n1. FOR ENCRYPTION:   \n2. FOR DECRYPTION:  \n '''))

def Encryption_Caesar(message, key):
    encrypted_message = ' '

    for letter in message:

        if letter.isupper():

            # check if it's an uppercase character
            letter_index = ord(letter) - ord('A')
            letter_shifted = (letter_index + key) % 26 + ord('A')

            letter_new = chr(letter_shifted)
            encrypted_message += letter_new

        elif letter.islower():

            # check if it's an lowercase character
            letter_index = ord(letter) - ord('a')
            letter_shifted = (letter_index + key) % 26 + ord('a')

            letter_new = chr(letter_shifted)
            encrypted_message += letter_new
        elif letter.isdigit():

            # Check if its a number
            # If its a number then it shift it the key value
            # For example if we have the number 3 and our key is 5 then the new number will be 8

            letter_new = (int(letter) + key) % 10
            encrypted_message += str(letter_new)

        else:

            # Check if its a punctuation
            # The total number of the punctuation are 32
            # If its a number then it shift it the key value
            # If you are confused check the ASCII table

            letter_index = ord(letter) - ord('!')
            letter_shifted = (letter_index + key) % 32 + ord('!')
            letter_new = chr(letter_shifted)
            encrypted_message += letter_new

    return encrypted_message


def Decryption_Caesar(message, key):
    decrypted_message = ' '

    for letter in message:

        if letter.isupper():

            # check if it's an uppercase character
            letter_index = ord(letter) - ord('A')
            letter_shifted = (letter_index - key) % 26 + ord('A')

            letter_new = chr(letter_shifted)
            decrypted_message += letter_new

        elif letter.islower():

            # check if it's an lowercase character
            letter_index = ord(letter) - ord('a')
            letter_shifted = (letter_index - key) % 26 + ord('a')

            letter_new = chr(letter_shifted)
            decrypted_message += letter_new
        elif letter.isdigit():

            # Check if its a number
            # If its a number then it shift it the key value
            # For example if we have the number 3 and our key is 5 then the new number will be 8

            letter_new = (int(letter) - key) % 10
            decrypted_message += str(letter_new)

        else:

            # Check if its a punctuation
            # The total number of the punctuation are 32
            # If its a number then it shift it the key value
            # If you are confussed check the ascii table

            letter_index = ord(letter) - ord('!')
            letter_shifted = (letter_index - key) % 32 + ord('!')
            letter_new = chr(letter_shifted)
            decrypted_message += letter_new

    return decrypted_message

def Caesar(message, key, mode):

    if mode == 1:
        print(f'Your encrypted message is the following below:', Encryption_Caesar(message,key))

    elif mode ==2:
        print(f'Your encrypted message is the following below:', Decryption_Caesar(message,key))
    else:
        print('Please type a right choice and run me again')


Caesar(message,key,mode)
