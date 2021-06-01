"""
Import the necessary module from Python
"""
import math

'''
Input 2 prime numbers
'''

print("Please enter 2 prime numbers p,q>20 (etc 23,29,31)")
p = int(input("Enter the first prime number for p: "))
q = int(input("Enter the second prime number for q: "))


'''
Tests to see if a number is prime.
'''

def prime_check(a):
    if (a < 20):
        return False
    if (a == 2):
        return True
    elif ((a < 2) or ((a % 2) == 0)):
        return False
    elif (a > 2):
        for i in range(2, a):
            if not (a % i):
                return False

    return True


check_p = prime_check(p)
check_q = prime_check(q)
while (((check_p == False) or (check_q == False))):
    p = int(input("Enter a prime number for p: "))
    q = int(input("Enter a prime number for q: "))
    check_p = prime_check(p)
    check_q = prime_check(q)


'''
RSA Modulus
'''
n = p * q
print("RSA Modulus(n) is:", n)


'''
"Euler's Totient
'''
r = (p - 1) * (q - 1)
print("Euler's Totient (r) is:", r)


'''
Calculate gcd
'''
def egcd(e, r):
    while (r != 0):
        e, r = r, e % r
    return e



'''
Euclid's algorithm 
'''
def eugcd(e, r):
    for i in range(1, r):
        while (e != 0):
            a, b = r // e, r % e
            if (b != 0):
                print("%d = %d*(%d) + %d" % (r, a, e, b))
            r = e
            e = b


'''
Euclid's algorithm 
'''
def eea(a, b):
    if (a % b == 0):
        return (b, 0, 1)
    else:
        gcd, s, t = eea(b, a % b)
        s = s - ((a // b) * t)
        print("%d = %d*(%d) + (%d)*(%d)" % (gcd, a, t, s, b))
        return (gcd, t, s)


'''
Multiplicative Inverse
'''
def mult_inv(e, r):
    gcd, s, _ = eea(e, r)
    if (gcd != 1):
        return None
    else:
        if (s < 0):
            print("s=%d. Since %d is less than 0, s = s(modr), i.e., s=%d." % (s, s, s % r))
        elif (s > 0):
            print("s=%d." % (s))
        return s % r


'''
Calculate the highest value of e between 1 and 1000 that makes (e,r) coprime.
'''
for i in range(1, 1000):
    if (egcd(i, r) == 1):
        e = i
print("The value of e is:", e)


'''
Calculate d.
'''

print("EUCLID'S EXTENDED ALGORITHM:")
d = mult_inv(e, r)
print("The value of d is:", d)

'''
Return public and private keypair
'''
public = (e, n)
private = (d, n)
print("Private Key is:", private)
print("Public Key is:", public)



def encrypt(pk, plaintext):
    '''
    Unpack the key into it's components
    '''
    key, n = pk
    '''
    Convert letters  to numbers  using a^b mod m
    '''
    cipher = [pow(ord(char), key, n) for char in plaintext]
    '''
    Return the array of bytes.
    '''
    return cipher


def decrypt(pk, ciphertext):
    key, n = pk
    '''
    Generate the plaintext based on the ciphertext and key using a^b mod m.
    '''
    plain = [chr(int(char) ** key % n) for char in ciphertext]
    '''
    Return the array of bytes as a string
    '''
    return ''.join(plain)

if __name__ == '__main__':

    '''
    User's message.
    '''
    message = input("What would you like encrypted or decrypted?:")
    print("Your message is:", message)

    '''
    Choise 1 for encrypt an 2 for decrypt.
    '''
    choose = input("Please enter: \n1:for encryption \n2:for decryption ")
    if (choose == '1'):
        enc_msg = encrypt(public, message)
        print(' '.join(map(lambda x: str(x), enc_msg)))

    elif (choose == '2'):
        enc_msg = message.split(" ")
        print("Your decrypted message is:", decrypt(private, enc_msg))

    else:
        print("You entered the wrong option.")
        
