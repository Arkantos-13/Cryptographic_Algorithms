"""
Convert a message to binary
"""


def text_to_binary(message):
    binary = ' '.join(format(ord(x), 'b') for x in message)
    print('Your converted message is the following: \n', binary)


"""
Convert a binary message back to a normal message
"""


def binary_to_text(message):
    new_message = ''.join([chr(int(s, 2)) for s in message.split()])
    print('Your converted binary code is the following: \n', new_message)


"""
We ask the user to type his choice.
One choice is to convert a message to binary or vice versa.
After that, we ask for his message
"""

choice_of_user = int(input('Please choose \n'
                           '1.To convert a text to a binary code: \n'
                           '2.To convert a binary code to a text: \n'
                           ))

message = input('Type the message you want to convert: ')


def Binary(message, choice_of_user):

    if choice_of_user == 1:
        text_to_binary(message)

    elif choice_of_user == 2:
        binary_to_text(message)

    else:
        print('Wrong choice! Please try again')


Binary(message, choice_of_user)
