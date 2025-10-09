try:
    from socketserver import TCPServer
except ImportError:
    from SocketServer import TCPServer

from tests.system import route
from umodbus import conf
from umodbus.server.tcp import RequestHandler, get_server

conf.SIGNED_VALUES = True

app = get_server(TCPServer, ('localhost', 0), RequestHandler)

route.bind_routes(app)
