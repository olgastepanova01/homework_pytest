from typing import Optional

import pytest
from src.widget import mask_account_card, get_date


# Фикстуры для подготовки тестовых данных для функции mask_account_card
@pytest.fixture
def valid_card_visa() -> str:
    return "Visa Platinum 7000792289606361"


@pytest.fixture
def valid_card_maestro() -> str:
    return "Maestro 1234567890123456"


@pytest.fixture
def valid_account() -> str:
    return "Счет 73654108430135874305"


@pytest.fixture
def invalid_input() -> str:
    return "Invalid Input 1234"


@pytest.fixture
def empty_string() -> str:
    return ""


# Параметризация для тестирования сценариев функции mask_account_card
@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1234567890123456", "Maestro 1234 56** **** 3456"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Invalid Input 1234", None),
        ("", None),
    ],
)
def test_mask_account_card(input_data: str, expected: Optional[str]) -> None:
    """Тестируем функцию mask_account_card с различными входными данными."""
    result = mask_account_card(input_data)
    assert result == expected, f"Ожидалось: {expected}, получено: {result}"


# Тесты с использованием фикстур
def test_valid_card_visa(valid_card_visa: str) -> None:
    result = mask_account_card(valid_card_visa)
    assert result == "Visa Platinum 7000 79** **** 6361"


def test_valid_card_maestro(valid_card_maestro: str) -> None:
    result = mask_account_card(valid_card_maestro)
    assert result == "Maestro 1234 56** **** 3456"


def test_valid_account(valid_account: str) -> None:
    result = mask_account_card(valid_account)
    assert result == "Счет **4305"


def test_invalid_input(invalid_input: str) -> None:
    result = mask_account_card(invalid_input)
    assert result is None


def test_empty_string(empty_string: str) -> None:
    result = mask_account_card(empty_string)
    assert result is None


# Фикстуры для подготовки тестовых данных для функции get_date
@pytest.fixture
def valid_date() -> str:
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def invalid_date_format() -> str:
    return "2024/03/11T02:26:18.671407"


@pytest.fixture
def null_string() -> str:
    return ""


# Параметризация для тестирования сценариев функции get_date
@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-12-31T23:59:59.999999", "31.12.2023"),
        ("2024-01-01T00:00:00.000000", "01.01.2024"),
        ("2024-02-29T12:34:56.789012", "29.02.2024"),
        ("2024/03/11T02:26:18.671407", None),
        ("", None),
    ],
)
def test_get_date(input_data: str, expected: Optional[str]) -> None:
    """Тестируем функцию get_date с различными входными данными."""
    if expected is not None:
        result = get_date(input_data)
        assert result == expected, f"Ожидалось: {expected}, получено: {result}"
    else:
        with pytest.raises(ValueError):
            get_date(input_data)


# Тесты с использованием фикстур
def test_valid_date(valid_date: str) -> None:
    result = get_date(valid_date)
    assert result == "11.03.2024"


def test_invalid_date_format(invalid_date_format: str) -> None:
    with pytest.raises(ValueError):
        get_date(invalid_date_format)


def test_null_string(null_string: str) -> None:
    with pytest.raises(ValueError):
        get_date(null_string)
