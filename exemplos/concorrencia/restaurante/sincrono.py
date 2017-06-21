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

    def __str__(self):
        return self.nome


if __name__ == '__main__':
    camarao = Pedido('Camarão', 10)
    log(f'Pedido Anotado: {camarao}')
    camarao.preparar()
    misto = Pedido('Misto Quente', 3)
    log(f'Pedido Anotado: {misto}')
    misto.preparar()
    log('Encerrando atendimeto')
