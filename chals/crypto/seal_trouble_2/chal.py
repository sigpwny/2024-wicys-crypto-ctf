def encrypt(message, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(message)])

def main():
    passphrase = input("Enter secret key: ")
    key = [ord(char) for char in passphrase]
    message = b"sigpwny{not_the_real_flag}"
    
    # Encrypt
    ciphertext = encrypt(message, key)
    print("Encrypted message:", ciphertext.hex())

if __name__ == '__main__':
    main()