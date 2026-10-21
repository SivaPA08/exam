import struct

def left_rotate(x,n):
    return ((x<<n)|(x>>(32-n))) & 0xffffffff

def sha1(message, show=True):
    data=message.encode("utf-8"); bit_len=len(data)*8
    if show: print("Original message bytes:",data.hex().upper()); print("Original length (bits):",bit_len)
    data+=b"\x80"
    while len(data)%64!=56: data+=b"\x00"
    data+=struct.pack(">Q",bit_len)
    if show: print("Padded message:",data.hex().upper())
    h0,h1,h2,h3,h4=0x67452301,0xEFCDAB89,0x98BADCFE,0x10325476,0xC3D2E1F0
    for start in range(0,len(data),64):
        block=data[start:start+64]
        w=list(struct.unpack(">16I",block))
        for i in range(16,80): w.append(left_rotate(w[i-3]^w[i-8]^w[i-14]^w[i-16],1))
        if show:
            print(f"\nBlock at byte offset {start}: first 16 message words")
            for j in range(16): print(f"W[{j:2}] = {w[j]:08X}")
        a,b,c,d,e=h0,h1,h2,h3,h4
        for i in range(80):
            if i<20: f=(b&c)|((~b)&d); k=0x5A827999
            elif i<40: f=b^c^d; k=0x6ED9EBA1
            elif i<60: f=(b&c)|(b&d)|(c&d); k=0x8F1BBCDC
            else: f=b^c^d; k=0xCA62C1D6
            temp=(left_rotate(a,5)+f+e+k+w[i])&0xffffffff
            e,d,c,b,a=d,c,left_rotate(b,30),a,temp
            if show and (i+1) in (20,40,60,80): print(f"After Round {i+1}: A={a:08X} B={b:08X} C={c:08X} D={d:08X} E={e:08X}")
        h0=(h0+a)&0xffffffff; h1=(h1+b)&0xffffffff; h2=(h2+c)&0xffffffff
        h3=(h3+d)&0xffffffff; h4=(h4+e)&0xffffffff
        if show: print(f"Updated hash state: {h0:08X} {h1:08X} {h2:08X} {h3:08X} {h4:08X}")
    return f"{h0:08x}{h1:08x}{h2:08x}{h3:08x}{h4:08x}"

if __name__ == "__main__":
    text=input("Enter text: ")
    print("\nSHA-1 Message Digest:",sha1(text))
