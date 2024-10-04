import struct


class Salsa20:
    def __init__(self) -> None:
        self.__CONST_EXPAND = b'expand 32-byte k'
        self.__block_size = 64
        self.__mod32 = 0xffffffff

    def encrypt(self, data: str, key: str, iv: str) -> str:
        """Шифрование/расшифрование данных"""
        res = ''
        for i in range(0, len(data), self.__block_size):
            block = data[i : i + self.__block_size]
            gen_key = self.__generate_key(
                key=key.encode('utf-8'),
                iv=iv.encode('utf-8'),
                counter=i//self.__block_size   
            )

            res += ''.join([chr(ord(block[x]) ^ gen_key[x]) for x in range(len(block))])
        
        return res

    def __generate_key(self, key: bytes, iv: bytes, counter: int = 0) -> bytes:
        """Возвращает заданный блок ключа"""
        if len(key) != 32 or len(iv) != 8:
            raise ValueError("Incorrect Values")

        initial_key = self.__initial_state_key(key, iv, counter)
        x = initial_key[:]

        for i in range(10):
            self.__QR(x, 0, 4, 8, 12)
            self.__QR(x, 5, 9, 13, 1)
            self.__QR(x, 10, 14, 2, 6)
            self.__QR(x, 15, 3, 7, 11)

            self.__QR(x, 0, 1, 2, 3)
            self.__QR(x, 5, 6, 7, 4)
            self.__QR(x, 10, 11, 8, 9)
            self.__QR(x, 15, 12, 13, 14)
        out = []
        
        for i in range(len(x)):
            out.append((initial_key[i] ^ x[i]) & self.__mod32)
        out = struct.pack('<16I',
                        out[0],  out[1],  out[2],  out[3],
                        out[4],  out[5],  out[6],  out[7],
                        out[8],  out[9],  out[10], out[11],
                        out[12], out[13], out[14], out[15])

        return out

    def __initial_state_key(self, key: bytes, iv: bytes, counter: int) -> bytes:
        """Вовзращает начальное состояние ключа"""
        iv = struct.unpack("<2I", iv)
        count = [counter >> 16, counter & 0xFFFF]
        const = struct.unpack("<4I", self.__CONST_EXPAND)
        k = struct.unpack("<8I", key)

        return [
            const[0], k[0],     k[1],     k[2],
            k[3],     const[1], iv[0], iv[1],
            count[1], count[0], const[2], k[4],
            k[5],     k[6],     k[7],     const[3]]

    def __QR(self, x: list, a: int, b: int, c: int, d: int):
        """Четверть раунда"""
        x[b] ^= self.__rol(self.__add_mod_32(x[a], x[d]), 7)
        x[c] ^= self.__rol(self.__add_mod_32(x[b], x[a]), 9)
        x[d] ^= self.__rol(self.__add_mod_32(x[c], x[b]), 13)
        x[a] ^= self.__rol(self.__add_mod_32(x[d], x[c]), 18)


    def __rol(self, a: int, n: int) -> int:
        """Циклический сдвиг влево"""
        n = n % (len(str(a))*8)
        t1 = a << n
        t2 = a >> (len(str(a))*8 - n)
        return t1 | t2;  


    def __add_mod_32(self, a: int, b: int) -> int:
        """Сложение двух чисел по модулю 2^32"""
        res = a + b
        return res - self.__mod32 if res >= self.__mod32 else res
