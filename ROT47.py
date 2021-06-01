"""

What is Rot-47? (Definition):

The Rot-47 is a shift cipher that improves the Rot-13 by allowing it to encode almost all visible ASCII characters (where Rot13 could only encode letters).
To achieve this, Rot47 uses a 94-character alphabet that is a subset of the ASCII table characters between the character 33 ! and the character 126 ~.

How to encrypt using Rot-47?

Rot47 encryption consists in replacing a character with another located 47 positions after in the alphabet. The conversion table is:
!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~

Example: DCODE is encrypted sr~st with ROT-47

How to decrypt Rot-47 cipher?

The decryption of the Rot-47 is identical to the encryption because the substitution alphabet used is reversible.
PQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNO

Example: #@E\cf is decoded Rot-47

Why the shift of 47?

The ASCII code defines 94 printable characters, so a rotation of half (94/2 = 47) makes it possible to obtain a symmetric cipher,
similar to ROT13 (for the 26 letters of the alphabet).

How to recognize ROT-47 ciphertext?

The message uses ASCII characters. It contains common letters as 6 or t which are the ciphered values of E and e.
Rot47 is a simple way to encode a message on discussion forums or social networks.

What are the variants of the Rot-47 cipher?

Rot-47 is a variant of Rot13, itself a variant of the Caesar cipher, a special case of shift cipher.

"""

msg = input('Type your text here: ')

def rot47(msg):

    x = []
    for i in range(len(msg)):
        j = ord(msg[i])
        if j >= 33 and j <= 126:
            x.append(chr(33 + ((j + 14) % 94)))
        else:
            x.append(msg[i])
   return ''.join(x)


print('Here\'s is your final message:' , rot47(msg)) 

