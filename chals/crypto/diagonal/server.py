import numpy as np
import random

FLAG = "sigpwny{mult1d1m3n510n4l}"

def inputs():
    print("[D] Define a 3 x 3 Integer Matrix M")
    M = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    for i in range(3):
        for j in range(3):
            try:
                M[i][j] = int(input(f"[D] M[{i}][{j}] = "))
            except:
                return None
    return M

def fun(M_, d):
    M = np.matrix(M_, dtype='object')
    M = M**d

    # [\\\]
    # [ \\]
    # [  \]
    return M[0, 0] + M[1, 1] + M[2, 2] + M[0, 1] + M[1, 2] + M[0, 2]

def main():
    secret = random.randint(1_000_000_000, 10_000_000_000)

    print("[D] Welcome")
    M = inputs()
    if M == None:
        print("[D] You tried something weird...")
        return

    res = fun(M, secret)
    print()
    print(f"[D] Have fun: {res}")
    print()
    try:
        guess = int(input(f"[D] Make a guess: "))
    except:
        print("[D] You tried something weird...")
        return

    if guess == secret:
        print(f"[D] {FLAG}")
    else:
        print(f"[D] Better luck next time!")

if __name__ == "__main__":
    main()
