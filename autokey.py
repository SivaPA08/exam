def clean(s): return "".join(c.upper() for c in s if c.isalpha())

def encrypt(text, key):
    p, k = clean(text), clean(key)
    if not k: raise ValueError("Key must contain letters")
    stream = k + p
    return "".join(chr((ord(ch)-65 + ord(stream[i])-65) % 26 + 65) for i,ch in enumerate(p))

def decrypt(cipher, key):
    c, k = clean(cipher), clean(key)
    if not k: raise ValueError("Key must contain letters")
    p = ""
    for i, ch in enumerate(c):
        keychar = k[i] if i < len(k) else p[i-len(k)]
        p += chr((ord(ch)-65 - (ord(keychar)-65)) % 26 + 65)
    return p

if __name__ == "__main__":
    key=input("Enter primer key: "); text=input("Enter plaintext: ")
    ptext, primer = clean(text), clean(key)
    print("Plaintext letters:",ptext); print("Primer key:",primer); print("Encryption key stream:",(primer+ptext)[:len(ptext)])
    c=encrypt(text,key); print("Encrypted:",c); print("Decrypted:",decrypt(c,key))
