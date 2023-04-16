class ImageCiphering:
    def encrypt_image(self, image, array):
        for i in range(len(image)):
            for j in range(len(image[i])):
                for k in range(len(image[i][j])):
                    if j % 3 == 0:
                        image[i][j][k] = array[image[i][j][k]]
                    elif j % 3 == 1:
                        image[i][j][k] = array[(image[i][j][k] + i) % 256]
                    else:
                        image[i][j][k] = array[(image[i][j][k] + j) % 256]
        return image

    def decrypt_image(self, image, array):
        # Compute the inverse of the encryption array
        inverse_array = [0] * 256
        for i in range(256):
            inverse_array[array[i]] = i

        # Decrypt the image by reversing the encryption process
        for i in range(len(image)):
            for j in range(len(image[i])):
                r, g, b = image[i][j]
                if j % 3 == 0:
                    image[i][j] = [inverse_array[r], inverse_array[g], inverse_array[b]]
                elif j % 3 == 1:
                    r = (r - i) % 256
                    g = (g - i) % 256
                    b = (b - i) % 256
                    image[i][j] = [inverse_array[r], inverse_array[g], inverse_array[b]]
                else:
                    r = (r - j) % 256
                    g = (g - j) % 256
                    b = (b - j) % 256
                    image[i][j] = [inverse_array[r], inverse_array[g], inverse_array[b]]

        return image
