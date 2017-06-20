from exemplos.concorrencia.callback import loop


class Tarefa:
    def __init__(self, nome):
        self.nome = nome

    def __call__(self, *args, **kwargs):
        print(f'Executando {self.nome}')

if __name__ == '__main__':
    dez_segundos=Tarefa('10 segundos')
    cinco_segundos=Tarefa('5 segundos')
    loop.executar(10, dez_segundos)
    loop.executar(5, cinco_segundos)
    loop.iniciar()
