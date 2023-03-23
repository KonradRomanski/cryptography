import json


class DataReader:
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        with open(self.filename, 'r') as f:
            data = json.load(f)
        return data
