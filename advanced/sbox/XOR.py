class SBoxAnalyzer:
    def __init__(self, sbox):
        self.sbox = sbox
        self.profile = self._compute_profile()

    def _compute_profile(self):
        # Create an array of all possible arguments (0-255)
        all_args = [index for index in range(256)]
        # Create an array of all possible argument pairs, excluding identical pairs
        all_pairs = [(foo, bar) for foo in all_args for bar in all_args if bar != foo]
        # Create a 256x256 array to hold the profile (initialized to all 0s)
        profile = [[0 for _ in range(256)] for _ in range(256)]

        for foo_x, bar_x in all_pairs:
            # Get the output values for the input arguments
            foo_y = self.sbox[foo_x]
            bar_y = self.sbox[bar_x]

            # Compute the XOR of the input and output arguments
            xor_x = foo_x ^ bar_x
            xor_y = foo_y ^ bar_y

            # Increment the profile at the location corresponding to the XOR of the input and output arguments
            profile[xor_x][xor_y] += 1

        return profile

    def get_max_probability(self):
        # Find the maximum probability by finding the maximum value in the profile
        max_prob = max([max(row) for row in self.profile])
        return max_prob
