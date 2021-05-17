msg = input('Type your text: ')

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

