frutas = 'banana castanha pequi caju umbu caqui amora'.split()

if __name__ == '__main__':
    def inverso(fruta):
        return ''.join(reversed(fruta))
    print(sorted(frutas, key=inverso))
    print(frutas)
