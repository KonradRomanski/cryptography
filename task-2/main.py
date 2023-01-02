from PIL import Image
import numpy as np
import random

class HideData:
    def __init__(self, secret_data, file_name=""):
        self.secret = secret_data
        self.file_name = file_name
        self.data_location_list = []
        self.data_location_list_flatten = []

    def load_and_run(self):
        image = Image.open(self.file_name)
        image = image.convert("RGB")
        # return image.tobytes()
        arr = np.array(image)
        print("SIZE", len(arr) * len(arr[0]))
        print("LENGTH", len(self.secret) * 8/3)

        self.save_bit(self.secret, arr)
        pil_img = Image.fromarray(arr, 'RGB')
        pil_img.save("img_out.png")
        print("location list: ", self.data_location_list)
        print("location list flatten: ", sorted(self.data_location_list_flatten))
        print(len(self.data_location_list_flatten))
        self.read_secret(arr)


    def save_bit(self, secret, img_array):
        print(secret)
        binary = self.text_to_binary(secret)
        while len(binary)%3 != 0:
            binary = "0" + binary
        print(binary)
        for i in range(0, len(binary) - 2, 3):
            rand = self.get_random_coordinates(img_array)
            self.data_location_list.append(rand)
            self.data_location_list_flatten.append(rand[0])
            self.data_location_list_flatten.append(rand[1])
            print(i, img_array[rand[0]][rand[1]])
            img_array[rand[0]][rand[1]][0] = self.add_bit_to_array(binary[i], img_array[rand[0]][rand[1]][0])
            img_array[rand[0]][rand[1]][1] = self.add_bit_to_array(binary[i+1], img_array[rand[0]][rand[1]][1])
            img_array[rand[0]][rand[1]][2] = self.add_bit_to_array(binary[i+2], img_array[rand[0]][rand[1]][2])


    def bin_to_num(self, to_transform=''):
        return int(to_transform, 2)

    def add_bit_to_array(self, bit, cell):
        if bit == "1":
            if cell % 2 == 0:
                cell += 1
        else:
            if cell % 2 == 1:
                cell -= 1
        print(cell)
        return cell

    def read_secret(self, img_array):
        secret = ""
        for i in self.data_location_list:
            secret += str(img_array[i[0]][i[1]][0]%2)
            secret += str(img_array[i[0]][i[1]][1]%2)
            secret += str(img_array[i[0]][i[1]][2]%2)
        while secret[-1] == "0" and len(secret) % 8 != 0:
            secret = secret[1:]
        print("binary secret: ", secret)
        print("secret: ", self.binary_to_text(secret))


    def get_random_coordinates(self, img_array):
        result = [0, 0]
        while 6 > img_array[result[0]][result[1]][0] > 250 \
               or 6 > img_array[result[0]][result[1]][1] > 250 \
               or 6 > img_array[result[0]][result[1]][2] > 250 \
                or result[0] in self.data_location_list_flatten \
                or result[1] in self.data_location_list_flatten \
                or result[0] == 0 \
                or result[1] == 0:
            result = [random.randint(1, len(img_array) - 1), random.randint(1, len(img_array[0]) - 1)]
        return result


    def text_to_binary(self, text):
        return "".join(f"{ord(i):08b}" for i in text)


    def binary_to_text(self, binary):
        n = int(binary, 2)
        return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()


def main():
    to_hide = "Lorem ipsum dolor sit amet, consectetur aaa "
    data = HideData(to_hide, 'image.png')
    data.load_and_run()


if __name__ == '__main__':
    main()
