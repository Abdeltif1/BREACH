import socket

def start_proxy():
    proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxy_socket.bind(('localhost', 12346))
    proxy_socket.listen(1)
    print("Proxy is listening on port 12346...")
    while True:
        client_socket, addr = proxy_socket.accept()
        print(f"Connection from {addr} has been established.")
        msg = client_socket.recv(1024).decode('utf-8')
        print(f"Received message: {msg}")
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.connect(('localhost', 12345))
        server_socket.send(msg.encode('utf-8'))
        server_socket.close()
        client_socket.close()

if __name__ == "__main__":
    start_proxy()
