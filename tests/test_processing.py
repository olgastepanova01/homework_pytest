import pytest
from src.processing import filter_by_state, sort_by_date
from typing import List, Dict, Any


# Фикстуры для подготовки тестовых данных для функции filter_by_state
@pytest.fixture
def transactions_with_executed_and_canceled() -> List[Dict[str, Any]]:
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    ]


@pytest.fixture
def transactions_only_executed() -> List[Dict[str, Any]]:
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    ]


@pytest.fixture
def transactions_only_canceled() -> List[Dict[str, Any]]:
    return [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    ]


@pytest.fixture
def empty_transactions() -> List[Dict[str, Any]]:
    return []


# Параметризация для тестирования сценариев функции filter_by_state
@pytest.mark.parametrize(
    "input_data, expected_executed, expected_canceled",
    [
        (
            [
                {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            ],
            [
                {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            ],
            [
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            ],
        ),
        (
            [
                {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            ],
            [
                {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            ],
            [],
        ),
        (
            [
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            ],
            [],
            [
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            ],
        ),
        ([], [], []),  # Пустой список
    ],
)
def test_filter_by_state(
    input_data: List[Dict[str, Any]],
    expected_executed: List[Dict[str, Any]],
    expected_canceled: List[Dict[str, Any]],
) -> None:
    """Тестируем функцию filter_by_state с различными входными данными."""
    executed, canceled = filter_by_state(input_data)
    assert executed == expected_executed, f"Ожидалось: {expected_executed}, получено: {executed}"
    assert canceled == expected_canceled, f"Ожидалось: {expected_canceled}, получено: {canceled}"


# Тесты с использованием фикстур
def test_filter_by_state_with_executed_and_canceled(
    transactions_with_executed_and_canceled: List[Dict[str, Any]],
) -> None:
    executed, canceled = filter_by_state(transactions_with_executed_and_canceled)
    assert len(executed) == 2
    assert len(canceled) == 2


def test_filter_by_state_only_executed(transactions_only_executed: List[Dict[str, Any]]) -> None:
    executed, canceled = filter_by_state(transactions_only_executed)
    assert len(executed) == 2
    assert len(canceled) == 0


def test_filter_by_state_only_canceled(transactions_only_canceled: List[Dict[str, Any]]) -> None:
    executed, canceled = filter_by_state(transactions_only_canceled)
    assert len(executed) == 0
    assert len(canceled) == 2


def test_filter_by_state_empty_list(empty_transactions: List[Dict[str, Any]]) -> None:
    executed, canceled = filter_by_state(empty_transactions)
    assert len(executed) == 0
    assert len(canceled) == 0


# Фикстуры для подготовки тестовых данных для функции sort_by_date
@pytest.fixture
def transactions_with_dates() -> List[Dict[str, Any]]:
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    ]


@pytest.fixture
def transactions_with_same_dates() -> List[Dict[str, Any]]:
    return [
        {'id': 1, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 2, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 3, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
    ]


@pytest.fixture
def transactions_with_invalid_dates() -> List[Dict[str, Any]]:
    return [
        {'id': 1, 'state': 'EXECUTED', 'date': 'invalid_date'},
        {'id': 2, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    ]


# Параметризация для тестирования сценариев функции sort_by_date
@pytest.mark.parametrize(
    "input_data, reverse, expected_dates",
    [
        (
            [
                {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            ],
            True,
            [
                '2019-07-03T18:35:29.512364',
                '2018-10-14T08:21:33.419441',
                '2018-09-12T21:27:25.241689',
                '2018-06-30T02:08:58.425572',
            ],
        ),
        (
            [
                {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            ],
            False,
            [
                '2018-06-30T02:08:58.425572',
                '2018-09-12T21:27:25.241689',
                '2018-10-14T08:21:33.419441',
                '2019-07-03T18:35:29.512364',
            ],
        ),
        (
            [
                {'id': 1, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 2, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 3, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
            ],
            True,
            [
                '2019-07-03T18:35:29.512364',
                '2019-07-03T18:35:29.512364',
                '2019-07-03T18:35:29.512364',
            ],
        ),
    ],
)
def test_sort_by_date(
    input_data: List[Dict[str, Any]], reverse: bool, expected_dates: List[str]
) -> None:
    """Тестируем функцию sort_by_date с различными входными данными."""
    sorted_data = sort_by_date(input_data, reverse=reverse)
    sorted_dates = [item["date"] for item in sorted_data]
    assert sorted_dates == expected_dates, (
        f"Ожидалось: {expected_dates}, получено: {sorted_dates}"
    )


# Тесты с использованием фикстур
def test_sort_by_date_with_same_dates(transactions_with_same_dates: List[Dict[str, Any]]) -> None:
    sorted_data = sort_by_date(transactions_with_same_dates, reverse=True)
    sorted_dates = [item["date"] for item in sorted_data]
    assert sorted_dates == [
        '2019-07-03T18:35:29.512364',
        '2019-07-03T18:35:29.512364',
        '2019-07-03T18:35:29.512364',
    ]
