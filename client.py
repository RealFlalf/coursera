import socket
import time


class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        try:
            self.sock = socket.create_connection((self.host, self.port), self.timeout)
        except socket.error as err:
            print(err)

    def __del__(self):
        self.sock.close()

    def put(self, metric, value, timestamp=None):
        if timestamp is None:
            msg = str.encode(f"put {metric} {value} {int(time.time())}\n")
        else:
            msg = str.encode(f"put {metric} {value} {timestamp}\n")
        try:
            self.sock.sendall(msg)
        except socket.ClientError as ex:
            print("error", ex)

    def get(self, key):
        message = str.encode(f"get {key}\n")
        bytes(message)
        try:
            self.sock.sendall(message)
            data = self.sock.recv(1024).decode("utf-8")
            if data.split("\n")[0] != "ok":
                raise socket.ClienError
            dic = {}
            resp = data.split("\n")
            for i in resp[1:len(resp) - 2]:
                metrics = i.split()
                key = metrics[0]
                timestamps = [int(tmp) for tmp in metrics[2::2]]
                value = [float(vl) for vl in metrics[1::2]]
                msg = []
                for j in range(len(timestamps)):
                    msg.append((timestamps[j], value[j]))
                dic[key] = sorted(msg)
            return dic
        except socket.timeout:
            print("get data timeout")
        except socket.ClientError as ex:
            print("error", ex)


if __name__ == '__main__':
    client = Client("127.0.0.1", 8888, timeout=15)
    client.put("asd", "asd", 15)
    print(client.get("*"))
