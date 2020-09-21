import socket
import time


class ClientError(Exception):
    pass


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
        message_timestamp = timestamp or int(time.time())
        msg = str.encode(f"put {metric} {value} {message_timestamp}\n")
        try:
            self.sock.sendall(msg)
            data = self.sock.recv(1024).decode("utf-8")
            if data.split("\n")[0] != "ok":
                raise ClientError
        except ClientError as ex:
            raise ClientError

    def get(self, key):
        message = str.encode(f"get {key}\n")
        bytes(message)
        try:
            self.sock.sendall(message)
            data = self.sock.recv(1024).decode("utf-8")
            if data.split("\n")[0] != "ok":
                raise ClientError
            dic = {}
            resp = data.split("\n")
            for i in resp[1:len(resp) - 2]:
                metrics = i.split()
                key = metrics[0]
                timestamps = [int(tmp) for tmp in metrics[2::2]]
                value = [float(vl) for vl in metrics[1::2]]
                if not timestamps or not value:
                    raise ClientError
                msg = []
                for j in range(len(timestamps)):
                    msg.append((timestamps[j], value[j]))
                if key in dic.keys():
                    old_msg = dic[key]
                    new_msg = old_msg + msg
                    dic[key] = sorted(new_msg)
                else:
                    dic[key] = sorted(msg)
            return dic
        except socket.timeout:
            print("get data timeout")
        except ClientError as ex:
            raise ClientError
        except Exception as err:
            raise ClientError


if __name__ == '__main__':
    client = Client("127.0.0.1", 8888, timeout=15)
    # client.put("asd", "asd", 15)
    print(client.get("*"))
    # msg = "ok\npalm.cpu 10.5 1501864259\npalm.cpu 10.5 1501864259\n\n"
    # dic = {}
    # resp = msg.split("\n")
    # print(resp)
    # for i in resp[1:len(resp) - 2]:
    #     key = i.split()[0]
    #     if key in dic:
    #         dic[key] = dic[key].append