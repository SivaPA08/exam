"""Triple AES-128 demonstration using EDE (Encrypt-Decrypt-Encrypt).
Educational block-cipher demo: exactly one 16-byte block; no padding/mode.
The construction mirrors the common EDE form of Triple DES, but uses AES.
"""
from aes import encrypt_block, decrypt_block


def read_block(prompt):
    value = input(prompt).encode("utf-8")
    if len(value) != 16:
        raise ValueError("Enter exactly 16 UTF-8 bytes (ASCII characters are safest for this lab demo).")
    return value


def encrypt(block, key1, key2, key3, show=True):
    if show:
        print("\n=== TRIPLE AES EDE ENCRYPTION ===")
        print("Plaintext block:", block.hex().upper())
        print("Key 1:", key1.hex().upper())
    stage1 = encrypt_block(block, key1, show=show)
    print("Stage 1 — E(K1, P):", stage1.hex().upper())
    if show:
        print("\nKey 2:", key2.hex().upper())
    stage2 = decrypt_block(stage1, key2, show=show)
    print("Stage 2 — D(K2, Stage 1):", stage2.hex().upper())
    if show:
        print("\nKey 3:", key3.hex().upper())
    stage3 = encrypt_block(stage2, key3, show=show)
    print("Stage 3 — E(K3, Stage 2):", stage3.hex().upper())
    print("Final Triple-AES EDE ciphertext:", stage3.hex().upper())
    return stage3


def decrypt(ciphertext, key1, key2, key3, show=True):
    if show:
        print("\n=== TRIPLE AES EDE DECRYPTION ===")
        print("Ciphertext block:", ciphertext.hex().upper())
    stage1 = decrypt_block(ciphertext, key3, show=show)
    print("Stage 1 — D(K3, C):", stage1.hex().upper())
    stage2 = encrypt_block(stage1, key2, show=show)
    print("Stage 2 — E(K2, Stage 1):", stage2.hex().upper())
    plain = decrypt_block(stage2, key1, show=show)
    print("Stage 3 — D(K1, Stage 2):", plain.hex().upper())
    print("Recovered plaintext:", plain.hex().upper())
    return plain


if __name__ == "__main__":
    try:
        plaintext = read_block("Enter plaintext (exactly 16 bytes): ")
        key1 = read_block("Enter AES Key 1 (exactly 16 bytes): ")
        key2 = read_block("Enter AES Key 2 (exactly 16 bytes): ")
        key3 = read_block("Enter AES Key 3 (exactly 16 bytes): ")
        ciphertext = encrypt(plaintext, key1, key2, key3)
        recovered = decrypt(ciphertext, key1, key2, key3)
        print("\nDecryption successful:", recovered == plaintext)
    except ValueError as exc:
        raise SystemExit(str(exc))
