class JQuery:
    def __init__(self):
        self.funcao = None

    def ready(self, funcao):
        self.funcao = funcao

    def pagina_pronta(self):
        print('pagina pronta')
        if self.funcao is not None:
            self.funcao()


jquery = JQuery()


def ola_mundo():
    print('Olá Mundo')


jquery.ready(ola_mundo)

if __name__ == '__main__':
    print('Main')
    jquery.pagina_pronta()
