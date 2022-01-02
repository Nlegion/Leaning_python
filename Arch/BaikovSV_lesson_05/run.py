from wsgiref.simple_server import make_server

from superior.core import Application
from urls import fronts
from views import routes

application = Application(routes, fronts)

with make_server('', 8080, application) as httpd:
    print("Запуск на порту 8080...")
    httpd.serve_forever()
