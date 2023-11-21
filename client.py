import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12346))  # Connect to the proxy
    message = "Hello, Server!"
    client_socket.send(message.encode('utf-8'))
    client_socket.close()

if __name__ == "__main__":
    start_client()
