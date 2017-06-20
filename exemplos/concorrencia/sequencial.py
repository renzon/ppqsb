from time import time, sleep


class Tarefa:
    def __init__(self, segundos):
        self.segundos = segundos

    def __call__(self, *args, **kwargs):
        print(f'Iniciando {self.segundos}', time())
        sleep(self.segundos)
        print(f'Finalizando Thread {self.segundos}', time())

if __name__ == '__main__':
    tarefas = (Tarefa(10), Tarefa(5))
    for t in tarefas:
        t()