import pytest


def fatorial(n):
    produto = 1
    for i in range(2, n + 1):
        produto *= i
    return produto


@pytest.mark.parametrize('n,esperado', [
    (-1, 1),
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (5, 120),
])
def test_fatorial(n, esperado):
    assert esperado == fatorial(n)


fat = fatorial


def test_atribuicao_de_funcao():
    assert 120 == fat(5)
    assert fat is fatorial
    assert 'fatorial' is fat.__name__
    assert callable(fat)


if __name__ == '__main__':
    print('test')
