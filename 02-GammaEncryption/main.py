import string


class IncorrectGamma(Exception):
    pass


class GammaEncryption:
    def __init__(
        self,
        gamma: str,
        alphabet: list[str] = [chr for chr in string.ascii_lowercase]
    ) -> None:
        self.gamma = gamma
        self.alphabet = alphabet

    def encode(self, message: str) -> str:
        return self.transform_message(message, 0)

    def decode(self, message: str) -> str:
        return self.transform_message(message, 1)

    def transform_message(self, message: str, mode: bool) -> str:
        '''
            message encoding/decoding
            mode:
                0 - encode
                1 - decode
        '''
        i = 0
        res = list()
        for symbol in message.lower():
            if symbol in self.alphabet:
                Si = self.alphabet.index(symbol)
                gamma_letter = self.gamma[i % len(self.gamma)].lower()
                if gamma_letter not in self.alphabet:
                    raise IncorrectGamma
                Gi = self.alphabet.index(gamma_letter) * (-1 if mode else 1)
                symbol = self.alphabet[(Si+Gi) % len(self.alphabet)]
                i += 1
            res.append(str(symbol))
        return "".join(res)
