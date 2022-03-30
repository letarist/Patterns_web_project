from letar_framework.templator import render


class About:
    def __call__(self, request):
        return '200 OK', render('about.html', date=request.get('date', None))


class Contacts:
    def __call__(self, request):
        return '200 OK', render('contact.html', date=request.get('date', None))


class NotFound:
    def __call__(self, request):
        return '404 NOT FOUND', [b'NOT FOUND']


class Index:
    def __call__(self, request):
        print(request)
        return '200 OK', render('index.html', date=request.get('date', None))
