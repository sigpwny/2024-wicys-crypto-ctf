from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import sympy

e = 65539
n = 4462776610810429874302099425257433084349                     # It seems that n is very small...
c = [b'\x06\x86\xbc}\x0f\xfc\xac\x80\x90&S\x98\xa1!+F>',         # List of messages for you to decrypt
     b'\x04\xe9%7\xeb\xdd\xf6\xcd\x9e\x7f\xa2Z\x81\x16,\x9fh', 
     b"\x00\xa3\x19lP'\x04\x02\xb1\xe0\x89p-\x99\xcc\xf1@"]