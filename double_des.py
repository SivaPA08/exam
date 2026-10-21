# Double DES (E_K2(E_K1(P))) using PyCryptodome; insecure and for lab use only.
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def encrypt(text,key1,key2):
    p=pad(text.encode(),8)
    print("Padded plaintext:",p.hex().upper())
    c1=DES.new(key1,DES.MODE_ECB).encrypt(p)
    print("Intermediate C1 = E(K1, P):",c1.hex().upper())
    c2=DES.new(key2,DES.MODE_ECB).encrypt(c1)
    print("Final C2 = E(K2, C1):",c2.hex().upper())
    return c2

def decrypt(ciphertext,key1,key2):
    c1=DES.new(key2,DES.MODE_ECB).decrypt(ciphertext)
    print("Intermediate C1 = D(K2, C):",c1.hex().upper())
    p=DES.new(key1,DES.MODE_ECB).decrypt(c1)
    print("Padded plaintext after D(K1, C1):",p.hex().upper())
    return unpad(p,8).decode()

if __name__=="__main__":
    k1=input("Key 1 (8 chars): ").encode(); k2=input("Key 2 (8 chars): ").encode()
    if len(k1)!=8 or len(k2)!=8: raise SystemExit("Each key must be 8 bytes")
    text=input("Enter plaintext: "); c=encrypt(text,k1,k2)
    print("\n========== DOUBLE DES RESULT ==========\nCiphertext hex:",c.hex().upper()); print("Decrypted:",decrypt(c,k1,k2))
