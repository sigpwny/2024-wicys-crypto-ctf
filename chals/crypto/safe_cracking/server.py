import time
import random

FLAG = "sigpwny{is_this_r3@lly_the_m0st_s3cure_s@f3_3ver?}"
combos = [11, 112, 81] 

def prompt():
    for i in range(3):
        try:
            value = int(input(f"Enter the {['first', 'second', 'third'][i]} value: ").strip())
            if value != combos[i]:
                return False
        except ValueError:
            print("Please enter a number.")
            return False
    return True
    
def main():
    print("Welcome to my extremely secure safe!")
    time.sleep(1)
    print("Get ready to start guessing!")
    if prompt():
        print("You have unlocked the safe! Please don't take anything except for this flag:", FLAG)
    else:
        print("Incorrect, try again.")

if __name__ == "__main__":
    main()
