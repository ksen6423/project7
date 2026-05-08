from datetime import datetime

from src.banking_processes import process_bank_search
from src.file_operations import reading_csv_file, reading_excel_file
from src.generators import filter_by_currency
from src.masks import get_mask_account
from src.processing import filter_by_state, sort_by_date
from src.utils import read_json_file


def main():
    """
    Функция, отвечающая за основную логику проекта и связывающая функциональности между собой.
    """
    while True:
        print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")

        user_choice = input().strip()

        if user_choice == "1":
            file_json_path = 'data/operation.json'
            transactions = read_json_file(file_json_path)
            print('Был выбран JSON')
            break
        elif user_choice == "2":
            file_csv_path = 'data/transactions (1).csv'
            transactions = reading_csv_file(file_csv_path)
            print('Был выбран CSV')
            break
        elif user_choice == "3":
            file_excel_path = 'data/transactions_excel.xlsx'
            transactions = reading_excel_file(file_excel_path)
            print('Был выбран XLSX')
            break
        else:
            print(f'Данный выбор {user_choice} не доступен')
            continue

    while True:
        print('Введите статус, по которому необходимо выполнить фильтрацию.')
        print('Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')
        status = ['EXECUTED', 'CANCELED', 'PENDING']
        user_status_choice = input().upper().strip()
        if user_status_choice in status:
            status_filter = user_status_choice
            print(f'Был выбран статус: {status_filter}')
            ft = filter_by_state(transactions, status_filter)
            break
        else:
            print(f'Статус операции {user_status_choice} недоступен')
            continue

    while True:
        sort_by_date_choice = input("Отсортировать операции по дате? Да/Нет\n").strip().lower()
        if sort_by_date_choice == 'да':
            order_choice = input('Отсортировать по возрастанию или по убыванию?\n').strip().lower()
            if order_choice == 'по возрастанию':
                ft = sort_by_date(ft, reverse_order=False)  # Сортировка по возрастанию
                break
            elif order_choice == 'по убыванию':
                ft = sort_by_date(ft, reverse_order=True)  # Сортировка по убыванию
                break
            else:
                print("Некорректный выбор. Введите 'по возрастанию' или 'по убыванию'.")  # Сообщение об ошибке
                continue  # Повторяем запрос
        elif sort_by_date_choice == 'нет':
            break
        else:
            print("Некорректный выбор. Введите 'Да' или 'Нет'.")  # Сообщение об ошибке
            continue

    while True:
        currency_choice = input('Выводить только рублевые транзакции? Да/Нет\n').strip().lower()
        if currency_choice in ("да", "нет"):
            if currency_choice.lower() == "да" and user_choice in ['2', '3']:
                ft = [t for t in ft if t.get("currency_code") == 'RUB']
                break
            elif currency_choice.lower() == "да" and user_choice == '1':
                ft = list(filter_by_currency(ft, 'RUB'))
                break
            if currency_choice.lower() == "нет":
                break

    while True:
        word_for_filter = input(
            'Отфильтровать список транзакций по определенному слову в описании? Да/Нет').strip().lower()
        if word_for_filter in ['да', 'нет']:
            if word_for_filter == 'да':
                filter_word = input('Введите слово:\n')
                ft = process_bank_search(ft, filter_word)
                break
            else:
                break
        else:
            continue

    print(f"Распечатываю итоговый список транзакций...{ft} ")
    print(f"Всего банковских операций в списке: {len(ft)}")

    for transaction in ft:
        date_str = transaction.get("date", "")
        try:
            date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y %H:%M")
        except (ValueError, TypeError):
            date = "Неизвестная дата"

        description = transaction.get("description", "Без описания")
        from_account = get_mask_account(transaction.get("from", "")) or "Неизвестно"
        to_account = get_mask_account(transaction.get("to", "")) or "Неизвестно"

    # Получаем сумму и валюту
        amount = transaction.get("amount", transaction.get("operationAmount", {}).get("amount", "Неизвестно"))
        currency = transaction.get("currency_code",
                                       transaction.get("operationAmount", {}).get("currency", {}).get("name", "Неизвестно"))
        print(f"{date} {description}")
        print(f"{from_account} -> {to_account}")
        print(f"Сумма: {amount} {currency}")
        print()


if __name__ == "__main__":
    main()
