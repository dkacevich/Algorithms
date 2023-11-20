import numpy as np
from PIL import Image


def simple_xor_encrypt_decrypt(text, key):
    """
    Шифрує або дешифрує текст за допомогою простого XOR-шифрування.

    :param text: str, текст для шифрування або дешифрування.
    :param key: int, ключ для XOR-шифрування.
    :return: str, шифрований або дешифрований текст.
    """
    extended_key = (key * (len(text) // len(key) + 1))[:len(text)]
    return ''.join(chr(ord(char) ^ ord(key_char)) for char, key_char in zip(text, extended_key))


def encode_text_in_image_utf8(image, text):
    """
    Вбудовує текст у зображення, змінюючи найменш значущі біти (з урахуванням UTF-8).

    :param image: PIL Image object, зображення для вбудовування тексту.
    :param text: str, текст для вбудовування.
    :return: PIL Image object, зображення з вбудованим текстом.
    """
    
    # Конвертуємо текст у двійковий формат з урахуванням UTF-8
    binary_text = ''.join([format(byte, '08b') for byte in text.encode('utf-8')])
    binary_text += '10101101'  # Додаємо маркер кінця тексту

    # Отримуємо дані зображення
    pixels = np.array(image)
    
    flat_pixels = pixels.flatten()

    # Перевіряємо, чи достатньо місця в зображенні для тексту
    if len(binary_text) > len(flat_pixels):
        raise ValueError("Текст занадто великий для вбудовування у це зображення.")

    # Вбудовування тексту
    for i in range(len(binary_text)):
        flat_pixels[i] = flat_pixels[i] & ~1 | int(binary_text[i])

    # Відновлюємо структуру пікселів зображення
    encoded_pixels = flat_pixels.reshape(pixels.shape)
    encoded_image = Image.fromarray(encoded_pixels)

    return encoded_image

def decode_text_from_image_utf8(image):
    """
    Вилучає текст з зображення, читаючи найменш значущі біти пікселів (з урахуванням UTF-8).

    :param image: PIL Image object, зображення з вбудованим текстом.
    :return: str, вилучений текст.
    """
    # Отримуємо дані зображення
    pixels = np.array(image)
    flat_pixels = pixels.flatten()

    # Читаємо двійкові біти тексту
    binary_text = ''.join([str(pixel & 1) for pixel in flat_pixels])

    # Конвертуємо двійковий рядок назад у байти
    byte_array = bytearray()
    for i in range(0, len(binary_text), 8):
        byte = binary_text[i:i+8]
        if byte == '10101101':  # Маркер кінця тексту
            break
        byte_array.append(int(byte, 2))

    # Декодуємо байти у текст
    decoded_text = byte_array.decode('utf-8')

    return decoded_text

# Приклад використання
original_image = Image.open('encoding/white_noise_image.png')  # Замініть на шлях до вашого зображення
text_to_encode = "Привет, как дела? Вот мой пароль: СОВЕРШЕННО СЕКРЕТНО"
key = "hekjfsfiskjfjsidfj"


encrypted_text = simple_xor_encrypt_decrypt(text_to_encode, key)

encoded_image = encode_text_in_image_utf8(original_image, encrypted_text)
decoded_text = decode_text_from_image_utf8(encoded_image)

print("Вилучений текст:", simple_xor_encrypt_decrypt(decoded_text, key))
