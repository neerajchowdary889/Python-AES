#!/usr/bin/python3
"""
This is taken as reference from https://gist.github.com/Alex-Zander/d050736f6896198afa2f94dcbc7e1a37
"""
from Crypto.Util.number import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from os import urandom


def encrypt(pt, key, iv):
    return (AES.new(key, AES.MODE_CBC, iv)).encrypt(pad(pt, 16))


def decrypt(ct, key, iv):
    return unpad((AES.new(key, AES.MODE_CBC, iv)).decrypt(ct), 16)


print(f"\n1. Encrypt\n2. Decrypt")

a = input("> ")

if a == "1":
    pt = input("Enter text to encrypt: ").encode()
    key, iv = [urandom(16) for i in range(2)]

    ct = encrypt(pt, key, iv)

    print(f"\ncipher: {ct.hex()}\nKey: {key.hex()}\nIV: {iv.hex()}")

elif a == "2":
    a = ["Text to decrypt: ", "key: ", "IV: "]
    ct, key, iv = [bytes.fromhex(input(i)) for i in a]

    pt = decrypt(ct, key, iv)

    print(f"\nText: {pt}")

else:
    print("Incorrect Input")