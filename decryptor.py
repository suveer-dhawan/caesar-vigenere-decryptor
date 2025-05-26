'''
Name: Suveer Dhawan

Using function invocation, this program takes an encrypted string from the user
along with the decryption key. Based on the parameter, the message is decrypted
using either a Caesar or Vigenere cypher. 
'''

# Declare constants
alphabet_size = 26

# Storing Alphabet Table (Encryption Key)
alphabet_key = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def caesar_cypher(encrypted_text, shift):
    ''' 
    This function decrypts the input using a Caesar Cypher. 

        Parameters:
            encrypted_text: the encrypted message received as input from user
            shift: Caesar shift (int) received from user

        Returns:
            Prints the decrypted string
    '''
    decrypt_list = []

    for char in encrypted_text:
        if char in alphabet_key:
            index = alphabet_key.index(char)
            decrypt_num = (index - shift) % alphabet_size
            decrypt_char = alphabet_key[decrypt_num]
            shift = decrypt_num  # Update shift for next character
            decrypt_list.append(decrypt_char)

    # Display decrypted string
    print("The decrypted string is:")
    print("".join(decrypt_list))

def vigenere_cipher(encrypted_text, key):
    ''' 
    This function decrypts the input using a Vigenere Cypher
            
        Parameters:
            encrypted_text: the encrypted message received as input from user
            key: Vigenere decryption key (string) as entered by user

        Returns:
            Prints the decrypted string
    '''
    decrypt_list = []
    
    for value in range(len(encrypted_text)):
        if encrypted_text[value] in alphabet_key and key[value % len(key)] in alphabet_key:
            vig_shift = alphabet_key.index(key[value % len(key)])
            index = alphabet_key.index(encrypted_text[value])
            decrypt_num = (index - vig_shift) % alphabet_size
            decrypt_char = alphabet_key[decrypt_num]
            decrypt_list.append(decrypt_char)

    # Display decrypted string
    print("The decrypted string is:")
    print("".join(decrypt_list))

def decrypt_cypher(encrypted_text, key):
    ''' 
    This function checks if the key is a Caesar or Vigenere Cypher
    
        Parameters:
            encrypted_text: the encrypted message received as input from user
            key: Decryption key from user, either a Caesar shift (int) or Vigenère key (string)
        
        Using if/else to invoke Caesar or Vigenere functions, depending on if 
        the key is numeric or text.
    '''
    if key.isdigit():
        key = int(key)
        caesar_cypher(encrypted_text, key)
    else:
        vigenere_cipher(encrypted_text, key.upper())

if __name__ == "__main__":
    print("DECRYPT STRING")

    encrypt_string = input("Input encrypted string: ")
    if encrypt_string == "" or encrypt_string == "\n":
        print("Empty encrypted string.")
        quit()

    encrypt_text = "".join(encrypt_string.split()).upper()
    encrypt_key = input("Input key: ")

    decrypt_cypher(encrypt_text, encrypt_key)