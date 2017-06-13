from itertools import count
from time import time

import matplotlib as mpl

mpl.use('TkAgg')

from matplotlib import pyplot

from descritores import s1, s2, s3, s4, s5, s6, s7


def create_instances_in_one_second(cls):
    initial = time()
    for i in count(1):
        cls('Ervilha', 1.41, 2)
        if (time() - initial) >= 1:
            break

    return i


versoes_item_pedido = (s.ItemPedido for s in (s1, s2, s3, s4, s5, s6, s7))
tempos = list(map(create_instances_in_one_second, versoes_item_pedido))
_, ax = pyplot.subplots()
pyplot.title('Criação de Objs ItemPedido')
pyplot.ylabel('Número de objetos criados em 1 segundo')
pyplot.xlabel('Versões de ItemPedido')
x_values = list(range(1, 8))
pyplot.bar(x_values, tempos)
for x, tempo in zip(x_values, tempos):
    ax.text(x - 0.4, tempo + 12000, str(tempo), color='black', fontweight='bold')
pyplot.grid(True, axis='y')
pyplot.show()
