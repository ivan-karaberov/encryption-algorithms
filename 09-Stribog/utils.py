from codecs import getdecoder, getencoder

_hexdecoder = getdecoder("hex")
_hexencoder = getencoder("hex")

def hexdec(data):
    return _hexdecoder(data)[0]

def hexenc(data):
    return _hexencoder(data)[0].decode("ascii")

def strxor(a, b) -> bytes:
    min_len = min(len(a), len(b))
    a = bytearray(a)
    b = bytearray(b)
    xor = bytearray(min_len)
    for i in range(min_len):
        xor[i] = a[i] ^ b[i]
    return bytes(xor)

def read_from_file(path: str) -> str:
    data = ""
    with open(path, "r", encoding='utf-8') as file:
        while line := file.readline():
            data += line
    return data