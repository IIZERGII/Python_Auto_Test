import pytest

from string_utils import StringUtils

string_util = StringUtils()

# Тест кейс 1: Проверяет, делает ли функция "capitalize" первую букву заглавной


@pytest.mark.parametrize(
    'string, result',
    [
        # positive test cases:
        ("peter", "Peter"),
        ("annMary", "Annmary"),
        ("mary Anne", "Mary anne"),
        ("ty'jan", "Ty'jan"),
        ("king1", "King1"),
        ("example-1", "Example-1"),
        # negative test cases:
        ("", ""),
        ("Steve", "Steve"),
        ("GPS", "Gps"),
        ("123abc", "123abc"),
        ("  leading space", "  leading space"),
        ("trailing space  ", "Trailing space  "),
        ("éxample", "Éxample"),  # другие алфавиты
    ],
)
def test_capitalize(string, result):
    string_util = StringUtils()
    print(f"Input string: {string}")
    print(f"Expected result: {result}")
    res = string_util.capitalize(string)
    print(f"Actual result: {res}")
    assert res == result


# Тест кейс 2: Проверяет, удаляет ли функция "trim" пустой пробел перед строкой


@pytest.mark.parametrize(
    'string, result',
    [
        # positive test cases:
        ("  dog", "dog"),
        (" ABC", "ABC"),
        ("  123  ", "123  "),
        (" Mary-Anne", "Mary-Anne"),
        ("   Peter1", "Peter1"),
        # negative test cases:
        ("", ""),
        ("ca t", "ca t"),
        ("monkey", "monkey"),
        ("123  ", "123  "),
        (1, 1),
        (0, 0),
    ],
)
def test_trim(string, result):
    string_util = StringUtils()
    print(f"Input string: {string}")
    print(f"Expected result: {result}")
    res = string_util.trim(string)
    print(f"Actual result: {res}")
    assert res == result


# Тест кейс 3: Проверяет, правильно ли функция "contains" проверяет, содержит ли строка символ


@pytest.mark.parametrize(
    'string, symbol, result',
    [
        # positive test cases:
        ("flower", "f", True),
        (" test", "t", True),
        ("space  ", "e", True),
        ("Mary-Anne", "-", True),
        ("123", "1", True),
        ("GPS", "P", True),
        ("", "", True),
        # negative test cases:
        ("City", "c", False),
        ("parameter", "P", False),
        ("hello", "x", False),
        ("hello", "!", False),
        ("hello", "", False),
        ("", "x", False),
        ("hello", "xyz", False),
    ],
)
def test_contains(string, symbol, result):
    string_util = StringUtils()
    print(f"Input string: {string}")
    print(f"Inputed symbol: {symbol}")
    print(f"Expected result: {result}")
    res = string_util.contains(string, symbol)
    print(f"Actual result: {res}")
    assert res == result


# Тест кейс 4: Проверяет, удаляет ли функция "delete_symbol" указанный символ


@pytest.mark.parametrize(
    'string, symbol, result',
    [
        # positive test cases:
        ("test", "t", "es"),
        ("Street", "r", "Steet"),
        ("Mountain", "M", "ountain"),
        ("123", "1", "23"),
        ("Mary-Anne", "-", "MaryAnne"),
        ("Sky Pro", "", "SkyPro"),
        ("plate", "pla", "te"),
        # negative test cases:
        ("spoon", "k", "spoon"),
        ("", "", ""),
        ("", "g", ""),
        ("milk", "", "milk"),
        ("park ", "", "park"),
        ("carpet  ", "r", "capet  "),
    ],
)
def test_delete_symbol(string, symbol, result):
    string_util = StringUtils()
    res = string_util.delete_symbol(string, symbol)
    assert res == result
