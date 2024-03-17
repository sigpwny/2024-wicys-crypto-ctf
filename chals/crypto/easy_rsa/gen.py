from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import sympy

flags = ["sigpwn","y{rsA_","FtW:P}"]

# Randomly generating two primes
p = 70979368125456165107
q = 62874279226076849807
e = 65539
n = p*q # 4462776610810429874302099425257433084349  
totn = int(sympy.totient(n))
d = pow(e,-1,totn) # 2524360373456480207131100680183211940587

# Generate public and private keys
pubkey = RSA.construct((n,e))
cipher = PKCS1_v1_5.new(pubkey)
priv = RSA.construct((n,e,d))
ciph = PKCS1_v1_5.new(priv)

# Print encryption for each flag chunk
for flag in flags:
    ciphertext = cipher.encrypt(flag.encode('utf-8'))
    print(ciphertext)
    plaintext = ciph.decrypt(ciphertext, None)
    print(plaintext.decode("utf-8")) 
