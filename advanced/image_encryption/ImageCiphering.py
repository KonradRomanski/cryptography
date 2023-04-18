import numpy as np
import pickle
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


class ImageCiphering:
    def __init__(self, key):
        self.key = key

    def encrypt_image(self, image):
        nrows, ncols, nchannels = image.shape
        pad_rows = int(np.ceil(nrows / 16.0) * 16) - nrows
        pad_cols = int(np.ceil(ncols / 16.0) * 16) - ncols
        padded_image = np.pad(image, [(0, pad_rows), (0, pad_cols), (0, 0)], mode='edge')
        flattened_image = padded_image.flatten()

        # Shuffle the pixels
        permutation = np.random.permutation(len(flattened_image))
        shuffled_image = flattened_image[permutation]

        # Encrypt the shuffled data using AES
        cipher = Cipher(algorithms.AES(self.key), modes.ECB(), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted_data = encryptor.update(shuffled_image) + encryptor.finalize()

        # Reshape the encrypted data to match the padded image
        encrypted_image = np.frombuffer(encrypted_data, dtype=np.uint8).reshape(padded_image.shape)

        # Serialize the permutation and padded image shape for decryption
        permutation_list = permutation.tolist()
        self.permutation_data = pickle.dumps((permutation_list, padded_image.shape))

        return encrypted_image

    def decrypt_image(self, encrypted_image):
        # Deserialize the permutation and padded image shape
        permutation_list, padded_image_shape = pickle.loads(self.permutation_data)

        # Decrypt the shuffled data using AES
        cipher = Cipher(algorithms.AES(self.key), modes.ECB(), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(encrypted_image.flatten()) + decryptor.finalize()

        # Unshuffle the pixels
        unshuffled_data = np.zeros(len(permutation_list), dtype=np.uint8)
        for i, j in enumerate(permutation_list):
            unshuffled_data[j] = decrypted_data[i]

        # Reshape the unshuffled data to match the padded shape of the original image
        unshuffled_image = unshuffled_data.reshape(padded_image_shape)

        # Remove the padded pixels from the unshuffled image to get the original image
        nrows, ncols, nchannels = padded_image_shape
        pad_rows = int(np.ceil(nrows / 16.0) * 16) - nrows
        pad_cols = int(np.ceil(ncols / 16.0) * 16) - ncols
        original_image = unshuffled_image[:nrows - pad_rows, :ncols - pad_cols, :]

        return original_image








