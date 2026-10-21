print("========== ELLIPTIC CURVE CRYPTOGRAPHY ==========")

p = int(input("Enter prime p: "))
a = int(input("Enter a: "))
b = int(input("Enter b: "))

if (4 * a**3 + 27 * b**2) % p == 0:
    raise ValueError("Invalid elliptic curve.")

Gx = int(input("Enter generator Gx: "))
Gy = int(input("Enter generator Gy: "))
G = (Gx, Gy)

if (Gy**2 - (Gx**3 + a * Gx + b)) % p != 0:
    raise ValueError("Generator point is not on the curve.")


def mod_inverse(k, p):
    k %= p

    for x in range(1, p):
        if (k * x) % p == 1:
            return x

    return None


def point_add(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and (y1 + y2) % p == 0:
        return None

    if P == Q:
        numerator = (3 * x1 * x1 + a) % p
        denominator = (2 * y1) % p
    else:
        numerator = (y2 - y1) % p
        denominator = (x2 - x1) % p

    inverse = mod_inverse(denominator, p)

    if inverse is None:
        return None

    slope = (numerator * inverse) % p

    x3 = (slope * slope - x1 - x2) % p
    y3 = (slope * (x1 - x3) - y1) % p

    return (x3, y3)


def scalar_multiply(k, P):
    result = None
    current = P

    while k > 0:
        if k % 2 == 1:
            result = point_add(result, current)

        current = point_add(current, current)
        k //= 2

    return result


print("\n========== CURVE DETAILS ==========")
print(f"Curve: y^2 = x^3 + {a}x + {b} (mod {p})")
print("Generator Point G =", G)


private_a = int(input("\nEnter Alice's private key: "))
private_b = int(input("Enter Bob's private key: "))

if private_a <= 0 or private_b <= 0:
    raise ValueError("Private keys must be positive integers.")


public_a = scalar_multiply(private_a, G)
public_b = scalar_multiply(private_b, G)

print("\n========== ALICE ==========")
print("Private Key =", private_a)
print("Public Key  = private key * G")
print("            =", private_a, "*", G)
print("            =", public_a)

print("\n========== BOB ==========")
print("Private Key =", private_b)
print("Public Key  = private key * G")
print("            =", private_b, "*", G)
print("            =", public_b)


shared_a = scalar_multiply(private_a, public_b)
shared_b = scalar_multiply(private_b, public_a)

print("\n========== SHARED SECRET ==========")

print("Alice calculates:")
print("S_A = private_a * public_b")
print("    =", private_a, "*", public_b)
print("    =", shared_a)

print("\nBob calculates:")
print("S_B = private_b * public_a")
print("    =", private_b, "*", public_a)
print("    =", shared_b)

print("\n========== RESULT ==========")

if shared_a == shared_b:
    print("ECC Key Exchange Successful!")
    print("Shared Secret =", shared_a)
else:
    print("ECC Key Exchange Failed!")
