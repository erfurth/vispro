from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def run_ftp_server():
    authorizer = DummyAuthorizer()
    authorizer.add_user("test", "1234", "./exchange", perm="elradfmwMT")

    handler = FTPHandler
    handler.authorizer = authorizer
    handler.passive_ports = range(30000, 30010)
    handler.masquerade_address = "10.70.16.106"

    server = FTPServer(("0.0.0.0", 21), handler)
    server.serve_forever()
