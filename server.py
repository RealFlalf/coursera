import asyncio
import bisect

class ServerError(Exception):
    pass






class ClientServerProtocol(asyncio.Protocol):
    full_data = {}
    def connection_made(self, transport):
        print("Client connected")
        self.transport = transport



    def data_received(self, data):
        resp = self.process_data(data.decode())
        self.transport.write(resp.encode())

    def process_data(self, rec_data):
        method = rec_data.split()[0]
        if method == "put":
            return self.put(rec_data)
        elif method == "get":
            return self.get(rec_data)
        else:
            raise ServerError
        return rec_data

    def put(self, rec_data):
        try:
            key, value, timestamp = rec_data.split()[1::]
            if key not in self.full_data:
                self.full_data[key] = []
            bisect.insort(self.full_data[key], ((int(timestamp), float(value))))
        except ValueError:
            raise ServerError
        print(self.full_data)
        return "ok\n\n"

    def get(self):
        pass


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
