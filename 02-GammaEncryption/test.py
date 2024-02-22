import pytest

from main import GammaEncryption


@pytest.mark.parametrize(
    "test_message, expected",
    [
        ("Hello World", "avlyg ezmlq"),
        ("I'm going to the cinema", "b'd gbavr oo gpe vznrei"),
        ("buy milk", "uly zatv")
    ]
)
def test_encode(test_message, expected):
    assert GammaEncryption("Transilvania").encode(test_message) == expected


@pytest.mark.parametrize(
    "test_message, expected",
    [
        ("avlyg ezmlq", "hello world"),
        ("b'd gbavr oo gpe vznrei", "i'm going to the cinema"),
        ("uly zatv", "buy milk")
    ]
)
def test_decode(test_message, expected):
    assert GammaEncryption("Transilvania").decode(test_message) == expected


@pytest.mark.parametrize(
    "test_message, expected",
    [
        ("Привет мир", "ыюурпа шцы"),
        ("Купил порше", "цбъцх эъюгу"),
        ("Молоко", "шьцьфь")
    ]
)
def test_change_alphabet(test_message, expected):
    russian_alphabet = [
        "а", "б", "в", "г", "д", "е", "ж", "з",
        "и", "й", "к", "л", "м", "н", "о", "п",
        "р", "с", "т", "у", "ф", "х", "ц", "ч",
        "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"
    ]
    assert GammaEncryption(
        "Молоко",
        alphabet=russian_alphabet
    ).encode(test_message) == expected
