from itertools import cycle
from threading import Thread
from time import strftime, sleep


def log(msg):
    print(strftime('%H:%M:%S'), msg)


class Pedido:
    def __init__(self, nome, tempo_de_preparo):
        self.tempo_de_preparo = tempo_de_preparo
        self.nome = nome

    def preparar(self):
        log(f'Iniciando preparo de {self}')
        sleep(self.tempo_de_preparo)
        log(f'Finalizando preparo de {self}')

    def __call__(self):
        return self.preparar()

    def __str__(self):
        return self.nome


if __name__ == '__main__':
    nomes = cycle(['Camarão', 'Misto Quente'])
    nomes = (f'{nome} - {i}' for nome, i in zip(nomes, range(1, 3)))
    tempos = cycle([10, 3])
    pedidos = [Pedido(nome, tempo) for nome, tempo in zip(nomes, tempos)]
    threads = [Thread(target=p) for p in pedidos]

    for pedido, thread in zip(pedidos, threads):
        log(f'Pedido Anotado: {pedido}')
        thread.start()

    for thread in threads:
        log(f'Pedido Anotado: {pedido}')
        thread.join()

    log('Encerrando atendimeto')
