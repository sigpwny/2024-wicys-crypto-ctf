from pwn import *

def main():

    # Here is some starter code for those unfamiliar with pwntools
    # I am not good at pwntools, so there may be better ways to do this
    # But this is how I know how to do things

    # Connect to remote server
    conn = remote("chal.cryptoctf.sigpwny.com", 5001)

    conn.recvline() # [D] Welcome
    conn.recvline() # [D] Define a 3 x 3 Integer Matrix M

    # Send matrix here
    # Replace the 0/1's with the numbers you want
    conn.sendline(b'1')
    conn.sendline(b'0')
    conn.sendline(b'0')
    conn.sendline(b'0')
    conn.sendline(b'1')
    conn.sendline(b'0')
    conn.sendline(b'0')
    conn.sendline(b'0')
    conn.sendline(b'1')

    conn.recvline()
    # Here is number the server gives
    res = int(conn.recvline().decode("utf-8")[13:].strip())
    print(f"Challenge Accepted: {res}")


    # TODO: Write some code to recover the secret from res!
    #
    # Bytes:
    #   pwntools reads and sends bytes
    #   .encode turns a string into a bytestring
    #   .decode("utf-8") turns a bytestring into a string
    #
    # Sending and Receiving:
    #   conn.sendline(b'#')
    #   output = conn.recvline()
    #   These do what you think
    #
    # Some basic string manipulation such as .strip() and slicing helps
    # Use alot of print statements in debugging this
    # Try some stuff locally as well
    # Have a working local solution *before* pwntools-ifying it
    #
    # pwntools is really useful, I recommend you learn it

if __name__ == "__main__":
    main()
