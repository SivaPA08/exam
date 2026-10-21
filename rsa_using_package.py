# RSA with the PyCryptodome package; use OAEP for encryption.
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def generate_keypair(bits=2048):
    key=RSA.generate(bits)
    return key, key.publickey()

def encrypt_bytes(data, public_key):
    return PKCS1_OAEP.new(public_key).encrypt(data)

def decrypt_bytes(ciphertext, private_key):
    return PKCS1_OAEP.new(private_key).decrypt(ciphertext)

if __name__=="__main__":
    private,public=generate_keypair()
    text=input("Enter text: ").encode()
    print("Algorithm: RSA-OAEP with SHA-1 default in PyCryptodome")
    print("Modulus size:",private.size_in_bits(),"bits")
    print("Public exponent e:",public.e)
    print("Plaintext bytes:",text.hex().upper())
    c=encrypt_bytes(text,public)
    print("Ciphertext hex:",c.hex().upper())
    print("Decrypted bytes:",decrypt_bytes(c,private).hex().upper())
    print("Decrypted:",decrypt_bytes(c,private).decode())
