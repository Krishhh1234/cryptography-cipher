import string

def caesar_encrypt(message, key):
    shift = key % 26
    cipher = str.maketrans(
        string.ascii_lowercase + string.ascii_uppercase,
        string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift] +
        string.ascii_uppercase[shift:] + string.ascii_uppercase[:shift]
    )
    encrypted_message = message.translate(cipher)
    return encrypted_message

def caesar_decrypt(encrypted_message, key):
    shift = 26 - (key % 26)
    cipher = str.maketrans(
        string.ascii_lowercase + string.ascii_uppercase,
        string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift] +
        string.ascii_uppercase[shift:] + string.ascii_uppercase[:shift]
    )
    message = encrypted_message.translate(cipher)
    return message

# Example usage
message = "Subscribe To W J Pearce"
key = 3

encrypted_message = caesar_encrypt(message, key)
print(f'Encrypted message: {encrypted_message}')

decrypted_message = caesar_decrypt(encrypted_message, key)
print(f'Decrypted message: {decrypted_message}')
