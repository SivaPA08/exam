import struct, math

def left_rotate(x,n):
    x &= 0xffffffff
    return ((x<<n)|(x>>(32-n))) & 0xffffffff

def md5(message, show=True):
    data=message.encode("utf-8"); bit_len=(len(data)*8)%(1<<64)
    if show: print("Original message bytes:",data.hex().upper()); print("Original length (bits):",bit_len)
    data+=b"\x80"
    while len(data)%64!=56: data+=b"\x00"
    data+=struct.pack("<Q",bit_len)
    if show: print("Padded message:",data.hex().upper())
    s=[7,12,17,22]*4+[5,9,14,20]*4+[4,11,16,23]*4+[6,10,15,21]*4
    K=[int(abs(math.sin(i+1))*(1<<32)) & 0xffffffff for i in range(64)]
    a0,b0,c0,d0=0x67452301,0xefcdab89,0x98badcfe,0x10325476
    for off in range(0,len(data),64):
        M=list(struct.unpack("<16I",data[off:off+64]))
        if show:
            print(f"\nBlock at byte offset {off}: 16 message words")
            for j,value in enumerate(M): print(f"M[{j:2}] = {value:08X}")
        A,B,C,D=a0,b0,c0,d0
        for i in range(64):
            if i<16: F=(B&C)|(~B&D); g=i
            elif i<32: F=(D&B)|(~D&C); g=(5*i+1)%16
            elif i<48: F=B^C^D; g=(3*i+5)%16
            else: F=C^(B|~D); g=(7*i)%16
            F=(F+A+K[i]+M[g])&0xffffffff
            A,D,C,B=D,C,B,(B+left_rotate(F,s[i]))&0xffffffff
            if show and (i+1) in (16,32,48,64): print(f"After Round {i+1}: A={A:08X} B={B:08X} C={C:08X} D={D:08X}")
        a0=(a0+A)&0xffffffff; b0=(b0+B)&0xffffffff
        c0=(c0+C)&0xffffffff; d0=(d0+D)&0xffffffff
        if show: print(f"Updated state: A={a0:08X} B={b0:08X} C={c0:08X} D={d0:08X}")
    return struct.pack("<4I",a0,b0,c0,d0).hex()

if __name__ == "__main__":
    text=input("Enter text: ")
    print("\nMD5 Message Digest:",md5(text))
