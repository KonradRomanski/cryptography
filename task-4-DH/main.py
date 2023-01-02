import random

from prime import Prime

class DiffyHelman:
    def __init__(self, n, g, x, y):
        self.n = n
        self.g = g
        self.x = x
        self.y = y
        self.A = self.get_A()
        self.B = self.get_B()
        self.Ka = self.get_Ka()
        self.Kb = self.get_Kb()

    def get_A(self):
        return pow(self.g, self.x, self.n)

    def get_B(self):
        return pow(self.g, self.y, self.n)

    def get_Ka(self):
        return pow(self.B, self.x, self.n)

    def get_Kb(self):
        return pow(self.A, self.y, self.n)

    def __str__(self):
        return f" n: {self.n} \n g: {self.g} \n x: {self.x} \n y: {self.y} \n A: {self.A} \n B: {self.B} \n Ka: {self.Ka} \n Kb: {self.Kb}"


def main():
    # n = Prime(12345, 123456).get_prime()
    n = 1009
    g = 798
    x = random.randint(100, 1000)
    y = random.randint(100, 10000)
    diffy_helman = DiffyHelman(n, g, x, y)
    print(diffy_helman)


if __name__ == '__main__':
    main()
