from typing import Optional, Union

import pytest
from src.masks import get_mask_card_number, get_mask_account


# Фикстуры для подготовки тестовых данных для функции get_mask_card_number
@pytest.fixture
def valid_card_number() -> str:
    return "7000792289606361"


@pytest.fixture
def invalid_card_number_len_short() -> str:
    return "1234"


@pytest.fixture
def invalid_card_number_len_long() -> str:
    return "12345678901234567890"


@pytest.fixture
def non_digit_card_number() -> str:
    return "7000abc289606361"


@pytest.fixture
def empty_string() -> str:
    return ""


# Параметризация для тестирования сценариев функции get_mask_card_number
@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79 ** **** 6361"),
        ("1234567890123456", "1234 56 ** **** 3456"),
        ("1234", None),
        ("12345678901234567890", None),
        ("7000abc289606361", None),
        ("", None),
        (7000792289606361, "7000 79 ** **** 6361"),
    ],
)
def test_get_mask_card_number(card_number: Union[str, int], expected: Optional[str]) -> None:
    """Тестируем функцию get_mask_card_number с различными входными данными."""
    result = get_mask_card_number(card_number)
    assert result == expected, f"Ожидалось: {expected}, получено: {result}"


# Тесты с использованием фикстур
def test_valid_card_number(valid_card_number: str) -> None:
    result = get_mask_card_number(valid_card_number)
    assert result == "7000 79 ** **** 6361"


def test_invalid_card_number_len_short(invalid_card_number_len_short: str) -> None:
    result = get_mask_card_number(invalid_card_number_len_short)
    assert result is None


def test_invalid_card_number_len_long(invalid_card_number_len_long: str) -> None:
    result = get_mask_card_number(invalid_card_number_len_long)
    assert result is None


def test_non_digit_card_number(non_digit_card_number: str) -> None:
    result = get_mask_card_number(non_digit_card_number)
    assert result is None


def test_empty_string(empty_string: str) -> None:
    result = get_mask_card_number(empty_string)
    assert result is None


# Фикстуры для подготовки тестовых данных для функции get_mask_account
@pytest.fixture
def valid_account_number() -> str:
    return "73654108430135874305"


@pytest.fixture
def invalid_account_number_short() -> str:
    return "1234"


@pytest.fixture
def invalid_account_number_long() -> str:
    return "123456789012345678901234"


@pytest.fixture
def non_digit_account_number() -> str:
    return "7365410843013587430a"


@pytest.fixture
def non_number_account_number() -> str:
    return "7365410843013587430a"


@pytest.fixture
def null_string() -> str:
    return ""


# Параметризация для тестирования сценариев функции get_mask_account
@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("73654108430135874305", "**4305"),
        ("12345678901234567890", "**7890"),
        ("1234", None),
        ("123456789012345678901234", None),
        ("7365410843013587430a", None),
        ("", None),
        (73654108430135874305, "**4305"),
    ],
)
def test_get_mask_account(account_number: Union[str, int], expected: Optional[str]) -> None:
    """Тестируем функцию get_mask_account с различными входными данными."""
    result = get_mask_account(account_number)
    assert result == expected, f"Ожидалось: {expected}, получено: {result}"


# Тесты с использованием фикстур
def test_valid_account_number(valid_account_number: str) -> None:
    result = get_mask_account(valid_account_number)
    assert result == "**4305"


def test_invalid_account_number_short(invalid_account_number_short: str) -> None:
    result = get_mask_account(invalid_account_number_short)
    assert result is None


def test_invalid_account_number_long(invalid_account_number_long: str) -> None:
    result = get_mask_account(invalid_account_number_long)
    assert result is None


def test_non_number_account_number(non_number_account_number: str) -> None:
    result = get_mask_account(non_number_account_number)
    assert result is None


def test_null_string(null_string: str) -> None:
    result = get_mask_account(null_string)
    assert result is None
