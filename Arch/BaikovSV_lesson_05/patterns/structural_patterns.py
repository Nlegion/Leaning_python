from time import time
from patterns.сreational_patterns import Logger


class AppRoute:
    def __init__(self, routes, url):
        self.routes = routes
        self.url = url

    def __call__(self, cls):
        self.routes[self.url] = cls()


# class Debug:
#
#     def __init__(self, name):
#         self.name = name
#
#     def __call__(self, cls):
#         def timeit(method):
#             def timed(*args, **kw):
#                 ts = time()
#                 result = method(*args, **kw)
#                 te = time()
#                 delta = te - ts
#
#                 print(f'debug --> {self.name} выполнялся {delta:2.2f} ms')
#                 return result
#
#             return timed
#
#         return timeit(cls)


class Debug:

    def __init__(self, name):
        self.name = name

    def __call__(self, cls):
        def time_decorator(func):
            def wrapper(*args, **kwargs):
                start_time = time()
                func_result = func(*args, **kwargs)
                end_time = time()
                time_interval = end_time - start_time

                Logger.log(f" Debug >>> {self.name} выполнялась {time_interval:2.3f} ms")

                return func_result

            return wrapper

        return time_decorator(cls)
