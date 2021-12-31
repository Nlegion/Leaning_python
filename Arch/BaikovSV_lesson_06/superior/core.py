from quopri import decodestring
from superior.requests import GetRequests, PostRequests
# import datetime
# import html.parser as hlmtparser
from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
sys.path.append(str(BASE_DIR))


class Application:

    def __init__(self, routes_obj, fronts_obj):
        self.routes_lst = routes_obj
        self.fronts_lst = fronts_obj

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']

        if not path.endswith('/'):
            path = f'{path}/'

        request = {}
        method = environ['REQUEST_METHOD']
        request['method'] = method

        if method == 'POST':
            data = PostRequests().get_request_params(environ)
            request['data'] = Application.decode_value(data)
            print(f'Нам пришёл post-запрос: {Application.decode_value(data)}')
        #     if method == 'POST':
        #         data = PostRequests().get_request_params(env)
        #         message = Application.decode_value(data)
        #         now = datetime.datetime.now()
        #         name = message['your_name']
        #         text = message['your_enquiry']
        #         email = message['your_email']
        #         print(f'Нам пришёл post-запрос: {message}')
        #         with open(f'{BASE_DIR}/messages/message_{now.strftime("%d%m%Y")}_{now.strftime("%H.%M.%S")}.txt',
        #                   'w') as message_file:
        #             message_file.write(
        #                 f'Нам пришло сообщение от: {name} \n емейл: \n {email} \n текстом: \n {text}')

        if method == 'GET':
            request_params = GetRequests().get_request_params(environ)
            request['request_params'] = Application.decode_value(request_params)
            print(f'Нам пришли GET-параметры:'
                  f' {Application.decode_value(request_params)}')

        if path in self.routes_lst:
            view = self.routes_lst[path]
        else:
            start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
            return '404 WHAT', '404 PAGE Not Found'

        for front in self.fronts_lst:
            front(request)
        # запуск контроллера с передачей объекта request
        # print('core:', request)
        code, body = view(request)
        # print('core:', code, body)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]

    @staticmethod
    def decode_value(data):
        new_data = {}
        for k, v in data.items():
            val = bytes(v.replace('%', '=').replace("+", " "), 'UTF-8')
            val_decode_str = decodestring(val).decode('UTF-8')
            new_data[k] = val_decode_str
        return new_data

    # @staticmethod
    # def decode_value(data):
    #     new_data = {}
    #     for k, v in data.items():
    #         val = bytes(v.replace('%', '=').replace("+", " "), 'UTF-8')
    #         val_decode_str = decodestring(val).decode('UTF-8')
    #         val_decode_str = decodestring(val_decode_str).decode('UTF-8')
    #         if "&#" in val_decode_str:
    #             parser = hlmtparser.HTMLParser()
    #             val_decode_str = parser.unescape(val_decode_str)
    #         new_data[k] = val_decode_str
    #     return new_data
