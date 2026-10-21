"""Double AES-128 demonstration using the local from-scratch AES implementation.
Educational block-cipher demo: exactly one 16-byte block; no padding/mode.
"""
from aes import encrypt_block, decrypt_block


def read_block(prompt):
    value = input(prompt).encode("utf-8")
    if len(value) != 16:
        raise ValueError("Enter exactly 16 UTF-8 bytes (ASCII characters are safest for this lab demo).")
    return value


def encrypt(block, key1, key2, show=True):
    if show:
        print("\n=== DOUBLE AES ENCRYPTION ===")
        print("Plaintext block:", block.hex().upper())
        print("Key 1:", key1.hex().upper())
    first = encrypt_block(block, key1, show=show)
    print("After AES encryption with Key 1:", first.hex().upper())
    if show:
        print("\nKey 2:", key2.hex().upper())
    second = encrypt_block(first, key2, show=show)
    print("Final Double-AES ciphertext:", second.hex().upper())
    return second


def decrypt(ciphertext, key1, key2, show=True):
    if show:
        print("\n=== DOUBLE AES DECRYPTION ===")
        print("Ciphertext block:", ciphertext.hex().upper())
    first = decrypt_block(ciphertext, key2, show=show)
    print("After AES decryption with Key 2:", first.hex().upper())
    plain = decrypt_block(first, key1, show=show)
    print("Recovered plaintext:", plain.hex().upper())
    return plain


if __name__ == "__main__":
    try:
        plaintext = read_block("Enter plaintext (exactly 16 bytes): ")
        key1 = read_block("Enter AES Key 1 (exactly 16 bytes): ")
        key2 = read_block("Enter AES Key 2 (exactly 16 bytes): ")
        ciphertext = encrypt(plaintext, key1, key2)
        recovered = decrypt(ciphertext, key1, key2)
        print("\nDecryption successful:", recovered == plaintext)
    except ValueError as exc:
        raise SystemExit(str(exc))
