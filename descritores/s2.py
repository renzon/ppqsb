import pytest


class ItemPedido:
    def __init__(self, descricao, preco, quantidade):
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade

    def subtotal(self):
        return self.quantidade * self.preco

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, valor):
        if valor <= 0:
            raise TypeError('Não pode ser negativo')
        self._quantidade = valor

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor <= 0:
            raise TypeError('Não pode ser negativo')
        self._preco = valor


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
