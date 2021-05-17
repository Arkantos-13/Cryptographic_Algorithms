"""
msg = input('Type your text: ')
def rot47(msg):

    x = []
    for i in range(len(msg)):
        j = ord(msg[i])
        if j >= 33 and j <= 126:
            x.append(chr(33 + ((j + 14) % 94)))
        else:
            x.append(msg[i])
    print(''.join(x))

rot47(msg)"""


"""def text_to_binary(msg):
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

main(msg,ch)"""


"""def txt_to_ascii():
    message = input('Please type the text you would like to convert: ')

    convert_to_ascii = [ord(c) for c in message]

    print('Your new text in ASCII code is ready:', convert_to_ascii)


def ascii_to_txt():
    ## number of elements

    numbers_elements = int(input("Enter number of elements : "))

    # Below line read inputs from user using map() function

    elemnets = list(map(int, input("\nEnter the numbers : ").strip().split()))[:numbers_elements]

    convert_to_text = ''.join([chr(i) for i in elemnets])
    print(convert_to_text)


mode = int(input(

    'Press 1. If you want to convert your text in ASCII Code \n'
    'Press 2. If you want to convert your ASCII Code to a text \n'
))


def ASCII(mode):
    if mode == 1:
        txt_to_ascii()
    else:
        ascii_to_txt()


ASCII(mode)
"""