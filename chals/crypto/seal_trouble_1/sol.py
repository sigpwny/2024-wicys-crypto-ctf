# Step 1: Inspect "comment" tag in metadata for passphrase (ex: exiftool seal1.png)
passphrase = "morefishplz"

# Step 2:
def decrypt(ciphertext, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(ciphertext)])

# Provided from message.txt
input = "1e06151511070a1303091b011c2d090f021637085c0810"

# Convert hexadecimal string to bytes
b_input = bytes.fromhex(input)

# Use key to decrypt
key = [ord(char) for char in passphrase]
output = decrypt(b_input, key)

print("Flag:", output.decode('utf-8'))
