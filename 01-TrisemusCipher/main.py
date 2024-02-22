russian_alphabet = [
    "а", "б", "в", "г", "д", "е", "ж", "з",
    "и", "й", "к", "л", "м", "н", "о", "п",
    "р", "с", "т", "у", "ф", "х", "ц", "ч",
    "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"
]


def remove_duplicate_letter(word: str) -> list[str]:
    res = list()
    for letter in word:
        if letter not in res:
            res.append(letter)
    return ''.join(res)


class TrisemusCipher:
    def __init__(
        self,
        key: str = "",
        alphabet: list[str] = russian_alphabet,
        line_size=8
    ) -> None:
        self.key = key
        self.alphabet = alphabet
        self.line_size = line_size

    def encode(self, message: str) -> str:
        return self.transform_message(message, 0)

    def decode(self, message: str) -> str:
        return self.transform_message(message, 1)

    def transform_message(self, message: str, status: int) -> str:
        '''
            message encoding/decoding function
            status:
                0 - encode
                1 - decode
        '''
        encryption_table = self.generate_encryption_table()

        res_str = list()
        for symbol in message.lower():
            if symbol in encryption_table:
                symbol = self.shift_letter(symbol, encryption_table, status)
            res_str.append(str(symbol))

        return ''.join(res_str)

    def generate_encryption_table(self) -> list[str]:
        ''' Creatng a table for encryption '''
        key = remove_duplicate_letter(self.key).lower()
        return list(key) + [i for i in self.alphabet if i not in key]

    def shift_letter(
        self,
        letter: str,
        encryption_table: list[str],
        status: int
    ) -> str:
        '''
        Offset a letter by line_size
        status:
            0 - forward
            1 - ago
        '''
        line_size = self.line_size*(-1 if status else 1)
        letter_index = encryption_table.index(letter)
        shift_index = (letter_index+(line_size)) % len(encryption_table)
        return encryption_table[shift_index]
