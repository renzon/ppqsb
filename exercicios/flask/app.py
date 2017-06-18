class RotaInexistente(Exception):
    pass


_rotas = {}


def rota(path):
    def decorator(func):
        _rotas[path] = func
        return func

    return decorator


def rotear(path, *args, **kwargs):
    return _rotas[path](*args, **kwargs)
