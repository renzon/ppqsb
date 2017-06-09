class Singleton:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance


# SINGLETON = _Singleton()



class Invocavel:
    def __init__(self, numero):
        self.numero = numero

    def __call__(self):
        return self.numero


if __name__ == '__main__':
    invocaveis = map(Invocavel, range(1, 3))

    for invocavel in invocaveis:
        print(invocavel())

    singleton_1 = Singleton()
    singleton_2 = Singleton()
    print(id(singleton_1), id(singleton_2))
    print(singleton_1 is singleton_2)
