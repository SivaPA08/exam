# Vigenere-style polyalphabetic cipher
def encrypt(text,key):
    if not key or any(not c.isalpha() for c in key): raise ValueError("Key must contain letters")
    out=[]; j=0
    for ch in text:
        if ch.isalpha() and ch.isascii():
            base=65 if ch.isupper() else 97
            k=ord(key[j%len(key)].lower())-97
            out.append(chr((ord(ch)-base+k)%26+base)); j+=1
        else: out.append(ch)
    return "".join(out)

def decrypt(text,key):
    if not key or any(not c.isalpha() for c in key): raise ValueError("Key must contain letters")
    out=[]; j=0
    for ch in text:
        if ch.isalpha() and ch.isascii():
            base=65 if ch.isupper() else 97
            k=ord(key[j%len(key)].lower())-97
            out.append(chr((ord(ch)-base-k)%26+base)); j+=1
        else: out.append(ch)
    return "".join(out)

if __name__ == "__main__":
    text=input("Enter text: "); key=input("Enter key: ")
    print("Plaintext:",text); print("Key:",key)
    letters=sum(1 for ch in text if ch.isalpha() and ch.isascii())
    print("Repeated key stream:", (key.lower()*(letters//len(key)+1))[:letters] if key else "")
    c=encrypt(text,key); print("Encrypted:",c); print("Decrypted:",decrypt(c,key))
