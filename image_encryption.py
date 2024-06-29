from PIL import Image

def encrypt_image(image_path, key):
    with Image.open(image_path) as img:
        pixel_data = img.load()
        width, height = img.size
        for x in range(width):
            for y in range(height):
                pixel_data[x, y] = (pixel_data[x, y][0] ^ key, pixel_data[x, y][1] ^ key, pixel_data[x, y][2] ^ key)
        img.save("encrypted_image.png")

def decrypt_image(image_path, key):
    with Image.open(image_path) as img:
        pixel_data = img.load()
        width, height = img.size
        for x in range(width):
            for y in range(height):
                pixel_data[x, y] = (pixel_data[x, y][0] ^ key, pixel_data[x, y][1] ^ key, pixel_data[x, y][2] ^ key)
        img.save("decrypted_image.png")

if __name__ == "__main__":
    image_path = "Image_path.jpg"
    key = 25  # Encryption/Decryption key (any integer value can be used as the key)

    # Encrypting the image
    encrypt_image(image_path, key)

    # Decrypting the image (use the same key as the encryption key)
    decrypt_image("encrypted_image.png", key)