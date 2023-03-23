import math

from prime import Prime


class RSA:
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.n = p * q
        self.phi = (p - 1) * (q - 1)
        self.e = 0
        self.d = 0
        self.public_key = (self.e, self.n)
        self.private_key = (self.d, self.n)
        self.generate_keys()

    def generate_keys(self):
        self.e = self.get_coprime()
        self.d = self.get_d()
        self.public_key = (self.e, self.n)
        self.private_key = (self.d, self.n)

    def get_coprime(self):
        while True:
            prime = Prime(2, self.phi).get_random_prime()
            if math.gcd(prime, self.phi) == 1:
                return prime

    def encrypt(self, message):
        return pow(message, self.e, self.n)

    def decrypt(self, message):
        return pow(message, self.d, self.n)

    def get_public_key(self):
        return self.public_key

    # def set_public_key(self, public_key):
    #     self.public_key = public_key
    #     self.generate_keys()

    def get_private_key(self):
        return self.private_key

    # def set_private_key(self, private_key):
    #     self.private_key = private_key
    #     self.generate_keys()

    def get_d(self):
        for i in range(1, 10000000000):
            if (i * self.e) % self.phi == 1:
                return i
        return 0

    # def set_d(self, d):
    #     self.d = d
    #     self.generate_keys()

    # def get_n(self):
    #     return self.n

    # def set_n(self, n):
    #     self.n = n
    #     self.generate_keys()

    # def get_e(self):
    #     return self.e

    # def set_e(self, e):
    #     self.e = e
    #     self.generate_keys()

    # def get_p(self):
    #     return self.p

    # def set_p(self, p):
    #     self.p = p
    #     self.n = p * self.q
    #     self.phi = (p - 1) * (self.q - 1)
    #     self.generate_keys()

    # def get_q(self):
    #     return self.q

    # def set_q(self, q):
    #     self.q = q
    #     self.n = self.p * q
    #     self.phi = (self.p - 1) * (q - 1)
    #     self.generate_keys()

    # def get_phi(self):
    #     return self.phi

    # def set_phi(self, phi):
    #     self.phi = phi
    #     self.generate_keys()

    def __str__(self):
        return "p: " + str(self.p) + " " \
               "q: " + str(self.q) + "\n" \
               "n: " + str(self.n) + " " \
               "phi: " + str(self.phi) + "\n" \
               "e: " + str(self.e) + " " \
               "d: " + str(self.d) + "\n"

    def __repr__(self):
        return self.__str__()
