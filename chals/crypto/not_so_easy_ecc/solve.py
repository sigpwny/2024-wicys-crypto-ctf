from pwn import *
from Crypto.Util.number import getPrime

def main():

    conn = process(["python3", "chal.py"])

    conn.recvline() # [D] Elliptic Curve Cryptography is so powerful, that I'll let you choose the curve!
    conn.recvline() # [D] I'm using a standard curve of the shape y^2 = x^3 + ax + b (mod p)

    prime = getPrime(128)
    conn.sendline(str(prime).encode())
    conn.sendline(b'0')
    conn.sendline(b'0')
    conn.recvline() # skip inputs
    
    conn.recvuntil(b': ') # [D] Here's a point P on the curve:
    p = conn.recvline() # [D] (x, y)
    conn.recvuntil(b': ') # [D] With a random number k, here's k*P:
    kp = conn.recvline() # [D] With a random number k, here's k*P: (x, y)
    
    p = p.decode().strip().split(',')
    kp = kp.decode().strip().split(',')

    xp, yp = int(p[0][1:]), int(p[1][:-1])
    xkp, ykp = int(kp[0][1:]), int(kp[1][:-1])

    mappedP = xp * pow(yp, -1, prime)
    mappedKP = xkp * pow(ykp, -1, prime)
    inv_mappedP = pow(mappedP, -1, prime)
    k = (mappedKP * inv_mappedP) % prime

    conn.sendline(str(k).encode())
    conn.recvuntil(b"Here's your flag: ") # skip input
    flag = conn.recvline().decode().strip()
    print(flag)

if __name__ == "__main__":
    main()
