def txt_to_ascii():
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
