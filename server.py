from pyramid.config import Configurator
from pyramid.response import Response


def hello(request):
    return Response('Hello Pyramid!')


config = Configurator()
config.add_route('hello', '/')
config.add_view(hello, route_name='hello')

app = config.make_wsgi_app()

# Or from an .ini file:
# app = get_app('config.ini', 'application_name')
