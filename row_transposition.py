def order_for_key(key):
    return sorted(range(len(key)), key=lambda i: (key[i], i))

def encrypt(text, key):
    if not key: raise ValueError("Key cannot be empty")
    cols=len(key); rows=(len(text)+cols-1)//cols
    text += "X"*(rows*cols-len(text))
    matrix=[text[i:i+cols] for i in range(0,len(text),cols)]
    return "".join(matrix[r][c] for c in order_for_key(key) for r in range(rows))

def decrypt(cipher, key):
    if not key or len(cipher)%len(key): raise ValueError("Ciphertext length must be a multiple of key length")
    cols=len(key); rows=len(cipher)//cols; matrix=[[""]*cols for _ in range(rows)]
    pos=0
    for c in order_for_key(key):
        for r in range(rows):
            matrix[r][c]=cipher[pos]; pos+=1
    return "".join("".join(row) for row in matrix)

def double_transposition(text, key1, key2):
    return encrypt(encrypt(text,key1),key2)

def double_transposition_decrypt(cipher, key1, key2):
    return decrypt(decrypt(cipher,key2),key1)

if __name__ == "__main__":
    text=input("Enter plaintext: "); key=input("Enter key: ")
    cols=len(key); rows=(len(text)+cols-1)//cols
    padded=text+"X"*(rows*cols-len(text))
    matrix=[padded[i:i+cols] for i in range(0,len(padded),cols)]
    print("\nPadded plaintext:",padded)
    print("Encryption matrix:")
    for row in matrix: print(" ".join(row))
    order=order_for_key(key)
    print("Key:",key); print("Column reading order (0-based):",order)
    c=encrypt(text,key); print("Encrypted:",c); print("Decrypted matrix/text (may end in X):",decrypt(c,key))
    key2=input("Second key for double transposition (or Enter to skip): ")
    if key2:
        d=double_transposition(text,key,key2); print("Double encrypted:",d); print("Double decrypted:",double_transposition_decrypt(d,key,key2))
