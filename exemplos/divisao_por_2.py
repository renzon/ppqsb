import functools
import operator


def divisao_por_2(n):
    return n // 2


def divisao_por_2(n):
    return operator.floordiv(n, 2)


def criador_de_divisao(funcao, quociente):
    def f(n):
        return funcao(n, quociente)

    return f


divisao_por_2 = criador_de_divisao(operator.floordiv, 2)


def test_divisao():
    assert 5 == divisao_por_2(10)


def f(a, b):
    return a, b


def test_parcial():
    atalho = functools.partial(f,1, b=2)
    assert (1, 2) == atalho()
    assert (1, 3) == atalho()
    assert (1, 4) == atalho()
