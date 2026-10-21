import string
ALPHABET=string.ascii_lowercase

def validate_key(key):
    key=key.lower()
    if len(key)!=26 or set(key)!=set(ALPHABET):
        raise ValueError("Key must be a permutation of all 26 letters")
    return key

def encrypt(text,key):
    key=validate_key(key); out=[]
    for ch in text:
        if ch.isalpha() and ch.lower() in ALPHABET:
            x=key[ord(ch.lower())-97]; out.append(x.upper() if ch.isupper() else x)
        else: out.append(ch)
    return "".join(out)

def decrypt(text,key):
    key=validate_key(key); out=[]
    for ch in text:
        if ch.isalpha() and ch.lower() in ALPHABET:
            x=ALPHABET[key.index(ch.lower())]; out.append(x.upper() if ch.isupper() else x)
        else: out.append(ch)
    return "".join(out)

if __name__ == "__main__":
    key=input("Enter 26-letter substitution key: ")
    text=input("Enter text: "); print("Alphabet:",ALPHABET); print("Substitution key:",key.lower()); c=encrypt(text,key)
    print("Encrypted:",c); print("Decrypted:",decrypt(c,key))
