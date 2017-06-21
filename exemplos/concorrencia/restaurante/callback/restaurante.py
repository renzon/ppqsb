from itertools import cycle
from time import strftime

from exemplos.concorrencia.restaurante.callback import loop


def log(msg):
    print(strftime('%H:%M:%S'), msg)


class Pedido:
    def __init__(self, nome, tempo_de_preparo):
        self.tempo_de_preparo = tempo_de_preparo
        self.nome = nome

    def preparar(self):
        log(f'Finalizando preparo de {self}')

    def __call__(self):
        return self.preparar()

    def __str__(self):
        return self.nome


if __name__ == '__main__':
    nomes = cycle(['Camarão', 'Misto Quente'])
    nomes = (f'{nome} - {i}' for nome, i in zip(nomes, range(1, 5000)))
    tempos = cycle([10, 3])
    pedidos = [Pedido(nome, tempo) for nome, tempo in zip(nomes, tempos)]

    for pedido in pedidos:
        log(f'Pedido Anotado: {pedido}')
        log(f'Iniciando preparo de {pedido}')
        loop.agendar(pedido.tempo_de_preparo, pedido)

    loop.iniciar_loop()

    log('Encerrando atendimeto')
