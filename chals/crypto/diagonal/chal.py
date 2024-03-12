import numpy as np
import random

import sympy as sp

FLAG = "sigpwny{testing_yay!}"

def inputs():
    print("Define a 3 x 3 Integer Matrix M")
    M = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    for i in range(3):
        for j in range(3):
            M[i][j] = int(input(f"[D] M[{i}][{j}] = "))
    return M

def fun(M_, d):
    M = np.matrix(M_)
    M = M**d

    return M[0, 0] + M[1, 1] + M[2, 2] + M[0, 1] + M[1, 2] + M[0, 2]

def main():
    secret = random.randint(1_000_000_000, 10_000_000_000)

    M = inputs()
    res = fun(M, secret)
    print()
    print(f"[D] Have fun: {res}")
    print()
    guess = int(input(f"[D] Make a guess: "))

    if guess == secret:
        print(f"[D] {FLAG}")
    else:
        print(f"[D] Better luck next time!")


    # # Some test solutions
    # disc = (25 - 4 * (6 - 2*int(res)))**(0.5)
    # sec_ = (-5 + disc) // 2
    # print(sec_)

    # n = sp.Symbol('n')
    # print(sp.solve(3 + 2*n + (n**2 + n) / 2 - res, n))



if __name__ == "__main__":
    main()
