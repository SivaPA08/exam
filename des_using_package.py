# Educational DES example. DES/ECB is insecure; use only for the lab.
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64

def encrypt(text, key=b"8bytekey"):
    if isinstance(key,str): key=key.encode()
    if len(key)!=8: raise ValueError("DES key must be exactly 8 bytes")
    padded=pad(text.encode(),DES.block_size)
    print("Padded plaintext (hex):",padded.hex().upper())
    cipher=DES.new(key,DES.MODE_ECB)
    blocks=[]
    for i in range(0,len(padded),8):
        block=padded[i:i+8]
        encrypted=cipher.encrypt(block)
        print(f"Block {i//8+1}: input={block.hex().upper()} -> encrypted={encrypted.hex().upper()}")
        blocks.append(encrypted)
    return b"".join(blocks)

def decrypt(ciphertext, key=b"8bytekey"):
    if isinstance(key,str): key=key.encode()
    cipher=DES.new(key,DES.MODE_ECB)
    return unpad(cipher.decrypt(ciphertext),DES.block_size).decode()

if __name__ == "__main__":
    text=input("Enter plaintext: ")
    key=input("Enter 8-character key: ").encode()
    c=encrypt(text,key)
    print("Ciphertext (hex):",c.hex())
    print("Ciphertext (Base64):",base64.b64encode(c).decode())
    print("Decrypted:",decrypt(c,key))
