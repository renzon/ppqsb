class Propriedade:
    def __init__(self):
        self.nome_do_alvo = None

    def set_nome_do_alvo(self, nome):
        self.nome_do_alvo = f'_{nome}'

    def __get__(self, instancia, classe):
        return getattr(instancia, self.nome_do_alvo)

    def __set__(self, instancia, valor):
        self.validar(valor)
        setattr(instancia, self.nome_do_alvo, valor)

    def validar(self, valor):
        """Método abstrato que deve levantar exceção caso o valor seja
        inválido"""
        raise NotImplementedError()


class ModeloMeta(type):
    def __init__(cls, nome, bases, dic):
        super().__init__(nome, bases, dic)
        for nome, valor in dic.items():
            if hasattr(valor, 'set_nome_do_alvo'):
                valor.set_nome_do_alvo(nome)


class Modelo(metaclass=ModeloMeta):
    pass
