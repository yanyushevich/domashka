def filter_by_state(list_dictionaries:list, value:str = "EXECUTED") ->list:
    """функция принимает список словарей и опционально значение для ключа state и
    возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению."""
    true_list = list()
    for dictionar in list_dictionaries:
        if dictionar['state'] == value:
            true_list.append(dictionar)
    return true_list

def sort_by_date(list_dictionaries_:list,sorting_direction:bool = True) -> list:
    """функция принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание) и  возвращать новый список, отсортированный по дате
"""
    final_list = list()
    final_list = sorted(list_dictionaries_, key = lambda value: value["date"], reverse = sorting_direction)
    return final_list
