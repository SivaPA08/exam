def encrypt(text, key):
    result = []
    key %= 26
    for ch in text:
        if ch.isupper():
            result.append(chr((ord(ch) - 65 + key) % 26 + 65))
        elif ch.islower():
            result.append(chr((ord(ch) - 97 + key) % 26 + 97))
        else:
            result.append(ch)
    return "".join(result)

def decrypt(text, key):
    return encrypt(text, -key)

if __name__ == "__main__":
    text = input("Enter plaintext: ")
    key = int(input("Enter key (0-25): "))
    print("Plaintext:", text)
    print("Normalized key:", key % 26)
    cipher = encrypt(text, key)
    print("Encrypted:", cipher)
    print("Decrypted:", decrypt(cipher, key))
