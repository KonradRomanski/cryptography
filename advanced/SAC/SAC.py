import numpy as np


class SBox:
    def __init__(self, data_file):
        self.sbox_data = data_file
        self.l = [2 ** i for i in range(8)]
        self.final_tab = []

    def sac(self, alfa, function):
        f = self.sbox_data.get(function)
        g = lambda x: f[alfa ^ x]
        return sum([int(f[index]) ^ int(g(index)) for index in range(len(f))])

    def sac_all_lambda(self, function):
        return [self.sac(i, function) for i in self.l]

    def sac_all_functions(self):
        self.final_tab = [self.sac_all_lambda(i) for i in self.sbox_data.keys()]

    def mean(self):
        result = np.mean(self.final_tab) / 256
        return result

    def get_final_tab(self):
        return self.final_tab

    def run_example(self):
        self.sac_all_functions()
        print(self.mean())
        print(self.get_final_tab())

