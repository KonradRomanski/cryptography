import random
from PIL import Image
import numpy as np


class Visual_cryptography:

    def __init__(self, file_name=""):
        self.file_name = file_name
        self.image_array = self.load_as_array()

    def load_as_array(self):
        image = Image.open(self.file_name).convert('1')
        return np.array(image)

    def save_as_image(self, img_array, image_name, show=0):
        pil_img = Image.fromarray(img_array)
        if show:
            pil_img.show()
        pil_img.save(image_name)

    def split(self):
        img_1 = []
        img_2 = []
        for i in self.image_array:
            temp = []
            temp2 = []
            # print(rand_int)
            for j in i:
                rand_int = random.randint(0, 1)
                if j:
                    if rand_int:
                        temp.append(False)
                        temp.append(True)
                        temp2.append(False)
                        temp2.append(True)
                    else:
                        temp.append(True)
                        temp.append(False)
                        temp2.append(True)
                        temp2.append(False)

                else:
                    if rand_int:
                        temp.append(True)
                        temp.append(False)
                        temp2.append(False)
                        temp2.append(True)
                    else:
                        temp.append(False)
                        temp.append(True)
                        temp2.append(True)
                        temp2.append(False)

            img_1.append(temp)
            img_2.append(temp2)

        self.save_as_image(np.array(img_1), "img_1.png")
        self.save_as_image(np.array(img_2), "img_2.png")


    def run(self):
        # print(self.image_array)
        # print(sum(self.image_array))
        self.save_as_image(self.image_array, "default_image.png")
        self.split()


class Main:
    visual_cryptography = Visual_cryptography("image.png")
    visual_cryptography.run()


if __name__ == '__main__':
    Main()
