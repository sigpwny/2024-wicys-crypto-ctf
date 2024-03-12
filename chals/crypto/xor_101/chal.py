def encrypt(message, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(message)])

def main():
    passphrase = input("Enter passphrase: ")
    key = [ord(char) for char in passphrase]
    message = b"sigpwny{fake_flag}"
    
    # Encrypt
    ciphertext = encrypt(message, key)
    print("Encrypted message:", ciphertext.hex())

if __name__ == '__main__':
    main()