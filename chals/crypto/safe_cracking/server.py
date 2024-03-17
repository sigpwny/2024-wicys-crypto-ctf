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

def print_notes():
    print("\nHints to help me remember the combination to my safe (since I always forget it).")
    print("The answer to each problem corresponds to one part of the safe combination.")
    print("1. Anna and Beatrice perform a Diffie-Hellman key exchange where p = 17 and g = 3. Privately, Anna selects 5 and Beatrice chooses 11. What's their shared secret key?")
    print("2. The two perform another key exchange. Now, p = 157 and g = 2. Anna's new private key is 67, while Beatrice's public key is 73. What is Anna's public key?")
    print("3. Anna forgot her private key and wants to solve for it. We know the following:\n\tTheir shared secret key, s, is equal to 2417097.\n\tThe values of p and g are 3042161 and 5, respectively.\n\tBeatrice's private key is 73.\n") 
    print("Get ready to start guessing!")
    time.sleep(1)
    
def main():
    print("Welcome to my extremely secure safe!")
    print("Note to self: Just in case I forget the combination, here's a note that reminds me how to remember it.")
    view_notes = input("View notes? If yes, enter 'y' ")

    if (view_notes == "y"):
        print_notes()
    else:
        print("Might want to view the notes...")
        time.sleep(1)
        print("Get ready to start guessing!")
    if prompt():
        print("You have unlocked the safe! Please don't take anything except for this flag:", FLAG)
    else:
        print("Incorrect, try again.")

if __name__ == "__main__":
    main()
