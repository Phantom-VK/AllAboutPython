import numpy as np


def mod26_inv(matrix):
    det = int(round(np.linalg.det(matrix))) % 26
    det_inv = None


    for i in range(26):
        if (det * i) % 26 == 1:
            det_inv = i
            break
    if det_inv is None:
        raise ValueError("Matrix is not invertible mod 26")

    matrix_mod_inv = np.round(det * np.linalg.inv(matrix)).astype(int) % 26
    #  inverse = det_inv * adjugate mod 26
    adjugate = matrix_mod_inv.T

    return (det_inv * adjugate) % 26


def text_to_numbers(text):
    return [ord(char) - ord('A') for char in text]


def numbers_to_text(numbers):
    return ''.join(chr(n + ord('A')) for n in numbers)


def hill_encrypt(plaintext, key_matrix):
    n = key_matrix.shape[0]
    plaintext = plaintext.upper().replace(" ", "")
    while len(plaintext) % n != 0:
        plaintext += 'X'

    ciphertext = []

    for i in range(0, len(plaintext), n):
        block = plaintext[i:i + n]
        block_vector = np.array(text_to_numbers(block))
        cipher_vector = key_matrix.dot(block_vector) % 26
        ciphertext.extend(cipher_vector)

    return numbers_to_text(ciphertext)


def hill_decrypt(ciphertext, key_matrix):
    n = key_matrix.shape[0]
    ciphertext = ciphertext.upper().replace(" ", "")

    inv_key_matrix = mod26_inv(key_matrix)

    plaintext = []

    for i in range(0, len(ciphertext), n):
        block = ciphertext[i:i + n]
        block_vector = np.array(text_to_numbers(block))
        plain_vector = inv_key_matrix.dot(block_vector) % 26
        plaintext.extend(plain_vector)

    return numbers_to_text(plaintext)

if __name__ == "__main__":
    key = np.array([[3, 3],
                    [2, 5]])

    plain = "HELLO"
    encrypted = hill_encrypt(plain, key)
    print("Encrypted:", encrypted)

    decrypted = hill_decrypt(encrypted, key)
    print("Decrypted:", decrypted)
