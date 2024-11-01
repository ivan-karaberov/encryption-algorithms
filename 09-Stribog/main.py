from stribog import Stribog
from rsa import generate_keys
from signature import signing, verify
from utils import read_from_file

def main():
    public_key, secret_key, mod = generate_keys(31231, 34673)
    data = read_from_file('data/test.txt').encode()
    stribog = Stribog(data)
    hashed_data = stribog.hash()
    signature = signing(hashed_data, public_key, mod)
    v = verify(data, signature, secret_key, mod)

    print(
        f"""
            Document hash > {hashed_data}

            Document ecp > {signature}
            
            Document verify > {v}
        """
    )

if __name__ == '__main__':
    main()