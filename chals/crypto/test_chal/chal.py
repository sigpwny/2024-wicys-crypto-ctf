import hashlib
import os.path

if __name__ == '__main__':
    print("Welcome to my neutron collider. Using state of the art technology, I will smash two strings into each other. I call this ability 'string theory'.")
    print("Weird stuff happens when they collide... the energy of the collision is so high it creates another third string that my research team is calling a 'flag'. ")
    print("BUT!!!! To save resources, your strings must be sigpwny (TM) branded!!!")

    x = input("string 1 > ").encode('utf8','surrogateescape')
    y = input("string 2 > ").encode('utf8','surrogateescape')

    if not x.startswith(b'sigpwny{') or not y.startswith(b'sigpwny{'):
        print("Hey! I'm on a tight budget here. I need to reinvest as much as possible into my collider. Make sure both strings are sigpwny (TM) branded.")

    if hashlib.md5(x).hexdigest() == hashlib.md5(y).hexdigest():
        print(open('flag.txt').read() if os.path.isfile('flag.txt') else 'Error: no flag file found')
    else:
        print("Yeah those strings didn't collide. Maybe collide two different strings...")