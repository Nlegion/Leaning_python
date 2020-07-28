# iterable vs iterator

class MyIterator:
    def __init__(self, n):
        self._cnt = n
        self._idx = 0

    def __next__(self):  # iterable
        if self._idx < self._cnt:
            self._idx += 1
            return self._idx - 1
        raise StopIteration

    def __iter__(self):  # iterator
        return self


a = MyIterator(5)
print('out', next(a))
print('out', next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

b = iter(a)
print(f'b: {next(b)}')

for el in a:
    print(el)
