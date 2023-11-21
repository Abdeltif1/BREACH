import socketserver
import zlib
import os
import random
import string
from Crypto.Cipher import DES

SECRET_LENGTH = 20

def generate_secret():
    return ''.join([random.choice(string.printable) for _ in range(SECRET_LENGTH)])

def encrypt_data(data):
    initialization_vector = os.urandom(8)
    des_cipher = DES.new(b'01234567', DES.MODE_CBC, initialization_vector)
    data += b'\x00' * (8 - len(data) % 8)
    ciphertext = initialization_vector + des_cipher.encrypt(data)
    return ciphertext

class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        received_data = self.receive_blob()
        compressed_message = zlib.compress(f'user_data={received_data};secret={SECRET}'.encode('utf-8'))
        encrypted_message = self.encrypt(compressed_message)
        self.send_blob(encrypted_message)

    def receive_blob(self):
        return self.request.recv(1024)

    def encrypt(self, data):
        return encrypt_data(data)

    def send_blob(self, data):
        self.request.sendall(data)

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 30001

    SECRET = generate_secret()
    print('THE SECRET IS %s' % repr(SECRET))

    socketserver.TCPServer.allow_reuse_address = True
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
