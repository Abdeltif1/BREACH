import socket

def start_server():
    #set ip and port

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('140.122.185.174', 8081))
    server_socket.listen(1)
    print("Server is listening on port 12345...")
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} has been established.")
        msg = client_socket.recv(1024).decode('utf-8')
        print(f"Received message: {msg}")
        client_socket.close()

if __name__ == "__main__":
    start_server()
