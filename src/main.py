
from src.file_operations import reading_csv_file, reading_excel_file
from src.utils import read_json_file
from src.banking_processes import process_bank_search
from src.generators import filter_by_currency
from src.processing import sort_by_date
from src.masks import get_mask_account

def main():
    print(
       '''Привет! Добро пожаловать в программу работы 
       с банковскими транзакциями. 
       Выберите необходимый пункт меню:
       1. Получить информацию о транзакциях из JSON-файла
       2. Получить информацию о транзакциях из CSV-файла
       3. Получить информацию о транзакциях из XLSX-файла'''
    )

    result_exe = reading_excel_file(r"C:\Users\cfif\PycharmProjects\PythonProject8\data\transactions_excel.xlsx")
    result_csv = reading_csv_file(r"C:\Users\cfif\PycharmProjects\PythonProject8\data\transactions (1).csv")
    result_json = read_json_file(r"C:\Users\cfif\PycharmProjects\PythonProject8\data\operation.json")

    user_choose_file = int(input("Введите номер операции: "))
    print(
        '''Введите статус, по которому необходимо выполнить фильтрацию. 
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING'''
    )
    valid_statuses = ["executed", "canceled", "pending"]
    search = ""

    if user_choose_file == 1:
        data = result_json
    elif user_choose_file == 2:
        data = result_csv
    elif user_choose_file == 3:
        data = result_exe

    while search not in valid_statuses:
        search = input('Введите статус: \n').lower()
        if search not in valid_statuses:
            print(f'Статус операции "{search}" недоступен.')
            print('Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')
    result = process_bank_search(data, search)
    dicts_state = result
    dicts_state = process_bank_search(data, search)

    sort_by_data_choose = ""
    while sort_by_data_choose not in ["да", "нет"]:
        sort_by_data_choose = input("Отсортировать выбранные операции по дате? Да\Нет.").strip().lower()
        if sort_by_data_choose == "да":
            sort_by_order = input("Отсортировать по возрастанию или убыванию?").strip().lower()
            if sort_by_order == "по возрастанию":
                sort_order = False
                filter_order = sort_by_date(sort_order)
            elif sort_by_order == "по убыванию":
                sort_order = True
                filter_order = sort_by_date(sort_order)
                break
        elif sort_by_data_choose == "нет":
            break
    while True:
        sort_by_transaction_choose = input("Выводить только рублевые транзакции? Да\Нет.").strip().lower()
        if sort_by_transaction_choose == "да":
            sort_transaction = "RUB"
            if user_choose_file == "1":
                sort_currency = ["operationAmount", "currency", "code"]
            elif user_choose_file == "2":
                sort_currency = ["sort_transaction"]
            elif user_choose_file == "3":
                sort_currency = ["sort_transaction"]
            transactions_rub = list(filter_by_currency(sort_transaction, sort_currency))
        else:
            break
    while True:
        sort_by_word = input("Отфильтровать список транзакций по определенному слову в описании? Да\Нет.").strip().lower()
        if sort_by_word == "да":
            filter_word = input("Введите слово для транзакций по описанию.").strip()
            filter_transactions = process_bank_search(transactions_rub, filter_word)
        else:
            filter_transactions = transactions_rub

print("Распечатываю итоговый список транзакций...")
print("Всего банковских операций в списке: {len(filter_transactions)}")
transactions = [
    {'id': 407169720, 'state': 'EXECUTED', 'date': '2018-02-03T14:52:08.093722',
    'operationAmount': {'amount': '67011.26', 'currency': {'name': 'руб.', 'code': 'RUB'}},
    'description': 'Перевод с карты на карту', 'from': 'MasterCard 4047671689373225', 'to':
    'Maestro 3806652527413662'}
    ]
for transaction in transactions:
    date = sort_by_date(transaction["date"])
    description = transaction["description"]
    from_account = get_mask_account(transaction.get("from", ""))
    to_account = get_mask_account(transaction.get("to", ""))
    amount = transaction['operationAmount']['amount']
    currency = transaction['operationAmount']['currency']['name']

    print(f"{date}{description}")
    print(f"{from_account} -> {to_account}")
    print(f"Сумма: {amount}{currency}")

