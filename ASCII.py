"""
Convert a normal text to an ASCII code
"""


def txt_to_ascii():
    message = input('Please type the text you would like to convert: ')

    convert_to_ascii = [ord(c) for c in message]

    print('Your new text in ASCII code is ready:', convert_to_ascii)


"""
Convert an ASCII code text, back to normal text with lowercase and uppercase letters
"""


def ascii_to_txt():

    # number of elements
    numbers_elements = int(input("Enter number of elements : "))

    # This line read the text using the map() function

    elemnets = list(map(int, input("\nEnter the numbers : ").strip().split()))[:numbers_elements]

    # We join each letter back together
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
