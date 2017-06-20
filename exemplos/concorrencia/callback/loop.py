from time import time


class _Tarefa:
    def __init__(self, segundos, invocavel):
        self.invocavel = invocavel
        self.segundos = time() + segundos

    def __call__(self, *args, **kwargs):
        if self.segundos <= time():
            self.invocavel()
            return True

        return False


_tarefas = []


def executar(segundos, invocavel):
    _tarefas.append(_Tarefa(segundos, invocavel))


def iniciar():
    global _tarefas
    print('Iniciando', time())
    while _tarefas:
        _tarefas_pendentes = []
        for t in _tarefas:
            if not t():
                _tarefas_pendentes.append(t)
            else:
                print(time())
        _tarefas = _tarefas_pendentes
    print('Finalizando', time())
