# Diffie-Hellman key exchange, with intermediate values as in Lab 7/9.
def exchange(p, g, a, b):
    A = pow(g, a, p)
    B = pow(g, b, p)
    sa = pow(B, a, p)
    sb = pow(A, b, p)
    return A, B, sa, sb

if __name__ == "__main__":
    print("========== DIFFIE-HELLMAN KEY EXCHANGE ========== ")
    p = int(input("Enter prime number (p): "))
    g = int(input("Enter primitive root (g): "))
    a = int(input("Enter private key of Alice: "))
    b = int(input("Enter private key of Bob: "))
    A, B, sa, sb = exchange(p, g, a, b)
    print("\nPublic Parameters:")
    print("Prime p =", p, "\nPrimitive Root g =", g)
    print("\n========== ALICE ==========")
    print("Private Key =", a)
    print(f"Public Key A = g^a mod p = {g}^{a} mod {p} = {A}")
    print("\n========== BOB ==========")
    print("Private Key =", b)
    print(f"Public Key B = g^b mod p = {g}^{b} mod {p} = {B}")
    print("\n========== SHARED SECRET ==========")
    print(f"Alice calculates: B^a mod p = {B}^{a} mod {p} = {sa}")
    print(f"Bob calculates: A^b mod p = {A}^{b} mod {p} = {sb}")
    print("\nKey Exchange Successful!" if sa == sb else "\nKey Exchange Failed!")
