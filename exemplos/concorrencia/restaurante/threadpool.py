from concurrent.futures import as_completed
from concurrent.futures.thread import ThreadPoolExecutor
from itertools import cycle
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
        return self.nome

    def __call__(self):
        return self.preparar()

    def __str__(self):
        return self.nome


if __name__ == '__main__':
    nomes = cycle(['Camarão', 'Misto Quente'])
    nomes = (f'{nome} - {i}' for nome, i in zip(nomes, range(1, 4000)))
    tempos = cycle([10, 3])
    pedidos = [Pedido(nome, tempo) for nome, tempo in zip(nomes, tempos)]
    with ThreadPoolExecutor(max_workers=1000) as executor:
        futures = []
        for p in pedidos:
            log(f'Anotando {p}')
            futures.append(executor.submit(p))
        for future in as_completed(futures):
            print(future.result())
    log('Encerrando atendimeto')
