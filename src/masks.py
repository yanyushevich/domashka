def get_mask_card_number(number_card: int) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    final_number = str(number_card)
    i = "** ****"
    if len(final_number) != 16:
        raise TypeError("Должно быть 16 цифр")
    chepa = final_number[:4]
    chepa_1 = final_number[4:6]
    chepa_2 = final_number[12:]
    final_super = chepa + " " + chepa_1 + i + " " + chepa_2
    return final_super


def get_mask_account(number_cheta: int) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    true_number_cheta = str(number_cheta)
    j = "**"
    if len(true_number_cheta) != 20:
        raise TypeError("Должно быть 20 цифр")
    last_numbers = true_number_cheta[-4:]
    final_number = j + last_numbers
    return final_number
