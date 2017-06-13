import pytest


class Quantidade:
    def __init__(self):
        self.nome_do_alvo = None

    def set_nome_do_alvo(self, nome):
        self.nome_do_alvo = f'_{nome}'

    def __get__(self, instancia, classe):
        return getattr(instancia, self.nome_do_alvo)

    def __set__(self, instancia, valor):
        if valor <= 0:
            raise TypeError('Nao pode ter valor negativo')
        setattr(instancia, self.nome_do_alvo, valor)


class ItemPedido:
    preco = Quantidade()
    quantidade = Quantidade()

    def __new__(cls, *args, **kwargs):
        for nome, valor in cls.__dict__.items():
            if hasattr(valor, 'set_nome_do_alvo'):
                valor.set_nome_do_alvo(nome)
        return super().__new__(cls)

    def __init__(self, descricao, preco, quantidade):
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade

    def subtotal(self):
        return self.quantidade * self.preco


@pytest.fixture
def item():
    item = ItemPedido('Ervilha', 1.41, 2)
    return item


def teste_sucesso(item):
    assert 2.82 == pytest.approx(item.subtotal())


def teste_quantidade_negativa(item):
    with pytest.raises(TypeError):
        item.quantidade = -2


def teste_quantidade_negativa(item):
    with pytest.raises(TypeError):
        item.preco = -2


def teste_atributos(item):
    expected = set('descricao _preco _quantidade'.split())
    assert expected == set(item.__dict__.keys())
