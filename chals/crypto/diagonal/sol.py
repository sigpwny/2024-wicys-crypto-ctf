from pwn import *
import sympy as sp

def main():

    conn = remote("chal.cryptoctf.sigpwny.com", 5001)

    conn.recvline() # [D] Welcome
    conn.recvline() # [D] Define a 3 x 3 Integer Matrix M

    # Send matrix
    conn.sendline(b'1')
    conn.sendline(b'1')
    conn.sendline(b'1')
    conn.sendline(b'0')
    conn.sendline(b'1')
    conn.sendline(b'1')
    conn.sendline(b'0')
    conn.sendline(b'0')
    conn.sendline(b'1')

    conn.recvline()
    # Here is number the server gives
    res = int(conn.recvline().decode("utf-8")[13:].strip())
    conn.recvline()
    print(f"Challenge Accepted: {res}")

    # Some solutions
    # TODO: Put some writing in here
    # disc = (25 - 4 * (6 - 2*int(res)))**(0.5)
    # secret = (-5 + disc) // 2

    n = sp.Symbol('n')
    secret = sp.solve(3 + 2*n + (n**2 + n) / 2 - res, n)[1]

    conn.sendline(str(int(secret)).encode())            # Send answer
    print(conn.recvline().decode("utf-8")[22:].strip()) # Print flag

if __name__ == "__main__":
    main()
