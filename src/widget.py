from src.masks import get_mask_card_number, get_mask_account
def mask_account_card(name_and_number):
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
    #print(name_card)
    if len(number_card) == 16:
        final_result = name_card + get_mask_card_number(int(number_card))
    else:
        final_result = name_card + get_mask_account(int(number_card))
    return final_result

def get_date(date_and_time):
    date_sample = "ДД.ММ.ГГГГ"
