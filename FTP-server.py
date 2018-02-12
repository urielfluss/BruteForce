from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("user", "", "/home", perm="elradfmw")
authorizer.add_anonymous("/home", perm="elradfmw")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("0.0.0.0", 1026), handler)
server.serve_forever()