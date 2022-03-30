from urls import routes
from views import NotFound
from datetime import date


def date_today(request):
    request['date'] = date.today()


fronts = [date_today]


class Application:
    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, answer):
        path = environ['PATH_INFO']
        print(environ['PATH_INFO'])
        if not path.endswith('/'):
            path = f'{path}/'
        if path in routes:
            view = self.routes[path]
        else:
            view = NotFound()
        request = {}
        for front in self.fronts:
            front(request)
        head, body = view(request)
        answer(head, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]
