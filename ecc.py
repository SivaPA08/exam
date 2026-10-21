p=17; a=2; b=2
G=(5,1)
O=None

def inv_mod(x,mod):
    x%=mod
    if x==0: raise ZeroDivisionError("No inverse")
    return pow(x,-1,mod)

def point_add(P,Q):
    if P is None: return Q
    if Q is None: return P
    x1,y1=P; x2,y2=Q
    if x1==x2 and (y1+y2)%p==0: return None
    if P==Q:
        if y1%p==0: return None
        slope=((3*x1*x1+a)*inv_mod(2*y1,p))%p
    else:
        slope=((y2-y1)*inv_mod(x2-x1,p))%p
    x3=(slope*slope-x1-x2)%p
    y3=(slope*(x1-x3)-y1)%p
    return x3,y3

def scalar_multiply(k,P):
    result=None
    while k:
        if k&1: result=point_add(result,P)
        P=point_add(P,P); k >>= 1
    return result

if __name__ == "__main__":
    print(f"Curve: y^2 = x^3 + {a}x + {b} (mod {p}), G={G}")
    ka=int(input("Alice private key: ")); kb=int(input("Bob private key: "))
    print("\nCurve equation: y^2 = x^3 + ax + b (mod p)")
    print(f"p={p}, a={a}, b={b}, Generator G={G}")
    A=scalar_multiply(ka,G); B=scalar_multiply(kb,G)
    print("\n========== ALICE ==========")
    print("Private key:",ka); print(f"Public point A = {ka}G =",A)
    print("\n========== BOB ==========")
    print("Private key:",kb); print(f"Public point B = {kb}G =",B)
    sa=scalar_multiply(ka,B); sb=scalar_multiply(kb,A)
    print("\n========== SHARED SECRET ==========")
    print(f"Alice computes {ka}B =",sa)
    print(f"Bob computes {kb}A =",sb)
    print("ECC Key Exchange Successful!" if sa==sb else "ECC Key Exchange Failed!")
