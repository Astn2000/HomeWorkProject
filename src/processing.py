def filter_by_state(my_list: list, state: str = "EXECUTED") -> list:
    """Функция обрабатывает список словарей , опционально использет ключ 'state'"""
    if my_list == []:
        raise ValueError("Список пуст")
    new_list = list()
    for list_ in my_list:
        status = list_.get("state")
        if state == status:
            new_list.append(list_)
    return new_list


def sort_by_date(list_dict: list, optional_parameter: bool = True) -> list:
    """Функция сортирующая словари по дате"""
    if list_dict == []:
        raise ValueError("Некорректный или нестандартный формат дат")
    sorted_list = sorted(list_dict, key=lambda date: date["date"], reverse=optional_parameter)
    return sorted_list


# if __name__ == "__main__":
#     print(
#         filter_by_state(
#             [
#                 {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#                 {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#                 {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#                 {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#             ],
#             "CANCELED",
#         )
#     )
#     print(
#         sort_by_date(
#             [
#                 {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#                 {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#                 {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#                 {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#             ]
#         )
#     )
