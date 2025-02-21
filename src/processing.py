from typing import Any, Tuple


def filter_by_state(transactions_by_state: list[dict[str, Any]]) -> Tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Функция принимает список словарей и возвращает список с ключом выбранного значения"""
    new_list1 = []
    new_list2 = []
    for i in transactions_by_state:
        if i.get('state') == 'EXECUTED':
            new_list1.append(i)
        else:
            new_list2.append(i)
    return new_list1, new_list2


list_1, list_2 = filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                 {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                 {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])
# print(list_1)


def sort_by_date(transactions_by_date: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """Функция принимает список словарей и возвращает список, отсортированный по дате"""
    return sorted(transactions_by_date, key=lambda x: x["date"], reverse=reverse)


list_1 = sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])
# print(list_1)
