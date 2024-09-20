import string
from collections import Counter


def cipher(text: str, shift: int) -> str:
    """Смещает каждую букву в тексте на заданный сдвиг"""
    cipher_text = ''
    for sym in text:
        if sym.isalpha():
            cipher_text += chr((ord(sym) - ord('а') + shift) % 32 + ord('а'))
        else:
            cipher_text += sym
    return cipher_text


def analyze_frequency(raw_text: str) -> dict[str, int]:
    """Возвращает частоту встречи символов"""
    text = raw_text.translate(str.maketrans("", "", string.punctuation))
    text = text.replace(" ", "").lower()
    return sorted(Counter(text).items(), key=lambda x: x[1], reverse=True)


def get_shift(symbol: str) -> int:
    """Возвращает наиболее вероятный сдвиг"""
    return ord('о')-ord(symbol)


if __name__ == "__main__":
    text = ""
    with open('text.txt', encoding='utf-8') as f:
        text = ''.join(f.readlines())

    cipher_text = cipher(text, 1)
    shift = get_shift(analyze_frequency(cipher_text)[0][0])
    print(cipher(cipher_text, shift))