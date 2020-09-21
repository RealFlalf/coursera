import asyncio
import bisect


class ServerError(Exception):
    pass


class ClientError(Exception):
    pass


class ClientServerProtocol(asyncio.Protocol):
    full_data = {}

    def connection_made(self, transport):
        print("Client connected")
        self.transport = transport

    def data_received(self, data):
        resp = self.process_data(data.decode())
        print(resp)
        self.transport.write(resp.encode())

    def process_data(self, rec_data):
        try:
            method = rec_data.split()[0]
        except IndexError:
            return "error\nwrong command\n\n"
        if method == "put":
            return self.put(rec_data)
        elif method == "get":
            return self.get(rec_data)
        else:
            return "error\nwrong command\n\n"
        return rec_data

    def put(self, rec_data):
        try:
            key, value, timestamp = rec_data.split()[1::]
            if key not in self.full_data:
                self.full_data[key] = []
            metric = dict(self.full_data[key])
            timestamp = int(timestamp)
            if timestamp in list(metric.keys()):
                metric[timestamp] = float(value)
                self.full_data[key] = sorted(list(metric.items()))
            else:
                bisect.insort(self.full_data[key], (timestamp, float(value)))
        except ValueError:
            return "error\nwrong command\n\n"
        print(self.full_data)
        return "ok\n\n"

    def get(self, rec_data):
        if len(rec_data.split()) != 2:
            return "error\nwrong command\n\n"
        resp = "ok\n"
        if rec_data == "get *\n":
            for key, metric in self.full_data.items():
                for value in metric:
                    resp += ' '.join([key, str(value[1]), str(value[0])])
                    resp += "\n"
            resp += "\n"
            print(resp)
        else:
            try:
                key = rec_data.split()[1].rstrip()
                for value in self.full_data[key]:
                    resp += ' '.join([key, str(value[1]), str(value[0])])
                    resp += "\n"
                resp += "\n"
            except Exception as err:
                resp += "\n"
                return resp
        return resp


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        host, port
    )

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == '__main__':
    run_server('127.0.0.1', 8181)
