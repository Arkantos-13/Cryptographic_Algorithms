"""
Here are  two alphabets, both English and Greek
"""

Alphabet = "ABCDEFGHIJKLMNOPQRSTUWXYZΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
AlphabetRVS = "ZYXWUTSRQPONMLKJIHGFEDCBAΩΨΧΦΥΤΣΡΠΟΞΝΜΛΚΙΘΗΖΕΔΓΒΑ"


'''
User's message
'''

message = input("Enter your message:").upper()


def encryption():

    encryption_text = ''

    '''
    Convert Alphabet to Alphabet reversed,space included.
    '''

    for i in range(len(message)):
        if message[i] == chr(32):
            encryption_text += " "
        else:
            for j in range(len(Alphabet)):
                if message[i] == Alphabet[j]:
                    encryption_text += AlphabetRVS[j]
                    break
    print("Encrypted message: {}".format(encryption_text))

def decryption():

    dencryption_text = ''

    '''
    Convert Alphabet reversed to Alphabet ,space included.
    '''

    for i in range(len(message)):
        if message[i] == chr(32):
            dencryption_text += " "
        else:
            for j in range(len(AlphabetRVS)):
                if message[i] == AlphabetRVS[j]:
                    dencryption_text += Alphabet[j]
                    break
    print("Decrypted message: {}".format(dencryption_text))


def main():

    '''
    User's choice for encryption or decryption.
    '''

    choice = int(input("Please enter:\n 1:for encryption\n 2:for decryption \n"))

    if choice == 1:
        print("---Encryption---")
        encryption()
    elif choice == 2:
        print("---Decryption---")
        decryption()
    else:
        print("Wrong choice. Try again!")





if __name__ == '__main__':
    main()


