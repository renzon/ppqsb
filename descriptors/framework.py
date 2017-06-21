class _ModeloMeta(type):
    def __init__(self, cls_name, bases, propriedades):
        for nome, valor in propriedades.items():
            if hasattr(valor, 'set_nome'):
                valor.set_nome(nome)
        super().__init__(cls_name, bases, propriedades)


class Propriedade:
    def __init__(self):
        self._nome = None

    def __get__(self, item, owner):
        return getattr(item, self._nome)

    def __set__(self, item, valor):
        self.validar(valor)
        setattr(item, self._nome, valor)

    def validar(self, valor):
        raise NotImplementedError()

    def set_nome(self, nome):
        self._nome = f'_{nome}'


class Modelo(metaclass=_ModeloMeta):
    pass