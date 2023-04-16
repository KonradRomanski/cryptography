import json


class NL:
    def __init__(self, functions_json_file, sbox_file, mode):
        self.mode = mode
        self.functions_json_file = functions_json_file
        self.sbox_file = sbox_file
        if mode == "bin":
            self.bin_file = open('sbox.sbx', 'rb')

    # Calculate the Hamming distance between two binary strings
    def calculate_hamming_distance(self, foo, bar):
        baz = list(map(
            lambda el: 0 if el[0] == el[1] else 1,
            zip(foo, bar)
        ))
        return sum(baz)

    # Analyze the 'sbox.sbx' file and compute the VULTR score for each function
    def analyze_sbox(self):
        arr = []
        fns = []
        if self.mode == "bin":
            # Get the size of the file in bytes
            size = self.bin_file.seek(0, 2)
            # Move the file pointer to the beginning of the file
            self.bin_file.seek(0, 0)
            # Loop over the bytes in the file in pairs
            for i in range(size // 2):
                # Read two bytes from the file and convert them to an integer
                word = self.bin_file.read(2)
                num = int.from_bytes(word, byteorder='big')
                # Convert the integer to an 8-bit binary string
                bin_str = bin(num)[2:].zfill(8)
                # Split the binary string into a list of characters and append it to the 'arr' list
                arr.append(list(bin_str))

                # Print the index of the byte pair, the byte pair as a hexadecimal string, and the binary string
                # print(i, hex(num), bin_str)
            # Close the file
            self.bin_file.close()
            # Transpose the 'arr' list and join the characters of each sublist to form a list of binary strings representing each function
            fns = [''.join(sublist) for sublist in zip(*arr)]
        else:
            fns = [i for i in self.sbox_file.values()]
        # print("fns: ", fns)
        # Calculate the VULTR score for each function
        vult = [min([self.calculate_hamming_distance(fn, self.functions_json_file[d]) for d in self.functions_json_file.keys()]) for fn in fns]
        # print("vult: ", vult)
        return min(vult)
