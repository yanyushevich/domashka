def filter_by_currency(transactions, currency):
    """функция принимает на вход список словарей, представляющих транзакции
и возвращает итератор, который поочередно выдает транзакции,
где валюта операции соответствует заданной"""
    chepa = (data for data in transactions if data["operationAmount"]["currency"]["code"] == currency)
    for dat in chepa:
        yield dat

#if __name__ == '__main__':



def transaction_descriptions(transactions):
    """генератор принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
"""
    otvet = (i.get("description") for i in transactions if i.get("description"))
    for specif in otvet:
       yield specif


def card_number_generator(start, stop):
    """генератор card_number_generator
, который выдает номера банковских карт в формате
XXXX XXXX XXXX XXXX
, где
X
 — цифра номера карты"""
    numbers = "0000000000000000"
    dlina = len(str(start))
    true_dlina = len(numbers) - dlina
    i = start
    while i <= stop:
        true_start = "0" * true_dlina + str(start)
        yield true_start[:4] + ' ' + true_start[4:8] + ' ' + true_start[8:12] + ' ' + true_start[-4:]
        start += 1
        i += 1
