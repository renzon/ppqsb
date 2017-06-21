import asyncio
from itertools import cycle
from time import strftime


def log(msg):
    print(strftime('%H:%M:%S'), msg)


class Pedido:
    def __init__(self, nome, tempo_de_preparo):
        self.tempo_de_preparo = tempo_de_preparo
        self.nome = nome

    async def preparar(self):
        log(f'Iniciando preparo de {self}')
        await asyncio.sleep(self.tempo_de_preparo)
        log(f'Finalizando preparo de {self}')
        return self.nome

    async def __call__(self):
        result = await self.preparar()
        return result

    def __str__(self):
        return self.nome


def main():
    global nome, i
    nomes = cycle(['Camarão', 'Misto Quente'])
    nomes = (f'{nome} - {i}' for nome, i in zip(nomes, range(1, 3)))
    tempos = cycle([10, 3])
    pedidos = [Pedido(nome, tempo) for nome, tempo in zip(nomes, tempos)]
    esperaveis = (pedido.preparar() for pedido in pedidos)
    loop = asyncio.get_event_loop()
    futures = asyncio.gather(*esperaveis)
    loop.run_until_complete(futures)
    # for r in futures.result():
    #     print(r)
    loop.close()
    log('Encerrando atendimeto')


if __name__ == '__main__':
    print(main())
