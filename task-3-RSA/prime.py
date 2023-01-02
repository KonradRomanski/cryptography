import random


class Prime:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.prime = self.get_prime()
        self.random_prime = self.get_random_prime()

    def get_random_prime(self):
        while True:
            n = random.randint(self.start, self.end)
            if self.is_prime(n):
                return n

    def get_prime(self):
        for i in range(self.start, self.end):
            if self.is_prime(i):
                return i
        return 0

    def is_prime(self, n):
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 2, 2):
            if n % i == 0:
                return False
        return True
