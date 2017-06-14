alterar = True


def criar_conta(saldo):
    def retirar(valor):
        global alterar
        nonlocal saldo
        alterar = False
        if valor >= saldo:
            raise ValueError('valor não pode ser maior que saldo')
        saldo -= valor
        return saldo

    def depositar(valor):
        nonlocal saldo
        saldo += valor
        return saldo

    return {'retirar': retirar, 'depositar': depositar}


if __name__ == '__main__':
    obj = criar_conta(400)
    print(obj['retirar'](250))
    print(obj['depositar'](250))
    print(obj['retirar'](300))
    print(alterar)
