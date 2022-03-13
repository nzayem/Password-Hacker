import socket
import argparse


parser = argparse.ArgumentParser()

# adding arguments:

parser.add_argument('hostname')
parser.add_argument('port')
parser.add_argument('message')

args = parser.parse_args()

with socket.socket() as client_socket:

    address = (args.hostname, int(args.port))

    client_socket.connect(address)

    data = args.message
    data = data.encode()

    client_socket.send(data)

    response = client_socket.recv(1024)

    response = response.decode()
    print(response)
