def encrypt(text, rails):
    if rails < 1: raise ValueError("Rails must be >= 1")
    if rails == 1 or rails >= len(text): return text
    rows=["" for _ in range(rails)]; row=0; direction=1
    for ch in text:
        rows[row]+=ch
        if row==0: direction=1
        elif row==rails-1: direction=-1
        row+=direction
    return "".join(rows)

def decrypt(cipher, rails):
    if rails < 1: raise ValueError("Rails must be >= 1")
    if rails == 1 or rails >= len(cipher): return cipher
    pattern=[]; row=0; direction=1
    for _ in cipher:
        pattern.append(row)
        if row==0: direction=1
        elif row==rails-1: direction=-1
        row+=direction
    counts=[pattern.count(r) for r in range(rails)]
    parts=[]; pos=0
    for count in counts:
        parts.append(list(cipher[pos:pos+count])); pos+=count
    indices=[0]*rails; out=[]
    for r in pattern:
        out.append(parts[r][indices[r]]); indices[r]+=1
    return "".join(out)

if __name__ == "__main__":
    text=input("Enter text: "); k=int(input("Enter number of rails: "))
    print("Plaintext:",text); print("Rails:",k)
    c=encrypt(text,k); print("Ciphertext (rail-wise read):",c); print("Decrypted:",decrypt(c,k))
