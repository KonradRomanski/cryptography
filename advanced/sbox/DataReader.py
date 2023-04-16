import json
import random

from PIL import Image
import numpy as np


class DataReader:
    def read_image(self, filename):
        image = Image.open(filename)
        image = image.convert("RGB")
        return np.array(image)

    def save_image(self, image, filename):
        image_array = np.array(image)
        img = Image.fromarray(image_array)
        img.save(filename)

    def read_binary_data(self, filename):
        sbox_bytes = list()

        with open(filename, 'rb') as file:
            sbox = file.read()
            counter = 0
            for byte in sbox:
                if counter % 2 == 0:
                    sbox_bytes.append(byte)
                counter += 1
        return sbox_bytes

    def transform_function_2_number_array(self, data):
        sbox_bytes = list()
        arr = "".join([i for i in data.values()])
        binary_list = [arr[i:i + 8] for i in range(0, len(arr), 8)]
        decimal_list = [int(binary, 2) for binary in binary_list]
        return decimal_list

    def read_json(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        return data
