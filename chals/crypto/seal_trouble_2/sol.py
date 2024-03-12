import itertools

def decrypt(ciphertext, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(ciphertext)])

# Provided from message.txt
input_hex = "03010e031f1e111207001106022c111f1d36150702371d1b0d2f0e0000005149480e"

# Convert hexadecimal string to bytes
ciphertext = bytes.fromhex(input_hex)

# Brute-force all possible 5-character lowercase alphabetical passphrases
length = 5
possible_characters = "abcdefghijklmnopqrstuvwxyz"

for possible_passphrase in itertools.product(possible_characters, repeat=length):
    key = [ord(char) for char in possible_passphrase]
    decrypted_message = decrypt(ciphertext, key)

    # Check if the decrypted message begins with sigpwny to narrow down search
    if b'sigpwny' in decrypted_message:
        print("Passphrase:", ''.join(possible_passphrase))
        print("Flag:", decrypted_message.decode('utf-8'))
        break
