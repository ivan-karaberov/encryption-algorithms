import random

class KeyGenerator:
    def generate_private_key(self, w_size: int = 8) -> list[int]:
        """Генерация сверхвозрастающей последовательности"""
        cur_sum = 0
        key = []
        for _ in range(w_size):
            next_number = random.randint(cur_sum + 1, cur_sum + 2)
            key.append(next_number)
            cur_sum += next_number
        return key

    def generate_public_key(self, q: int, r: int, private_key: list[int]) -> list[int]:
        """Генерация открытого ключа"""
        return [(r * w) % q for w in private_key]

    def generate_q_and_r(self, private_key: list[int]) -> tuple[int, int]:
        """Генерация числа q и поиск взаимнопростого к нему числа r"""
        q = sum(private_key) + 1
        r = self.get_coprime(q)
        return q, r

    def get_coprime(self, num: int) -> int:
        """Нахождение взаимно простого числа к num в диапазоне от num до 1"""
        for i in range(num, 1, -1):
            if self.gcd(num, i) == 1:
                return i

    def gcd(self, p: int, q: int) -> int:
        """Нахождение наибольшего общего делителя двух чисел"""
        while q != 0:
            p, q = q, p % q
        return p

class MerkleHellmanCipher:
    def __init__(self, q: int, r: int, public_key: list[int], private_key: list[int]) -> None:
        self.q = q
        self.r = r
        self.private_key = private_key
        self.public_key = public_key
        self.w_size = len(self.public_key)

    def encode(self, message: str) -> str:
        """Кодирование сообщения"""
        result = []
        for ch in message:
            num = 0
            for i, sym in enumerate(self.__prepare_sum(ch)):
                if sym == '1':
                    num += self.public_key[i]
            result.append(num)
        return "".join([chr(s) for s in result])
    
    def decode(self, cipher_text: str) -> str:
        """Расшифровка сообщения"""
        q = self.q
        
        # Поиск обратного числа для r по модулю q
        gcd_val, _, reverse_r = self.__extended_gcd(q, self.r)
        
        if gcd_val != 1:
            raise ValueError("r не имеет обратного по модулю q.")
        
        # Приводим reverse_r к положительному значению
        reverse_r = reverse_r % q

        res = ""
        for ch in cipher_text:
            dec = 0
            dec_num = (ord(ch) * reverse_r) % q

            for i in range(len(self.private_key)-1, 0, -1):
                if self.private_key[i] <= dec_num:
                    dec |= 1 << (len(self.private_key) - i - 1)
                    dec_num -= self.private_key[i]
            res += chr(dec)
        
        return res

    def __prepare_sum(self, sym: str):
        return bin(ord(sym))[2:].zfill(self.w_size)

    def __extended_gcd(self, a: int, b: int) -> tuple[int, int, int]:
        """Расширенный алгоритм Евклида"""
        if b == 0:
            return a, 1, 0
        gcd, x1, y1 = self.__extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y


if __name__ == '__main__':
    key_generator = KeyGenerator()
    private_key = key_generator.generate_private_key(w_size=16)
    q, r = key_generator.generate_q_and_r(private_key=private_key)
    public_key = key_generator.generate_public_key(q, r, private_key)

    cipher = MerkleHellmanCipher(q, r, public_key, private_key)
    encode = cipher.encode("Hello World! Привет")
    decode = cipher.decode(encode)
    
    print(f"Зашифрованное сообщение: {encode}")
    print(f"Расшифрованное сообщение: {decode}")