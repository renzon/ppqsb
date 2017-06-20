from exemplos.concorrencia.callback import loop


class Task:
    def __init__(self, nome):
        self.nome = nome

    def __call__(self, *args, **kwargs):
        print(f'Executando {self.nome}')

if __name__ == '__main__':
    dez_segundos=Task('10 segundos')
    cinco_segundos=Task('5 segundos')
    loop.executar(10, dez_segundos)
    loop.executar(5, cinco_segundos)
    loop.iniciar()
