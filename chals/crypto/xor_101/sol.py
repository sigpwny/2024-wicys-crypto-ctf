# Step 1: Inspect "comment" tag in metadata for passphrase (ex: exiftool seal1.png)
passphrase = "tomatoisafruit"

# Step 2:
def decrypt(ciphertext, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(ciphertext)])

# Provided from message.txt
input = "07060a110301100806030601001a13301e15151d1d160539052a11440612"

# Convert hexadecimal string to bytes
b_input = bytes.fromhex(input)

# Use key to decrypt
key = [ord(char) for char in passphrase]
output = decrypt(b_input, key)

print("Flag:", output.decode('utf-8'))
