def filter_by_state(list_dictionaries:list, value:str = "EXECUTED") ->list:
    """функция принимает список словарей и опционально значение для ключа state и
    возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению."""
    true_list = list()
    for dictionar in list_dictionaries:
        if dictionar['state'] == value:
            true_list.append(dictionar)
    return true_list
