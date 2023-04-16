import json
from PIL import Image
import numpy as np


class DataReader:
    def __init__(self, filename):
        self.filename = filename

    def read_image(self):
        image = Image.open(self.filename)
        image = image.convert("RGB")
        return np.array(image)

    def save_image(self, image, file_name):
        image_array = np.array(image)
        img = Image.fromarray(image_array)
        img.save(file_name)

    def read_binary_data(self):
        sbox_bytes = list()

        with open(self.filename, 'rb') as file:
            sbox = file.read()
            counter = 0
            for byte in sbox:
                if counter % 2 == 0:
                    sbox_bytes.append(byte)
                counter += 1
        return sbox_bytes

    def read_data(self):
        with open(self.filename, 'r') as f:
            data = json.load(f)
        return data
