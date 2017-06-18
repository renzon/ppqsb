"""
O Micro framework Flask faz uso de decorator para definir suas rotas:

http://flask.pocoo.org/

O objetivo desse exercício é construir uma versão simplificada desse sistema
   de rotas.

"""
import pytest

from exercicios.flask.app import rota, rotear, RotaInexistente


@rota('/usuario')
def usuario(nome):
    return f'salvando {nome}'


@rota('/carro')
def carro(nome, ano):
    return f'{nome} ano {ano}'


def test_execucao_sem_parametro():
    """Testa se home é executado através da função rotear depois de mapeado
    para o path '/' """

    @rota('/')
    def home():
        return 'home executada'

    assert home() == rotear('/') == 'home executada'


def test_execucao_com_parametro_posicional():
    assert usuario('Renzo') == rotear('/usuario', 'Renzo') == 'salvando Renzo'


def test_execucao_com_parametro_nomeado():
    assert usuario('Foo') == rotear('/usuario', nome='Foo') == 'salvando Foo'


def test_execucao_com_parametros_posicionais():
    assert carro('Fusca', 88) == rotear(
        '/carro', 'Fusca', 88) == 'Fusca ano 88'


def test_execucao_com_parametros_nomeados():
    assert carro('Gol', 2000) == rotear(
        '/carro', ano=2000, nome='Gol') == 'Gol ano 2000'


def test_execucao_com_parametro_posicional_e_nomeado():
    assert carro('Celta', 99) == rotear(
        '/carro', 'Celta', 99) == 'Celta ano 99'


def test_parametros_errados():
    with pytest.raises(TypeError):
        rotear('/carro')


def test_rota_inexistente():
    with pytest.raises(RotaInexistente) as excinfo:
        rotear('/inexistente')

    assert str(excinfo.value) == 'Rota inexistente: /inexistente'
