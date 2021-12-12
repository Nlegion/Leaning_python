from quopri import decodestring
from superior.requests import GetRequests, PostRequests
import datetime
import html.parser as hlmtparser


class Application:
    def __init__(self, urlpatterns: dict, front_controllers: list):
        self.urlpatterns = urlpatterns
        self.front_controllers = front_controllers

    def __call__(self, env, start_response):
        path = env['PATH_INFO']
        if path[-1] != '/':
            path = f'{path}/'
        request = {}
        method = env['REQUEST_METHOD']
        request['method'] = method
        if method == 'POST':
            data = PostRequests().get_request_params(env)
            message = Application.decode_value(data)
            now = datetime.datetime.now()
            print(repr(message))
            name = message['your_name']
            text = message['your_enquiry']
            email = message['your_email']
            print(f'Месседж от {name} емейл {email} и текстом {text}')
            with open(f'../BaikovSV_lesson_02/messages/message_{now.strftime("%d%m%Y")}_{now.strftime("%H.%M.%S")}.txt',
                      'w') as message_file:
                message_file.write(
                    f'Нам пришло сообщение от: {name} \n емейл: \n {email} \n текстом: \n {text}')

        # if method == 'GET':
        #     request_params = GetRequests().get_request_params(env)
        #     request['request_params'] = request_params
        #     print(f'Нам пришли GET-параметры: {request_params}')

        if path in self.urlpatterns:
            view = self.urlpatterns[path]
            request = {}
            for controller in self.front_controllers:
                controller(request)
            code, text = view(request)
            start_response(code, [('Content-Type', 'text/html')])
            return [text.encode('utf-8')]
        else:
            start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
            return '404 WHAT', '404 PAGE Not Found'

    @staticmethod
    def decode_value(data):
        new_data = {}
        for k, v in data.items():
            val = bytes(v.replace('%', '=').replace("+", " "), 'UTF-8')
            val_decode_str = decodestring(val).decode('UTF-8')
            val_decode_str = decodestring(val_decode_str).decode('UTF-8')
            if "&#" in val_decode_str:
                parser = hlmtparser.HTMLParser()
                val_decode_str = parser.unescape(val_decode_str)
            new_data[k] = val_decode_str
        return new_data
