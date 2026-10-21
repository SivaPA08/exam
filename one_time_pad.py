import secrets
import string

def clean(s): return "".join(c.upper() for c in s if c.isalpha())

def encrypt(text, key):
    p,k=clean(text),clean(key)
    if len(p)!=len(k): raise ValueError("OTP key must be same length as cleaned plaintext")
    return "".join(chr((ord(a)-65+ord(b)-65)%26+65) for a,b in zip(p,k))

def decrypt(cipher, key):
    c,k=clean(cipher),clean(key)
    if len(c)!=len(k): raise ValueError("OTP key must be same length as cleaned ciphertext")
    return "".join(chr((ord(a)-65-(ord(b)-65))%26+65) for a,b in zip(c,k))

def generate_key(length):
    return "".join(secrets.choice(string.ascii_uppercase) for _ in range(length))

if __name__ == "__main__":
    text=clean(input("Enter plaintext (letters only): "))
    key=input("Enter key or press Enter to generate one: ").upper()
    if not key: key=generate_key(len(text)); print("Generated key (save it securely):",key)
    print("Plaintext:",text); print("Key:",key)
    print("Plaintext numeric:",[ord(ch)-65 for ch in text]); print("Key numeric:",[ord(ch)-65 for ch in key])
    c=encrypt(text,key); print("Encrypted:",c); print("Cipher numeric:",[ord(ch)-65 for ch in c]); print("Decrypted:",decrypt(c,key))
