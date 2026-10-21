def clean(s):
    return "".join(c.upper() for c in s if c.isalpha())

def encrypt(text, key):
    p, k = clean(text), clean(key)
    if not k: raise ValueError("Key must contain letters")
    return "".join(chr((ord(ch)-65 + ord(k[i % len(k)])-65) % 26 + 65) for i,ch in enumerate(p))

def decrypt(text, key):
    c, k = clean(text), clean(key)
    if not k: raise ValueError("Key must contain letters")
    return "".join(chr((ord(ch)-65 - (ord(k[i % len(k)])-65)) % 26 + 65) for i,ch in enumerate(c))

if __name__ == "__main__":
    key = input("Enter key: "); text = input("Enter plaintext: ")
    print("Plaintext letters:",clean(text)); print("Key:",clean(key))
    expanded=(clean(key)*(len(clean(text))//len(clean(key))+1))[:len(clean(text))] if clean(key) else ""
    print("Repeated key stream:",expanded)
    c = encrypt(text,key); print("Encrypted:",c); print("Decrypted:",decrypt(c,key))
