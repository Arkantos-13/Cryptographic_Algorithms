from playsound import playsound
import time


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


def Txt_to_Morse():
    txt = input('Please type your Text to convert to Morse code: ')
    letters = [morse_dict[i.upper()] + ' ' for i in txt if i.upper() in morse_dict.keys()]
    morse = ''.join(letters)
    print(morse)
    for m in morse:
        if m == '.':
            playsound('dit.wav')
        elif m == '-':
            playsound('dah.wav')
        else:
            time.sleep(10)


def Morse_to_Txt():
    txt = input('Please type your Morse Code to convert to Text: ')
    letters = [k for i in txt.split() for k, v in morse_dict.items() if i == v]
    new_txt = ''.join(letters)
    print(new_txt)


print('''\n1 - Convert Text to Morse \n2 - Convert Morse to Text\n3 - Quit\n ''')

while True:
    try:
        choice_of_user = int(input('Type your Choice:'))

        if choice_of_user == 1:
            print(Txt_to_Morse())
            break
        elif choice_of_user == 2:
            print((Morse_to_Txt()))
            break
        elif choice_of_user == 3:
            print('Wrong Choice, Try again')
        else:
            print('AGAIN')
    except:
        print('Enter again')
