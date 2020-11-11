#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import sys
import random
import concurrent.futures
import socket
import json
import threading
import time

from util import recvall

HEADER_SIZE = 4

ADDR = ('0.0.0.0', 50637)


def __recv(sock, as_str=False):
    header = recvall(sock, 4)
    bytes_to_read = int.from_bytes(header, byteorder=sys.byteorder)
    print('%d bytes to read!' % bytes_to_read)

    data = recvall(sock, bytes_to_read)
    if as_str:
        data = data.decode("utf-8")

    return data


def handle_connection(sock, addr):
    tag = '%s:%s' % (threading.get_ident(), addr)
    # [1] client -> server
    data = __recv(sock, as_str=True)
    print(data)

    data = json.loads(data)
    print('[%s] recv: %s' % (tag, data))

    # [2] server -> client
    ActionCommand = {
        "ActionNumbers": 2,
        "Actions": [
            {
                "Id": 0,
                "Engine": 5,
                "Direction": 0
            },
            {
                "Id": 4,
                "Engine": 2,
                "Direction": 2
            },
        ]
    }
    data = json.dumps(ActionCommand)
    data = data.encode("utf-8")
    print('[%s] send: %d bytes' % (tag, len(data)), data)
    sock.sendall(int.to_bytes(len(data), HEADER_SIZE, byteorder=sys.byteorder))
    time.sleep(1)
    sock.sendall(data)

    # [4] Close
    print("Socket Closing")
    time.sleep(10)
    sock.close()


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(ADDR)
    sock.listen(8)
    print('Server is running at %s' % (ADDR,))

    pool = concurrent.futures.ThreadPoolExecutor(max_workers=8)

    while True:
        print('Waiting for connection..')
        client, addr = sock.accept()
        pool.submit(handle_connection, client, addr)    # future.result()


if __name__ == "__main__":
    main()
