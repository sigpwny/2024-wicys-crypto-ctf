from mini_ecdsa import *
from flag import flag
from tonelli_shanks import tonelli
from Crypto.Util.number import *

def elliptic_curve_random_point(E):
    while True:
        x = getRandomRange(1, E.char-1)
        y2 = (x**3 + E.b*x + E.c) % E.char
        y = tonelli(y2, E.char)
        if y:
            return Point(x, y)

def die(*args):
    print(*args)
    exit(1)

def main():
    nbits = 128
    print("Elliptic Curve Cryptography is so powerful, that I'll let you choose the curve!")
    print("I'm using a standard curve of the shape y^2 = x^3 + ax + b (mod p)")

    p = input(f"Enter the prime p ({nbits} bits): ")
    try:
        p = int(p)
    except:
        die('at least give me a number')
    if not(isPrime(p) and p.bit_length() == nbits):
        die('nice try')

    a = input("Enter the coefficient a: ")
    try:
        a = int(a)
    except:
        die('at least give me a number')

    b = input("Enter the coefficient b: ")
    try:
        b = int(b)
    except:
        die('at least give me a number')

    E = CurveOverFp(0, a, b, p)
    point = elliptic_curve_random_point(E)
    k = getRandomRange(2, p >> 1)
    print(f"Here's a point P on the curve: {point}")
    print(f"With a random number k, here's k*P: {E.mult(point, k)}")
    ans = int(input("What is k? "))
    if ans == k:
        print(f"Congratulations! Here's your flag: {flag}")
    else:
        die("Nope, that's not the right k!")

if __name__ == "__main__":
    main()