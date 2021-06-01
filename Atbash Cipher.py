"""
Here are the two alphabets, both in English and Greek
"""

Alphabet = "ABCDEFGHIJKLMNOPQRSTUWXYZΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
AlphabetRVS = "ZYXWUTSRQPONMLKJIHGFEDCBAΩΨΧΦΥΤΣΡΠΟΞΝΜΛΚΙΘΗΖΕΔΓΒΑ"


'''
User's message
'''

message = input("enter message:").upper()


def encryption():

    encry_text = ''

    '''
    Convert Alphabet to Alphabet reversed,space included.
    '''

    for i in range(len(message)):
        if message[i] == chr(32):
            encry_text += " "
        else:
            for j in range(len(Alphabet)):
                if message[i] == Alphabet[j]:
                    encry_text += AlphabetRVS[j]
                    break
    print("Encrypted message: {}".format(encry_text))

def decryption():

    dencry_text = ''

    '''
    Convert Alphabet reversed to Alphabet ,space included.
    '''

    for i in range(len(message)):
        if message[i] == chr(32):
            dencry_text += " "
        else:
            for j in range(len(AlphabetRVS)):
                if message[i] == AlphabetRVS[j]:
                    dencry_text += Alphabet[j]
                    break
    print("Decrypted message: {}".format(dencry_text))





def main():

    '''
    User's choice for encryption or decryption.
    '''

    choise = int(input("Please enter:\n1:for encryption\n2:for devryption "))

    if choise == 1:
        print("Encryption")
        encryption()
    elif choise == 2:
        print("Decryption")
        decryption()
    else:
        print("Wrong choice. Try again!")





if __name__ == '__main__':
    main()


