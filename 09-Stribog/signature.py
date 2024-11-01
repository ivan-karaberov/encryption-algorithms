from stribog import Stribog
from rsa import encode, decode

def signing(hashed_data: str, public_key: str, mod):
    return encode(hashed_data, public_key, mod)

def verify(data: str, signature, secret_key, mod):
    stribog = Stribog(data)
    hash = stribog.hash()
    hash_2 = decode(signature, secret_key, mod)
    return hash == hash_2