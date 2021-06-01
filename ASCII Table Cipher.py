"""
Convert a normal text to an ASCII code
"""


def txt_to_ascii():

    # We ask the user for his input text
    text = input('Please type your text here: \n')

    # Here we change each letter, number or punctuation to an ASCII code
    convert_to_ascii = [ord(c) for c in text]

    print('Your new text in ASCII code is this: \n', convert_to_ascii)


"""
Convert an ASCII code text, back to normal text with lowercase and uppercase letters
"""


def ascii_to_txt():

    # Here we read the ASCII code, using the map() function
    # Be careful, you should erase the bracket and the commas when you type the ascii code
    elemnets = list(map(int, input("Enter the numbers of the ASCII code in order to convert them: ").strip().split()))[:1000]

    # We join each letter back together and create the original text
    convert_to_text = ''.join(chr(i) for i in elemnets)
    print(convert_to_text)


"""
We give the user only two options in this cipher
"""


def ASCII():

    mode = int(input(

        'Press 1. If you want to convert your text into ASCII code: \n'
        'Press 2. If you want to convert your ASCII code to a text: \n'
    ))

    if mode == 1:
        txt_to_ascii()
    else:
        ascii_to_txt()


ASCII()
