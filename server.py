import socket
import sys


class CreatingServer:

    @staticmethod
    def creating_a_server_to_connect_to_the_client(ip_address, port, number_of_listeners_at_the_port, size_buffer):
        socket_server = socket.socket()
        socket_server.bind((ip_address, port))
        socket_server.listen(number_of_listeners_at_the_port)

        print('Server working...')
        my_name = input('Enter your name!: ').upper()

        client_socket, address = socket_server.accept()

        client_data = client_socket.recv(size_buffer).decode()
        print(client_data + ' -> connection established!')
        client_socket.send(my_name.encode())

        while True:
            message = input('I: ')
            client_socket.send(message.encode())
            message = client_socket.recv(size_buffer).decode()
            print(client_data + ': ' + message)
            if message == 'stop':
                print('<<< close server socket >>>')
                sys.exit()


def creation_of_an_object_through_which_data_is_exchanged(ip_address, port, number_of_listeners_at_the_port,
                                                          size_buffer):
    return CreatingServer.creating_a_server_to_connect_to_the_client(ip_address, port,
                                                                     number_of_listeners_at_the_port, size_buffer)


# MAIN
IP_ADDRESS, PORT, SIZE_BUFFER = '127.0.0.1', 2000, 1024
NUMBER_OF_CLIENTS_FOR_THE_PORT = 1

if __name__ == '__main__':
    creation_of_an_object_through_which_data_is_exchanged(IP_ADDRESS, PORT, NUMBER_OF_CLIENTS_FOR_THE_PORT,
                                                          SIZE_BUFFER)
