import pytest

from descritores.framework import Propriedade, Modelo


class Quantidade(Propriedade):
    def validar(self, valor):
        if valor <= 0:
            raise TypeError('Nao pode ter valor negativo')


class ItemPedido(Modelo):
    preco = Quantidade()
    quantidade = Quantidade()

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
