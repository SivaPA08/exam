# 3DES EDE using PyCryptodome. Deprecated for modern use; lab demonstration only.
from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
import base64

def make_key(k1,k2,k3):
    raw=b"".join(x.encode() if isinstance(x,str) else x for x in (k1,k2,k3))
    if len(raw)!=24: raise ValueError("Provide three 8-byte keys")
    return DES3.adjust_key_parity(raw)

def encrypt(text,key):
    padded=pad(text.encode(),8)
    print("Padded plaintext:",padded.hex().upper())
    # PyCryptodome performs the internal E(K1)-D(K2)-E(K3) stages.
    cipher=DES3.new(key,DES3.MODE_ECB)
    result=cipher.encrypt(padded)
    print("Triple-DES ciphertext block(s):")
    for i in range(0,len(result),8): print(f"Block {i//8+1}: {result[i:i+8].hex().upper()}")
    print("Note: package API does not expose each internal DES round.")
    return result

def decrypt(data,key):
    raw=DES3.new(key,DES3.MODE_ECB).decrypt(data)
    print("Decrypted padded bytes:",raw.hex().upper())
    return unpad(raw,8).decode()

if __name__=="__main__":
    k1=input("Key 1 (8 chars): "); k2=input("Key 2 (8 chars): "); k3=input("Key 3 (8 chars): ")
    key=make_key(k1,k2,k3); text=input("Enter plaintext: ")
    c=encrypt(text,key); print("Ciphertext hex:",c.hex()); print("Ciphertext Base64:",base64.b64encode(c).decode())
    print("Decrypted:",decrypt(c,key))
