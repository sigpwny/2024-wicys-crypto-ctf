import sympy as sp

def main():

    res = 18669237451167230340

    # Some solutions
    disc = (25 - 4 * (6 - 2*int(res)))**(0.5)
    sec_ = (-5 + disc) // 2
    print(int(sec_))

    n = sp.Symbol('n')
    print(sp.solve(3 + 2*n + (n**2 + n) / 2 - res, n)[1])



if __name__ == "__main__":
    main()
