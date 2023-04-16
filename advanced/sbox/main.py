from TestsRunner import TestsRunner
from DataReader import DataReader
from NL import NL
from SAC import SAC
from XOR import SBoxAnalyzer


def main():
    data_reader = DataReader()
    tests_runner = TestsRunner()

    # Generate files
    # tests_runner.generate_single_data_file("data.json", num_entries=8, num_digits=256)
    tests_runner.generate_multiple_data_files("data_more.json", num_entries=8, num_digits=256, num_duplications=100)

    # Run one test
    # file_json = data_reader.read_json('sbox.json')
    # print(tests_runner.one_run('sbox.json'))
    # print(tests_runner.one_run('data.json'))
    print(tests_runner.multiple_run('data_more.json', "data_output.json"))
    tests_runner.draw_results_chart("data_output.json", nested=True, sort_col=-1)
    # # NL
    # # nl = NL(data_reader.read_json('functions.json'), data_reader.read_binary_data('./sbox.sbx'), "bin")
    # nl = NL(data_reader.read_json('functions.json'), file_json, "json")
    # # print("NL")
    # print("NL: ", nl.analyze_sbox())
    #
    # # SAC
    # # print("SAC")
    # sac = SAC(file_json)
    # print("SAC:", sac.run_example())
    #
    # # XOR
    # # print("XOR")
    # data = data_reader.transform_function_2_number_array(file_json)
    # # data = data_reader.read_binary_data('./sbox.sbx')
    # analyzer = SBoxAnalyzer(data)
    # max_prob = analyzer.get_max_probability()
    # # print(f"Maximum probability: {max_prob}")
    # print(f"XOR: {max_prob}")


if __name__ == '__main__':
    main()
