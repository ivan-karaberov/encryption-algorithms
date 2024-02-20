import pytest

from main import TrisemusCipher


@pytest.mark.parametrize(
    "test_message, expected",
    [
        ("Привет мир", "чшркнъ фрш"),
        ("Один Два Три", "цмрх мки ъшр"),
        ("Проверка, 34 число", "чшцкншти, 34 ярщуц")
    ]
)
def test_encode(test_message, expected):
    cipher = TrisemusCipher()
    assert cipher.encode(test_message) == expected


@pytest.mark.parametrize(
    "test_message, expected",
    [
        ("Космос", "чъйщъй"),
        ("Один Два Три", "ъпгб пдл кзг"),
        ("Проверка, 34 число", "ызъджзчл, 34 ягйшъ")
    ]
)
def test_encode_with_key(test_message, expected):
    cipher = TrisemusCipher("Университет")
    assert cipher.encode(test_message) == expected


@pytest.mark.parametrize(
    "test_message, expected",
    [
        ("фцуцтц", "молоко"),
        ("эунй щ фищуцф", "хлеб с маслом"),
        ("чцша 911", "порш 911")
    ]
)
def test_decode(test_message, expected):
    cipher = TrisemusCipher()
    assert cipher.decode(test_message) == expected


@pytest.mark.parametrize(
    "test_message, expected",
    [
        ("гчзл", "икра"),
        ("ызгжэлш д 3 ялйл", "приехал в 3 часа"),
        ("ьгшещ гпжк д чгбъкжлкзж", "фильм идет в кинотеатре")
    ]
)
def test_decode_with_key(test_message, expected):
    cipher = TrisemusCipher("Университет")
    assert cipher.decode(test_message) == expected


@pytest.mark.parametrize(
    "expected",
    [
        (
            ['г', 'р', 'е', 'ч', 'к', 'а', 'б', 'в',
             'д', 'ж', 'з', 'и', 'й', 'л', 'м', 'н',
             'о', 'п', 'с', 'т', 'у', 'ф', 'х', 'ц',
             'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
        )
    ]
)
def test_generate_encryption_table(expected):
    assert TrisemusCipher("Гречка").generate_encryption_table() == expected
