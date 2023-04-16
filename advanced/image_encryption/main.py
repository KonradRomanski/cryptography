from DataReader import DataReader
from ImageCiphering import ImageCiphering
import numpy as np


def main():
    # Init objects
    data = DataReader("sbox.SBX")
    # image = DataReader("img.png")
    image = DataReader("pikatchu.png")
    image_ciphering = ImageCiphering()

    # Read data
    encryption_array = data.read_binary_data()

    # Encrypt image using encryption array and save it
    encrypted_image = image.read_image()
    # encrypted_image = image_ciphering.multiple_rounds_encryption(encrypted_image, encryption_array)
    encrypted_image = image_ciphering.encrypt_image(encrypted_image, encryption_array)
    print("Image encrypted")
    # for i in range(5):
    #     encrypted_image = image_ciphering.encrypt_image(encrypted_image, encryption_array)
    #     encryption_array = [int((i + 2)/2) for i in encryption_array]
    # data.save_image(encrypted_image, "encrypted_img.png")
    data.save_image(np.array(encrypted_image, dtype=np.uint8), "pikatchu_en.png")

    # # Decrypt encrypted image and save it
    decrypted_image = image_ciphering.decrypt_image(encrypted_image, encryption_array)
    data.save_image(np.array(decrypted_image, dtype=np.uint8), "pikatchu_de.png")
    print("Image decrypted")


if __name__ == '__main__':
    main()
