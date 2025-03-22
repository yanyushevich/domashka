from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(name_and_number: str) -> str:
    """Фуекция принимает строку содержащую тип и номер карты и возвращает строку
    с замаскированным номером"""
    final_result = str()
    name_card = str()
    number_card = str()
    for name in name_and_number:
        if name.isdigit():
            number_card += name
        else:
            name_card += name
    # print(name_card)
    if len(number_card) == 16:
        final_result = name_card + get_mask_card_number(int(number_card))
    elif len(number_card) == 20:
        final_result = name_card + get_mask_account(int(number_card))
    else:
        raise TypeError("Должно быть 20 или 16 цифр")
    return final_result


def get_date(date_and_time: str) -> str:
    if len(date_and_time) < 10:
        raise TypeError("Введите корректную дату")
    final_result = date_and_time[8:10] + "." + date_and_time[5:7] + "." + date_and_time[0:4]
    return final_result
