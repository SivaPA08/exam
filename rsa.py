import math

def generate_keys(p,q,e=None):
    if p==q or p<2 or q<2: raise ValueError("Use distinct primes")
    n=p*q; phi=(p-1)*(q-1)
    if e is None:
        e=3
        while math.gcd(e,phi)!=1: e+=2
    if math.gcd(e,phi)!=1: raise ValueError("e must be coprime to phi(n)")
    d=pow(e,-1,phi)
    return (e,n),(d,n)

def encrypt_int(m,public_key):
    e,n=public_key
    if not 0<=m<n: raise ValueError("Message integer must be in [0,n)")
    return pow(m,e,n)

def decrypt_int(c,private_key):
    d,n=private_key
    return pow(c,d,n)

if __name__ == "__main__":
    p=int(input("Enter prime p (small lab example): ")); q=int(input("Enter prime q: "))
    pub,priv=generate_keys(p,q)
    n=p*q; phi=(p-1)*(q-1)
    print("\nIntermediate calculations:")
    print(f"n = p*q = {p}*{q} = {n}")
    print(f"phi(n) = (p-1)(q-1) = {phi}")
    print("Public key (e,n):",pub); print("Private key (d,n):",priv)
    print(f"Check: (e*d) mod phi(n) = {(pub[0]*priv[0])%phi}")
    m=int(input(f"Enter integer plaintext 0 <= m < {pub[1]}: "))
    c=encrypt_int(m,pub); print(f"Encryption: c = m^e mod n = {m}^{pub[0]} mod {pub[1]} = {c}")
    print(f"Decryption: m = c^d mod n = {c}^{priv[0]} mod {priv[1]} = {decrypt_int(c,priv)}")
