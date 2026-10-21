import hashlib

if __name__ == "__main__":
    text=input("Enter text: ")
    data=text.encode("utf-8")
    print("Original text:",repr(text))
    print("UTF-8 bytes (hex):",data.hex().upper())
    print("Message length (bytes):",len(data))
    print("Message length (bits):",len(data)*8)
    print("\n========== PACKAGE DIGESTS ==========")
    print("SHA-1:",hashlib.sha1(data).hexdigest())
    print("MD5:",hashlib.md5(data).hexdigest())
    print("SHA-256:",hashlib.sha256(data).hexdigest())
    print("Note: hashlib returns the final digest; internal compression rounds are not exposed.")
