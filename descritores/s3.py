import pytest


class NumeroPositivo:
    def __init__(self):
        self.nome_do_alvo = '_{}'.format(id(self))

    def __get__(self, instancia, classe):
        return getattr(instancia, self.nome_do_alvo)

    def __set__(self, instancia, classe):
        if classe <= 0:
            raise TypeError('Nao pode ter valor negativo')
        setattr(instancia, self.nome_do_alvo, classe)


class ItemPedido:
    preco = NumeroPositivo()
    quantidade = NumeroPositivo()

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
