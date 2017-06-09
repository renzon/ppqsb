import functools
from time import strftime


def logar(fmt):
    def decorator(func):
        @functools.wraps(func)
        def envoltoria(*args, **kwargs):
            agora = strftime(fmt)
            print(f'{agora} executado função {func.__name__}')
            return func(*args, **kwargs)

        return envoltoria

    return decorator


class logar:
    def __init__(self, fmt):
        self.fmt = fmt

    def __call__(self, func):
        @functools.wraps(func)
        def envoltoria(*args, **kwargs):
            agora = strftime(self.fmt)
            print(f'{agora} executado função {func.__name__}')
            return func(*args, **kwargs)

        return envoltoria


def ola_mundo():
    """Funcao olá mundo"""
    return 'Olá Mundo'


decorator = logar('%H:%M:%S')
ola_mundo = decorator(ola_mundo)


@logar('%H-%M-%S')
def hello(nome):
    return f'Hello {nome}'


if __name__ == '__main__':
    print(ola_mundo())
    print(ola_mundo.__name__)
    print(ola_mundo.__doc__)
    print(hello('Matheus'))
    print(hello.__name__)
