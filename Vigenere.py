def Encryption_Vigenre(message, key):
    key_int = [ord(i) for i in key]
    message_int = [ord(i) for i in message]
    encrypted_message = ''

    for i in range(len(message_int)):
        letters = key_int[i % len(key)]
        encrypted_letters = (message_int[i] - 32 + letters) % 95
        encrypted_message += chr(encrypted_letters + 32)
    return encrypted_message


def Decryption_Vigenere(message, key):
    key_int = [ord(i) for i in key]
    message_int = [ord(i) for i in message]
    decrypted_message = ''

    for i in range(len(message_int)):
        letters = key_int[i % len(key)]
        decrypted_letters = (message_int[i] - 32 - letters) % 95
        decrypted_message += chr(decrypted_letters + 32)
    return decrypted_message


message = input('Please type your text:')
key = input('Please type your key word:')
choice_of_user = int(
    input('P1ease choose one of the following belong: \n Enter 1.For Encryption:\n Enter 2. For Decryption: \n '))


def Vigenere_Cipher(choice_of_user, message, key):
    if choice_of_user == 1:
        print('You chose the number', choice_of_user, 'so you just want to encrypt your message:')
        print('\n The encrypted message is: ', Encryption_Vigenre(message, key))
    elif choice_of_user == 2:
        print('\n You chose the number', choice_of_user, 'so you just want to decrypt your message:')
        print('\n The decrypted message is: ', Decryption_Vigenere(message, key))
    else:
        print('\n', 'Please type valid input')


Vigenere_Cipher(choice_of_user, message, key)