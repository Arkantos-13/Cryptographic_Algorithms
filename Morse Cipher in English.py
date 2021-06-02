"""

Import the necessary modules.

We use the module playsound so we can listen the Morse Code as we use telegraph.
Also, we use the module time in order to create the spaces between the letters for better understanding of the Morse Code

"""
from playsound import playsound
import time
import pyttsx3 as pyt

"""
The English alphabet, numbers and punctuation in Morse
"""
morse_dict = {

    # Uppercase letters

    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',

    # Numbers

    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----',

    # Punctuation

    ' ': '/', ', ': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', "_": "..--.-",
    "=": "-...-", "+": ".-.-.", "@": ".--.-.",
    ":": "---..."

}


def Txt_to_Morse():
    txt = input('Please type your Text to convert to Morse code:')
    letters = [morse_dict[i.upper()] + ' ' for i in txt if i.upper() in morse_dict.keys()]
    morse = ''.join(letters)
    print(morse)
    """
    This is the part of the code that can play your message in Morse Code
    However i can not upload any audio files on GitHub, because of privacy matters
     but if you Google it you will find the same files
    """
    for m in morse:
        if m == '.':
            playsound('dit.wav')
        elif m == '-':
            playsound('dah.wav')

        else:
             """
             0.5 seconds, is the time space between '.' and '-' when we hear the Morse Code
             """
             time.sleep(0.5)


def Morse_to_Txt():
    txt = input('Please type your Morse Code to convert back to Text:')
    letters = [k for i in txt.split() for k, v in morse_dict.items() if i == v]
    new_txt = ''.join(letters)
    print(new_txt)

    engine = pyt.init()
    engine.say(new_txt)
    engine.runAndWait()


print('''\n1 - Convert Text to Morse \n2 - Convert Morse to Text\n3 - Quit\n ''')

while True:
    try:
        choice_of_user = int(input('Type your Choice:'))

        if choice_of_user == 1:
            Txt_to_Morse()
            break
        elif choice_of_user == 2:
            Morse_to_Txt()
            break
        elif choice_of_user == 3:
            print('Exiting')
        else:
            print('Wrong Choice, Try again')
    except:
        print('Wrong Choice, Try again')
