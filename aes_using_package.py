# AES-CBC package example with random IV and PKCS#7 padding.
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

def encrypt(text,key):
    if isinstance(key,str): key=key.encode()
    if len(key) not in (16,24,32): raise ValueError("AES key must be 16, 24, or 32 bytes")
    raw=text.encode()
    padded=pad(raw,AES.block_size)
    iv=get_random_bytes(16)
    print("Plaintext bytes:",raw.hex().upper())
    print("PKCS#7 padded bytes:",padded.hex().upper())
    print("Random IV:",iv.hex().upper())
    cipher=AES.new(key,AES.MODE_CBC,iv)
    ciphertext=cipher.encrypt(padded)
    previous=iv
    print("CBC block intermediates:")
    for i in range(0,len(padded),16):
        block=padded[i:i+16]
        mixed=bytes(x^y for x,y in zip(block,previous))
        encrypted=ciphertext[i:i+16]
        print(f"Block {i//16+1}: padded block={block.hex().upper()} XOR previous/IV={mixed.hex().upper()} ciphertext={encrypted.hex().upper()}")
        previous=encrypted
    print("Package note: AES internal SubBytes/ShiftRows/MixColumns/AddRoundKey rounds are not exposed by PyCryptodome.")
    return iv+ciphertext

def decrypt(blob,key):
    if isinstance(key,str): key=key.encode()
    iv, ciphertext=blob[:16],blob[16:]
    cipher=AES.new(key,AES.MODE_CBC,iv)
    raw=cipher.decrypt(ciphertext)
    print("CBC decrypted padded bytes:",raw.hex().upper())
    plain=unpad(raw,AES.block_size)
    print("After PKCS#7 unpadding:",plain.hex().upper())
    return plain.decode()

if __name__ == "__main__":
    text=input("Enter plaintext: "); key=input("Enter AES key (16/24/32 characters): ").encode()
    blob=encrypt(text,key)
    print("\nIV+ciphertext (Base64):",base64.b64encode(blob).decode())
    print("Decrypted:",decrypt(blob,key))
