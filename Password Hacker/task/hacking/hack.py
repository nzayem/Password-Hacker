import socket
import argparse
from itertools import product


def generate_password():
    index = 1
    abc = 'abcdefghijklmnopqrstuvwxyz1234567890'
    while True:
        yield from product(abc, repeat=index)
        index += 1


my_pass = generate_password()

parser = argparse.ArgumentParser()

# adding arguments:

parser.add_argument('hostname')
parser.add_argument('port')

args = parser.parse_args()

client_socket = socket.socket()

address = (args.hostname, int(args.port))

client_socket.connect(address)

while True:
    guess = (''.join(next(my_pass))).encode()
    client_socket.send(guess)
    response = (client_socket.recv(1024)).decode()
    if response == "Connection success!":
        print(guess.decode())
        break

client_socket.close()
