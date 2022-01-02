from superior.templates import render_


def index_view(request):
    print(request)
    return '200 OK', render_('index.html', color_name='none')


def black_view(request):
    print(request)
    return '200 OK', render_('index.html', color_name='black')


def red_view(request):
    print(request)
    return '200 OK', render_('index.html', color_name='red')


def white_view(request):
    print(request)
    return '200 OK', render_('index.html', color_name='white')


class Other:
    def __call__(self, request):
        return '200 OK', render_('index.html', color_name='other color')


def opposite_color_front(request):
    request['opposite_color'] = 'opposite color'


def similar_color_front(request):
    request['similar_color'] = 'similar color'
