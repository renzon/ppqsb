import pytest


class ItemPedido:
    def __init__(self, descricao, preco, quantidade):
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade

    def subtotal(self):
        return self.quantidade * self.preco


def teste():
    item = ItemPedido('Ervilha', 1.41, 2)
    assert 2.82 == pytest.approx(item.subtotal())
    item.quantidade = -2
    assert -2.82 == pytest.approx(item.subtotal())
