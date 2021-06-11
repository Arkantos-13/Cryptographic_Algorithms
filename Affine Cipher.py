def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


"""
Modular Multiplicative Inverse Function
"""

def mod_inv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m


"""
Affine cipher encrytion function
returns the cipher text
"""

def affine_encrypt(message, key):
    """
    C = (a*P + b) % 26
    """
    return ''.join([chr(((key[0] * (ord(t) - ord('A')) + key[1]) % 26)
                        + ord('A')) for t in message.upper().replace(' ', '')])


"""
Affine cipher decryption function
returns original text
"""

def affine_decrypt(cipher, key):
    """
    P = (a^-1 * (C - b)) % 26
    """
    return ''.join([chr(((modinv(key[0], 26) * (ord(c) - ord('A') - key[1]))
                         % 26) + ord('A')) for c in cipher])


"""
Driver Code to test the above functions
"""

def main():
    
    # declaring text and key
    message = input('Please type your message you would like to Encrypt or Decrypt: ')
    key = [17, 20]
    choice = int(input('Press 1. For Encryption or 2. For Decryption: '))
    
    if choice == 1:
        # calling encryption function
        affine_encrypted_text = affine_encrypt(message, key)

        print('Your encrypted text is the following: {}'.format(affine_encrypted_text))
        
    else:
        # calling decryption function
        print('Your decrypted text is the following: {}'.format
               (affine_decrypt(message, key)))


main()

