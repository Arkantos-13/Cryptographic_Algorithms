'''
User's input:the path of image.
'''

img_path = input(r'Enter path of Image:')



'''
User's input:the key to encrypt or decrypt.
'''

key = int(input('Enter Key for encryption or decryption of Image:'))



'''
Open file to read data.
'''

f = open(img_path, 'rb')



'''
Storing image data in image variable
'''

image = f.read()
f.close()


'''
Converting image into byte array.
'''

image = bytearray(image)



'''
Perform XOR operation on each value of bytearray.
'''

for index, values in enumerate(image):
    image[index] = values ^ key




'''
Open file to write data.
'''

f1 = open(img_path, 'wb')



'''
Write encrypted data of image.
'''

f1.write(image)
f1.close()
print('Encryption/Decryption Done...')
