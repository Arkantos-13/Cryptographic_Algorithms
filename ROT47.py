"""
The Rot-47 is a shift cipher that improves the Rot-13 by allowing it to encode almost all visible ASCII characters (where Rot13 could only encode letters).

To achieve this, Rot47 uses a 94-character alphabet that is a subset of the ASCII table characters between the character 33 ! and the character 126 ~. 

Rot47 encryption consists in replacing a character with another located 47 positions after in the alphabet. The conversion table is:
!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
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

