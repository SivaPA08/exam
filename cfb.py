"""CFB (Cipher Feedback) mode using PyCryptodome AES or DES.

Full-block CFB: AES uses 16-byte blocks; DES uses 8-byte blocks.
Intermediate values are printed for every block.
Install dependency: python -m pip install pycryptodome
"""
from Crypto.Cipher import AES, DES
import base64


def hx(data):
    return data.hex().upper()


def make_cipher(algorithm, key):
    algorithm = algorithm.strip().upper()
    if algorithm == "AES":
        if len(key) not in (16, 24, 32):
            raise ValueError("AES key must be 16, 24, or 32 bytes.")
        return AES.new(key, AES.MODE_ECB), 16
    if algorithm == "DES":
        if len(key) != 8:
            raise ValueError("DES key must be exactly 8 bytes.")
        return DES.new(key, DES.MODE_ECB), 8
    raise ValueError("Choose AES or DES.")


def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


def encrypt(plaintext, key, iv, algorithm="AES", show=True):
    cipher, size = make_cipher(algorithm, key)
    if len(iv) != size:
        raise ValueError(f"{algorithm.upper()} IV must be exactly {size} bytes.")
    feedback = iv
    result = bytearray()
    if show:
        print(f"\n========== CFB {algorithm.upper()} ENCRYPTION ==========")
        print("Initial IV / feedback :", hx(feedback))
    for offset in range(0, len(plaintext), size):
        block = plaintext[offset:offset + size]
        encrypted_feedback = cipher.encrypt(feedback)
        stream = encrypted_feedback[:len(block)]
        cipher_block = xor_bytes(block, stream)
        result.extend(cipher_block)
        if show:
            print(f"\n--- Block {offset // size + 1} ---")
            print("Feedback register     :", hx(feedback))
            print("E(feedback)           :", hx(encrypted_feedback))
            print("Plaintext block       :", hx(block))
            print("Keystream portion     :", hx(stream))
            print("Plaintext XOR stream  :", hx(cipher_block))
            print("Ciphertext block      :", hx(cipher_block))
        # CFB feeds ciphertext back into the register.
        if len(block) == size:
            feedback = cipher_block
            if show:
                print("Updated feedback      :", hx(feedback))
    return bytes(result)


def decrypt(ciphertext, key, iv, algorithm="AES", show=True):
    cipher, size = make_cipher(algorithm, key)
    if len(iv) != size:
        raise ValueError(f"{algorithm.upper()} IV must be exactly {size} bytes.")
    feedback = iv
    result = bytearray()
    if show:
        print(f"\n========== CFB {algorithm.upper()} DECRYPTION ==========")
        print("Initial IV / feedback :", hx(feedback))
    for offset in range(0, len(ciphertext), size):
        block = ciphertext[offset:offset + size]
        encrypted_feedback = cipher.encrypt(feedback)  # CFB uses E() for both directions
        stream = encrypted_feedback[:len(block)]
        plain_block = xor_bytes(block, stream)
        result.extend(plain_block)
        if show:
            print(f"\n--- Block {offset // size + 1} ---")
            print("Feedback register      :", hx(feedback))
            print("E(feedback)            :", hx(encrypted_feedback))
            print("Ciphertext block       :", hx(block))
            print("Keystream portion      :", hx(stream))
            print("Ciphertext XOR stream  :", hx(plain_block))
            print("Plaintext block        :", hx(plain_block))
        if len(block) == size:
            feedback = block
            if show:
                print("Updated feedback       :", hx(feedback))
    return bytes(result)


def main():
    algorithm = input("Choose cipher (AES/DES): ").strip().upper()
    key = input("Key as text (AES: 16/24/32 bytes; DES: 8 bytes): ").encode()
    _, size = make_cipher(algorithm, key)
    iv = input(f"IV as text ({size} bytes): ").encode()
    if len(iv) != size:
        raise ValueError(f"IV must be exactly {size} bytes after UTF-8 encoding.")
    plaintext = input("Plaintext: ").encode("utf-8")
    ciphertext = encrypt(plaintext, key, iv, algorithm, True)
    recovered = decrypt(ciphertext, key, iv, algorithm, True)
    print("\n========== RESULT ==========")
    print("Ciphertext (hex)   :", hx(ciphertext))
    print("Ciphertext (Base64):", base64.b64encode(ciphertext).decode())
    print("Decrypted text     :", recovered.decode("utf-8", errors="replace"))


if __name__ == "__main__":
    main()
