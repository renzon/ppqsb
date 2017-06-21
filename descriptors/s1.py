import pytest


class ItemPedido:
    def __init__(self, descricao, preco, quantidade):
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade

    def subtotal(self):
        return self.preco * self.quantidade


def test_subtotal():
    item = ItemPedido('Ervilha', 1.21, 2)
    assert pytest.approx(2.42, item.subtotal())


def test_subtotal_negativo():
    item = ItemPedido('Ervilha', 1.21, -2)
    assert pytest.approx(-2.42, item.subtotal())
