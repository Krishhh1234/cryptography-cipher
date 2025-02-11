# cryptography-cipher
This Python script implements a Caesar Cipher, a simple encryption technique where each letter in the message is shifted by a specified key. It supports both encryption and decryption of text, preserving uppercase and lowercase letters for accurate encoding.


# Caesar Cipher Encryption/Decryption Script 🛡️

## Description
This project provides a Python implementation of the **Caesar Cipher**, a basic encryption technique used to encode and decode messages by shifting letters by a given key. The cipher works for both uppercase and lowercase letters, maintaining the original casing.

The script includes two main functions:
1. **`caesar_encrypt(message, key)`** – Encrypts the input message using the given key.
2. **`caesar_decrypt(encrypted_message, key)`** – Decrypts the encrypted message back to its original form.

## Features
- Supports both uppercase and lowercase letters.
- Allows you to encrypt and decrypt any text message.
- Simple and easy to use with minimal setup.

## Example Usage
```python
message = "Subscribe To W J Pearce"
key = 3

encrypted_message = caesar_encrypt(message, key)
print(f'Encrypted message: {encrypted_message}')

decrypted_message = caesar_decrypt(encrypted_message, key)
print(f'Decrypted message: {decrypted_message}')


##expected output

Encrypted message: Vxevfuleh Wr Z M Shdufh
Decrypted message: Subscribe To W J Pearce
