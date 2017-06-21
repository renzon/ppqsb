import pytest

from descriptors.framework import Propriedade, Modelo


class Quantidade(Propriedade):
    def validar(self, valor):
        if valor <= 0:
            raise TypeError('Quantidade deveria ser positiva')


class ItemPedido(Modelo):
    quantidade = Quantidade()
    preco = Quantidade()

    def __init__(self, descricao, preco, quantidade):
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade

    def subtotal(self):
        return self.preco * self.quantidade


def test_subtotal():
    item = ItemPedido('Ervilha', 1.21, 2)
    assert pytest.approx(2.42, item.subtotal())


def test_set_quantidade_negativa():
    item = ItemPedido('Ervilha', 1.21, 2)
    with pytest.raises(TypeError):
        item.quantidade = -2


def test_set_quantidade_negativa_no_init():
    with pytest.raises(TypeError):
        ItemPedido('Ervilha', 1.21, -2)


def test_set_preco_negativo():
    item = ItemPedido('Ervilha', 1.21, 2)
    with pytest.raises(TypeError):
        item.preco = -1.21


def test_set_preco_negativo_no_init():
    with pytest.raises(TypeError):
        ItemPedido('Ervilha', -1.21, 2)


def test_propriedade_de_descriptor():
    item = ItemPedido('Ervilha', 1.21, 2)
    assert {'descricao': 'Ervilha', '_preco': 1.21,
            '_quantidade': 2} == item.__dict__
