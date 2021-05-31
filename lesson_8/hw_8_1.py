from datetime import datetime


def time_log(f):
    def inner(*args, **kwargs):
        with open('test_file.txt', 'a', encoding='utf-8') as test_file:
            test_file.write(f'{datetime.now().strftime("%Y-%m-%d  %H:%M")} '
                            f'создан екземпляр класса {f.__name__} '
                            f'по адресу памяти {hex(id(f))}\n')
        return f(*args, **kwargs)
    return inner

@time_log
class SomeClass:

    def __init__(self, y):
        self.y = y
        print(self.y)


x = SomeClass(y='55')

