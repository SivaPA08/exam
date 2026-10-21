CRYPTography LAB PYTHON FILES

Files:
- caesar.py
- playfair.py
- vigenere.py
- autokey.py
- one_time_pad.py
- rail_fence.py
- row_transposition.py (single and double transposition)
- monoalphabetic.py
- polyalphabetic.py
- hill_cipher.py
- diffie_hellman.py
- ecc.py (small educational curve parameters from the lab style)
- rsa.py (textbook RSA for small integer lab examples)
- rsa_using_package.py
- des.py (complete single-block DES implementation)
- des_using_package.py
- double_des.py
- triple_des.py
- aes_using_package.py
- sha1.py (from-scratch SHA-1)
- md5.py (from-scratch MD5)
- digest_using_package.py

Install dependency for package-based block ciphers and package RSA:
    python -m pip install pycryptodome

Run any standalone script:
    python caesar.py

Notes:
- Classical ciphers, textbook RSA, small-curve ECC, DES, ECB and 3DES are educational examples, not secure modern designs.
- AES example uses CBC and a random IV; this is for demonstrating encryption/decryption, not a complete authenticated-encryption system.
- DES uses an 8-byte block and 8-byte key; the standalone implementation accepts one block only.
- Digest examples are SHA-1 and MD5 because those appear in the lab reports. Use SHA-256 for modern non-password hashing.


INTERMEDIATE RESULTS (UPDATED)
------------------------------
The scripts now print intermediate values where the algorithm/package exposes them.
- DES: round keys, IP, L/R, E expansion, XOR, S-box, P-box, each round, FP.
- Double DES: padded plaintext, first-stage ciphertext, final ciphertext and reverse intermediate.
- Triple DES package: padded bytes and ciphertext blocks; package does not expose internal DES rounds.
- AES (`aes.py`): AES-128 key expansion and every SubBytes/ShiftRows/MixColumns/AddRoundKey stage for encryption and decryption. AES package: plaintext/padded bytes, IV, CBC XOR inputs and ciphertext blocks; PyCryptodome does not expose AES round internals.
- SHA-1/MD5: padded message, message words, round checkpoints, updated state and digest.
- DH/ECC/RSA: public parameters, key calculations, public values and shared secret/encryption arithmetic.
- Classical ciphers: key streams, prepared text, Playfair matrix, Hill pairs, transposition matrix/order, and round-trip results.

DES, AES-CBC, and textbook RSA settings here are for lab demonstration only, not production security.

AES IMPLEMENTATIONS
-------------------
aes.py             AES-128 from scratch, one 16-byte block, round-by-round trace.
aes_using_package.py  AES-CBC using PyCryptodome (message-oriented, with padding and IV).
double_aes.py      Double AES-128: E(K2, E(K1, P)), with both AES round traces.
triple_aes.py      Triple AES-128 in EDE form: E(K3, D(K2, E(K1, P))), with traces.

The educational from-scratch AES scripts use exactly one 16-byte plaintext block
and 16-byte keys. They do not add padding or implement a secure message mode.
Double/triple AES here are lab demonstrations, not standard recommended encryption
schemes; use authenticated encryption such as AES-GCM for real applications.
Run from this directory so `from aes import ...` resolves correctly:
  python aes.py
  python double_aes.py
  python triple_aes.py
