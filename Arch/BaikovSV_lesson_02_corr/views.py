from superior.templates import render
from datetime import date


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html')


class About:
    def __call__(self, request):
        return '200 OK', render('about.html')


class Contact:
    def __call__(self, request):
        return '200 OK', render('contact.html', data=request.get('date', None))


def secret_front(request):
    request['date'] = date.today()


def other_front(request):
    request['key'] = 'key'
