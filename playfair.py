def build_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    chars = []
    for ch in (key.upper() + alphabet):
        if ch.isalpha():
            ch = "I" if ch == "J" else ch
            if ch in alphabet and ch not in chars:
                chars.append(ch)
    return [chars[i:i+5] for i in range(0, 25, 5)]

def prepare(text):
    s = "".join("I" if c == "J" else c for c in text.upper() if c.isalpha())
    out, i = [], 0
    while i < len(s):
        a = s[i]
        if i + 1 >= len(s):
            out.extend([a, "X"]); i += 1
        elif s[i+1] == a:
            out.extend([a, "X"]); i += 1
        else:
            out.extend([a, s[i+1]]); i += 2
    return "".join(out)

def transform(text, key, decrypt=False):
    matrix = build_matrix(key)
    pos = {matrix[r][c]: (r, c) for r in range(5) for c in range(5)}
    s = prepare(text) if not decrypt else "".join("I" if c == "J" else c for c in text.upper() if c.isalpha())
    if len(s) % 2: s += "X"
    out = []
    step = -1 if decrypt else 1
    for i in range(0, len(s), 2):
        a, b = s[i], s[i+1]
        r1, c1 = pos[a]; r2, c2 = pos[b]
        if r1 == r2:
            out.extend([matrix[r1][(c1+step)%5], matrix[r2][(c2+step)%5]])
        elif c1 == c2:
            out.extend([matrix[(r1+step)%5][c1], matrix[(r2+step)%5][c2]])
        else:
            out.extend([matrix[r1][c2], matrix[r2][c1]])
    return "".join(out)

def encrypt(text, key): return transform(text, key, False)
def decrypt(text, key): return transform(text, key, True)

if __name__ == "__main__":
    key = input("Enter key: ")
    text = input("Enter plaintext: ")
    print("Key matrix:")
    for row in build_matrix(key): print(" ".join(row))
    print("Prepared digraph text:",prepare(text))
    c = encrypt(text, key)
    print("Encrypted:", c)
    print("Decrypted (may retain filler X):", decrypt(c, key))
