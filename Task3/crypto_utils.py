from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

BLOCK_SIZE = 16

def encrypt_file(data, key):
    iv = get_random_bytes(BLOCK_SIZE)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    padding = BLOCK_SIZE - len(data) % BLOCK_SIZE
    data += bytes([padding]) * padding

    encrypted = cipher.encrypt(data)
    return iv + encrypted


def decrypt_file(data, key):
    iv = data[:BLOCK_SIZE]
    encrypted = data[BLOCK_SIZE:]

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(encrypted)

    padding = decrypted[-1]
    return decrypted[:-padding]
