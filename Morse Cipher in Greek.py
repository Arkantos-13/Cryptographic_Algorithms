"""
Import the necessary modules.

We use the module playsound so we can listen the Morse Code as we use telegraph.
Also, we use the module time in order to create the spaces between the letters for better understanding of the Morse Code
"""

from playsound import playsound
import time

"""
This is the Morse Code for the Greek language 
"""

morse_dict = {

    # Uppercase letters - Κεφαλαία Γράμματα

    'Α': '.-', 'Β': '-...',
    'Γ': '--.', 'Δ': '-..', 'Ε': '.',
    'Ζ': '--..', 'Η': '....', 'Θ': '-.-.',
    'Ι': '..', 'Κ': '-.-', 'Λ': '.-..',
    'Μ': '--', 'Ν': '-.', 'Ξ': '-..-',
    'Ο': '---', 'Π': '.--.', 'Ρ': '.-.',
    'Σ': '...', 'Τ': '-', 'Υ': '-.--',
    'Φ': '..-.', 'Χ': '----', 'Ψ': '--.-',
    'Ω': '..-',

    # Numbers - Αριθμοί

    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----',

    # Punctuation - Σύμβολα

    ' ': '/', ', ': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', "_": "..--.-",
    "=": "-...-", "+": ".-.-.", "@": ".--.-.",
    ":": "---..."
}

"""
Convert the text in Morse Code
"""

def Txt_to_Morse():

    letters = [morse_dict[i.upper()] + ' ' for i in txt if i.upper() in morse_dict.keys()]
    morse = ''.join(letters)
    print('Here is your message in Morse Code: \n', morse)

    """
    Here it is how we can listen our message in Morse Code.
    In order to make it happen you need to download the wav files first
    """

    for m in morse:
        if m == '.':
            playsound('dit.wav')
        elif m == '-':
            playsound('dah.wav')
        else:
            time.sleep(0.5)

"""
Convert the Morse Code back to text
"""

def Morse_to_Txt():

    letters = [k for i in txt.split() for k, v in morse_dict.items() if i == v]
    new_txt = ''.join(letters)
    print('Here is your message from Morse Code back to normal: \n',new_txt)


print('''\n 1 - Convert Text to Morse \n 2 - Convert Morse to Text\n 3 - Quit\n ''')

while True:
    try:
        choice_of_user = int(input('Type your Choice:'))

        if choice_of_user == 1:
            txt = input('Please type your Text to convert to Morse Code: ')
            Txt_to_Morse()
            break
        elif choice_of_user == 2:
            txt = input('Please type your Morse Code to convert to Text: ')
            Morse_to_Txt()
            break
    except:
        print('Wrong Choice, Please try again')
