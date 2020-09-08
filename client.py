import socket


class Client:
    def __init__(self, host, port, timeout):
        self.host = host
        self.port = port
        self.timeout = timeout

    def get(self, key):
        message = "get {}".format(key)
        with socket.create_connection((self.host, self.port), self.timeout) as sock:
            try:
                sock.sendall(b"get {}\n")
            except socket.timeout:
                print("get data timeout")
            except socket.error as ex:
                print("error", ex)


if __name__ == '__main__':
    client = Client("127.0.0.1", 8888, timeout=15)
    print(client.get("*"))
