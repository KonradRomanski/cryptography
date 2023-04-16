import json
import random
import matplotlib.pyplot as plt
from DataReader import DataReader
from NL import NL
from SAC import SAC
from XOR import SBoxAnalyzer


class TestsRunner:
    def __init__(self):
        self.data_reader = DataReader()

    def count_cycles(self, sbox):
        n = len(sbox)
        visited = [False] * n
        cycles = 0
        for i in range(n):
            if not visited[i]:
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = sbox[j]
                if j == i:
                    cycles += 1
        return cycles

    def multiple_run(self, file_name, output_file=None):
        file_json = self.data_reader.read_json(file_name)
        arr = [self.run(i) for i in file_json]
        if output_file:
            with open(output_file, 'w') as f:
                json.dump(arr, f)
        return arr


    def run(self, data):
        xor_data = self.data_reader.transform_function_2_number_array(data)
        # print(self.count_cycles(xor_data), xor_data)
        nl = NL(self.data_reader.read_json('functions.json'), data, "json")
        sac = SAC(data)
        analyzer = SBoxAnalyzer(xor_data)

        return [nl.analyze_sbox(), sac.run_example(), analyzer.get_max_probability(), self.count_cycles(xor_data)]


    def one_run(self, file_name):
        file_json = self.data_reader.read_json(file_name)
        return self.run(file_json)

    def generate_binary_string(self, num_digits):
        return ''.join([str(random.randint(0, 1)) for j in range(num_digits)])

    def generate_data(self, num_entries, num_digits):
        return {str(i): self.generate_binary_string(num_digits) for i in range(num_entries)}

    def write_data_to_file(self, data, file_name):
        with open(file_name, 'w') as f:
            json.dump(data, f, indent=2)

    def generate_single_data_file(self, file_name, num_entries, num_digits):
        data = self.generate_data(num_entries, num_digits)
        self.write_data_to_file(data, file_name)

    def generate_multiple_data_files(self, file_name, num_entries, num_digits, num_duplications):
        data = [self.generate_data(num_entries, num_digits) for _ in range(num_duplications)]
        self.write_data_to_file(data, file_name)

    def draw_results_chart(self, filename, nested=False, sort_col=0):
        with open(filename, 'r') as f:
            results = json.load(f)

        # Sort the results by NL value
        sorted_results = sorted(results, key=lambda x: x[sort_col])

        # Extract the NL values and the corresponding SAC and XOR values into separate lists
        nl_values = [result[0] for result in sorted_results]
        sac_values = [result[1] for result in sorted_results]
        xor_values = [result[2] for result in sorted_results]
        cycle_values = [result[3] for result in sorted_results]

        if sort_col == -1:
            nl_values.sort()
            sac_values.sort()
            xor_values.sort()
            cycle_values.sort()

        # Define the colors for the lines
        nl_color = 'tab:blue'
        sac_color = 'tab:orange'
        xor_color = 'tab:green'
        cycle_color = 'tab:red'

        if nested:
            # Plot the data as four separate subplots
            fig, axs = plt.subplots(4, 1, sharex=True, squeeze=True)
            ax1, ax2, ax3, ax4 = axs[0], axs[1], axs[2], axs[3]

            fig.set_size_inches(6, 12)
            ax1.plot(nl_values, color=nl_color)
            ax1.set_ylabel('NL')
            ax2.plot(sac_values, color=sac_color)
            ax2.set_ylabel('SAC')
            ax3.plot(xor_values, color=xor_color)
            ax3.set_ylabel('XOR')
            ax4.plot(cycle_values, color=cycle_color)
            ax4.set_ylabel('Cycles')
            ax4.set_xlabel('Result Index')
            fig.suptitle('Results')
        else:
            # Plot the data as a line chart with four datasets
            fig, ax = plt.subplots()
            fig.set_size_inches(6, 6)
            ax.plot(nl_values, color=nl_color, label='NL')
            ax.plot(sac_values, color=sac_color, label='SAC')
            ax.plot(xor_values, color=xor_color, label='XOR')
            ax.plot(cycle_values, color=cycle_color, label='CYCLE')
            ax.set_xlabel('Result Index')
            ax.set_ylabel('Value')
            ax.set_title('Results')
            ax.legend()

        plt.show()
