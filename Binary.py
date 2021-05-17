def text_to_binary(msg):
    binary = ' '.join(format(ord(x), 'b') for x in msg )
    print(binary)


def binary_to_text(msg):
    text = ''.join([chr(int(s, 2)) for s in msg.split()])
    print(text)

msg = input('Type the message you want to convert: ')
ch = int(input('Please choose \n'
               '1. To convert a text to a binary code: \n' 
               '2. To convert a binary code to a text: \n'
               ))


def main(msg, ch):
    if ch == 1:
        text_to_binary(msg)
    elif ch == 2:
        binary_to_text(msg)
    else:
        print('Wrong choice!')


main(msg,ch)