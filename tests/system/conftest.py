import socket
import struct
from threading import Thread

import pytest

from .rtu_server import app as rtu
from .tcp_server import app as tcp


@pytest.fixture(autouse=True, scope="session")
def tcp_server(request):
    t = Thread(target=tcp.serve_forever)
    t.start()

    try:
        yield tcp
    finally:
        tcp.shutdown()
        tcp.server_close()
        t.join()


@pytest.fixture
def sock(tcp_server):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(tcp_server.socket.getsockname())

    try:
        yield sock
    finally:
        sock.close()


@pytest.fixture
def rtu_server():
    return rtu


@pytest.fixture
def mbap():
    return struct.pack('>HHHB', 0, 0, 6, 1)
