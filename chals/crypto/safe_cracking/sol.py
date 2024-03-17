# PART 1 and PART 2
# Multiple ways of getting here, can just use an online generator 

# --- PART 3 ---
# Part 3: Finding A

p = 3042161
b = 73
shared_secret = 2417097

def find_base(p, b, shared_secret):
    for base in range(1, p):
        if pow(base, b, p) == shared_secret:
            return base
    return None

# Part 3: Finding a
base = 5
A = find_base(p, b, shared_secret)

def find_exponent(p, base, A):
    for x in range(1, p):
        if pow(base, x, p) == A:
            return x
    return None

a = find_exponent(p, base, A)

print("Third number to unlock safe:", a)

