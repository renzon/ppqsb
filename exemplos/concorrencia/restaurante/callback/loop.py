from time import time

_tarefas = []


def agendar(tempo, tarefa):
    inicio = time()
    _tarefas.append((inicio + tempo, tarefa))


def iniciar_loop():
    global _tarefas
    while _tarefas:
        tarefas_inacabadas = []
        for tempo_pronto, tarefa in _tarefas:
            if tempo_pronto >= time():
                tarefas_inacabadas.append((tempo_pronto, tarefa))
            else:
                tarefa()
        _tarefas = tarefas_inacabadas
