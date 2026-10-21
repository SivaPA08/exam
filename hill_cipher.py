# Valid key : 3 3 2 5
def clean(s): return "".join(c for c in s.upper() if "A" <= c <= "Z")
def inv_mod(a,m):
    return pow(a, -1, m)
    
def encrypt(text,key):
    p=clean(text)
    if len(p)%2: p+="X"
    a,b=key[0]; c,d=key[1]
    det=(a*d-b*c)%26
    inv_mod(det,26)
    out=""
    for i in range(0,len(p),2):
        x,y=ord(p[i])-65,ord(p[i+1])-65
        out+=chr(((a*x+b*y)%26)+65)+chr(((c*x+d*y)%26)+65)
    return out

def decrypt(cipher,key):
    s=clean(cipher)
    if len(s)%2: raise ValueError("Ciphertext length must be even")
    a,b=key[0]; c,d=key[1]; det=(a*d-b*c)%26
    inv=inv_mod(det,26)
    inverse=[[inv*d%26,(-inv*b)%26],[(-inv*c)%26,inv*a%26]]
    out=""
    for i in range(0,len(s),2):
        x,y=ord(s[i])-65,ord(s[i+1])-65
        out+=chr((inverse[0][0]*x+inverse[0][1]*y)%26+65)
        out+=chr((inverse[1][0]*x+inverse[1][1]*y)%26+65)
    return out

if __name__ == "__main__":
    key=[[int(input("key[0][0]: ")),int(input("key[0][1]: "))],
         [int(input("key[1][0]: ")),int(input("key[1][1]: "))]]
    text=input("Enter plaintext: ")
    print("Key matrix:",key)
    normalized=clean(text); padded=normalized+("X" if len(normalized)%2 else "")
    print("Normalized plaintext:",normalized); print("Padded plaintext:",padded)
    print("Plaintext numeric pairs:",[(ord(padded[i])-65,ord(padded[i+1])-65) for i in range(0,len(padded),2)])
    c=encrypt(text,key)
    print("Encrypted:",c); print("Decrypted:",decrypt(c,key))
