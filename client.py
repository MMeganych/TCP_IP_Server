import socket
from server import IP_ADDRESS, PORT, SIZE_BUFFER
import sys


class CreatingClientForServer:

    @staticmethod
    def creating_connect_to_the_server(ip_address, port, size_buffer):
        socket_server = socket.socket()

        my_name = input('Enter your name!: ').upper()

        socket_server.connect((ip_address, port))

        socket_server.send(my_name.encode())
        socket_data = socket_server.recv(size_buffer).decode()
        print(socket_data + ' -> joined!')

        while True:
            message = socket_server.recv(size_buffer).decode()
            print(socket_data + ': ' + message)
            if message == 'stop':
                print('<<< close client socket >>>')
                sys.exit()
            message = input('I: ')
            socket_server.send(message.encode())


def creation_of_an_object_through_which_data_is_exchanged(ip_address, port, size_buffer):
    return CreatingClientForServer.creating_connect_to_the_server(ip_address, port, size_buffer)


# MAIN

if __name__ == '__main__':
    creation_of_an_object_through_which_data_is_exchanged(IP_ADDRESS, PORT, SIZE_BUFFER)
