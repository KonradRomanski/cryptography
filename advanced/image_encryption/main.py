from DataReader import DataReader
from ImageCiphering import ImageCiphering
import numpy as np
import os

def main():
    # Init objects
    data = DataReader("sbox.SBX")
    # image = DataReader("img.png")
    image = DataReader("pikatchu.png")

    # Read data
    encryption_array = data.read_binary_data()
    print(encryption_array)


    key = os.urandom(32)  # 256-bit key

    sbox = np.arange(256)
    np.random.shuffle(sbox)
    image_ciphering = ImageCiphering(key)

    # Encrypt image using encryption array and save it
    encrypted_image = image.read_image()

    encrypted_image = image_ciphering.encrypt_image(encrypted_image)
    print("Image encrypted")

    data.save_image(np.array(encrypted_image, dtype=np.uint8), "pikatchu_en.png")

    # # Decrypt encrypted image and save it
    decrypted_image = image_ciphering.decrypt_image(encrypted_image)
    data.save_image(np.array(decrypted_image, dtype=np.uint8), "pikatchu_de.png")
    print("Image decrypted")


if __name__ == '__main__':
    main()
