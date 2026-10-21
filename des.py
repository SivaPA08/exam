# Full educational DES implementation (permutation tables, key schedule, 16 Feistel rounds).
# DES is obsolete and insecure. For study only.
IP=[58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]
FP=[40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25]
E=[32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]
P=[16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]
PC1=[57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]
PC2=[14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]
SHIFTS=[1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
SBOX=[
[[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]],
[[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]],
[[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]],
[[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]],
[[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]],
[[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]],
[[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]],
[[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]]


def permute(x, table, nbits):
    out=0
    for pos in table: out=(out<<1)|((x>>(nbits-pos))&1)
    return out

def subkeys(key, show=False):
    k=int.from_bytes(key,"big")
    k=permute(k,PC1,64); c=k>>28; d=k&((1<<28)-1); keys=[]
    for i,shift in enumerate(SHIFTS, 1):
        c=((c<<shift)|(c>>(28-shift)))&((1<<28)-1)
        d=((d<<shift)|(d>>(28-shift)))&((1<<28)-1)
        round_key=permute((c<<28)|d,PC2,56)
        keys.append(round_key)
        if show: print(f"Round key K{i:02}: {round_key:012X}")
    return keys

def f(r,k,show=False):
    expanded=permute(r,E,32); x=expanded^k; out=0
    for i in range(8):
        six=(x>>(42-6*i))&0x3f
        row=((six&0x20)>>4)|(six&1); col=(six>>1)&0xf
        out=(out<<4)|SBOX[i][row][col]
    result=permute(out,P,32)
    if show: print(f"  E(R)={expanded:012X}  E(R) XOR K={x:012X}  S-Box={out:08X}  P-box F={result:08X}")
    return result

def block(block8,key,decrypt=False,show=False):
    if len(block8)!=8 or len(key)!=8: raise ValueError("DES block and key must be 8 bytes")
    if show: print("\n========== KEY GENERATION ==========\nEffective 48-bit round keys:")
    keys=subkeys(key,show)
    if decrypt: keys=keys[::-1]
    x=permute(int.from_bytes(block8,"big"),IP,64); l=x>>32; r=x&0xffffffff
    if show:
        print(f"\n========== {'DECRYPTION' if decrypt else 'ENCRYPTION'} BLOCK ==========")
        print(f"Input Block = {int.from_bytes(block8,'big'):016X}")
        print(f"After IP = {x:016X}\nL0 = {l:08X}\nR0 = {r:08X}")
    for i,k in enumerate(keys,1):
        old_l,old_r=l,r
        new_l,new_r=r,l^f(r,k,show)
        if show:
            print(f"Round {i}\nKey = {k:012X}\nL = {old_l:08X}\nR = {old_r:08X}\nNew L = {new_l:08X}\nNew R = {new_r:08X}\n")
        l,r=new_l,new_r
    pre=(r<<32)|l; final=permute(pre,FP,64)
    if show: print(f"Before FP = {pre:016X}\nAfter FP = {final:016X}")
    return final.to_bytes(8,"big")

def encrypt_block(block8,key,show=False): return block(block8,key,False,show)
def decrypt_block(block8,key,show=False): return block(block8,key,True,show)

if __name__=="__main__":
    key=input("Enter 8-character key: ").encode()
    text=input("Enter plaintext (exactly 8 bytes): ").encode()
    if len(text)!=8 or len(key)!=8: raise SystemExit("Plaintext and key must each be exactly 8 bytes.")
    print("Plaintext (hex):",text.hex().upper())
    c=encrypt_block(text,key,show=True)
    print("\nCiphertext (hex):",c.hex().upper())
    print("\n========== DECRYPTION TRACE ==========\nDecrypted:",decrypt_block(c,key,show=True).decode(errors="replace"))
