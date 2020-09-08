import socket


class Client:
    def __init__(self, host, port, timeout):
        self.host = host
        self.port = port
        self.timeout = timeout

    def get(self, key):
        message = f"get {key}"
        with socket.create_connection((self.host, self.port), self.timeout) as sock:
            try:
                sock.sendall(b"get {}\n")
                data = sock.recv(1024).decode("utf-8")
                if data.split("\n") != "ok":
                    raise socket.error("Wrong command")
                return data
            except socket.timeout:
                print("get data timeout")
            except socket.error as ex:
                print("error", ex)


if __name__ == '__main__':
    client = Client("127.0.0.1", 8888, timeout=15)
    print(client.get("*"))
