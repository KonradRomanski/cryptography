import numpy as np
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


class ImageCiphering:
    def __init__(self, key):
        self.key = key

    def encrypt_image(self, image):
        nrows, ncols, nchannels = image.shape
        padded_image = np.pad(image, [(0, nrows % 16), (0, ncols % 16), (0, 0)], mode='edge')
        flattened_image = padded_image.flatten()

        # Encrypt the data using AES
        cipher = Cipher(algorithms.AES(self.key), modes.ECB(), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted_data = encryptor.update(flattened_image) + encryptor.finalize()

        # Reshape the encrypted data to match the padded image
        encrypted_image = np.frombuffer(encrypted_data, dtype=np.uint8).reshape(padded_image.shape)

        return encrypted_image

    def decrypt_image(self, encrypted_image):
        nrows, ncols, nchannels = encrypted_image.shape
        flattened_image = encrypted_image.flatten()

        # Decrypt the data using AES
        cipher = Cipher(algorithms.AES(self.key), modes.ECB(), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(flattened_image) + decryptor.finalize()

        # Remove padding and reshape the decrypted data to match the original image
        decrypted_data = decrypted_data[:nrows * ncols * nchannels]
        decrypted_image = np.frombuffer(decrypted_data, dtype=np.uint8).reshape((nrows, ncols, nchannels))

        return decrypted_image

