from DataReader import DataReader
from SAC import SBox


def main():
    data_reader = DataReader('sbox.json')
    data = data_reader.read_data()
    s = SBox(data)
    s.run_example()


if __name__ == '__main__':
    main()
