# Uncomment this to pass the first stage
import socket



def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    # server_socket.accept() # wait for client
    client_socket, client_address = server_socket.accept()
    data = client_socket.recv(1024)
    msg = b"+PONG\r\n"
    client_socket.send(msg)
    


if __name__ == "__main__":
    main()
