class NotPrimeNumber(Exception):
    pass

# RSA CIPHER
def encode(message: str, open_key: int, mod: int):
    symbols = []
    for sym in message:
        symbols.append(ord(sym))
    string = ''
    for sym in symbols:
        string += str(cipher(sym, open_key, mod)) + ' '
    return string[:-1]

def decode(message: str, secret_key: int, mod: int):
    symbols = message.split(' ')
    string = ''
    for sym in symbols:
        string += chr(cipher(int(sym), secret_key, mod))
    return string

def cipher(symbol: int, key: int, mod: int):
    return pow(symbol, key, mod)


# RSA GET KEYS
ferma = [65537, 257, 17, 5, 3]

def generate_keys(p: int, q: int):
    if not is_prime(p) or not is_prime(q):
        raise NotPrimeNumber
    n = p*q
    euler = (p-1)*(q-1)
    e = get_coprime(euler)
    d = get_modulo_inverse(e, euler)
    return e, d, n

def is_prime(num: int):
    if num % 2 == 0:
        return num == 2
    d = 3
    while d * d <= num and num % d != 0:
        d += 2
    return d * d > num

def get_coprime(num: int):
    for n in ferma:
        if gcd(num, n) == 1:
            return n

def gcd(p: int, q: int):
    while q != 0:
        p, q = q, p % q
    return p

def get_modulo_inverse(a: int, m: int):
    return pow(a, -1, m)