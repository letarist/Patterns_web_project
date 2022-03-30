from wsgiref.simple_server import make_server
from letar_framework.main import Application, fronts
from urls import routes

application = Application(routes, fronts)
with make_server('', 8000, application) as httpd:
    print('start server ...')
    httpd.serve_forever()
