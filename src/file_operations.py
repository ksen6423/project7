import pandas as pd


def reading_csv_file(file: str) -> list:
    """Функция чтения файла csv"""
    try:
        file_csv = pd.read_csv(file)
        return file_csv.to_dict('records')
    except FileNotFoundError:
        print(f"Файл не найден: {file}")
        return []
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return []


if __name__ == "__main__":
    transactions = reading_csv_file("C:/Users/cfif/PycharmProjects/PythonProject8/data/transactions (1).csv")
    print(transactions[:10])


def reading_excel_file(path_excel: str) -> list:
    try:
        df_exl = pd.read_excel(path_excel)
        transactions_exl_list = df_exl.to_dict(orient="records")
    except ValueError as e:
        raise ValueError(f"Ошибка при чтении файла Excel: {e}")
    return transactions_exl_list

if __name__ == "__main__":
    transactions = reading_csv_file("../data/transactions_excel.xlsx")
    print(transactions[:10])
