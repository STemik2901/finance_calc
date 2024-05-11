import csv, re
from typing import List, Dict, Any


class Record:
    """Класс для представления записи"""

    def __init__(self, date: str, category: str, amount: float, description: str):
        """
        Создает новую запись о финансовой операции.

        Args:
            date (str): Дата операции в формате 'YYYY-MM-DD'.
            category (str): Категория операции ('Доход' или 'Расход').
            amount (float): Сумма операции.
            description (str): Описание операции.

        Raises:
            TypeError: Если дата или категория не являются строками, или сумма не является числом,
                или описание не является строкой или None.
            ValueError: Если дата не соответствует формату YYYY-MM-DD, или категория некорректна,
                или сумма отрицательна или равна нулю.
        """
        self.validate_record(date, category, amount, description)

        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    @staticmethod
    def validate_record(date, category, amount, description):
        """
        Проверяет корректность переданных данных для создания записи о финансовой операции.

        Args:
            date (str): Дата операции в формате 'YYYY-MM-DD'.
            category (str): Категория операции ('Доход' или 'Расход').
            amount (float): Сумма операции.
            description (str): Описание операции.

        Raises:
            TypeError: Если дата или категория не являются строками, или сумма не является числом,
                или описание не является строкой или None.
            ValueError: Если дата не соответствует формату YYYY-MM-DD, или категория некорректна,
                или сумма отрицательна или равна нулю.

        Returns:
            bool: True, если данные прошли проверку успешно.
        """
        if not isinstance(date, str):
            raise TypeError("Дата должна быть строкой")
        if not isinstance(category, str):
            raise TypeError("Категория должна быть строкой")
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть числом")
        if description is not None and not isinstance(description, str):
            raise TypeError("Описание должно быть строкой или None")

        if not re.match(r'\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])', date):
            raise ValueError("Дата должна быть в формате YYYY-MM-DD")
        if category not in ['Доход', 'Расход']:
            raise ValueError("Категория должна быть 'Доход' или 'Расход'")
        if amount <= 0:
            raise ValueError("Сумма должна быть положительным числом")
        return True


class FinanceManager:
    """Класс для управления финансами, предоставляющий функции
    добавления, изменения, поиска записей и отображения баланса"""

    def __init__(self, file_path: str):
        """
        Инициализирует объект FinanceManager.

        Args:
            file_path (str): Путь к файлу для хранения записей.

        Attributes:
            file_path (str): Путь к файлу для хранения записей.
            data (List[Dict[str, Any]]): Список словарей, представляющих данные о финансовых операциях.

        Raises:
            FileNotFoundError: Если указанный файл не найден.
        """
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self) -> List[Dict[str, Any]]:
        """
        Загружает данные из файла CSV.

        Returns:
            List[Dict[str, Any]]: Список словарей с данными о финансовых операциях.
        """

        try:
            with open(self.file_path, mode='r') as file:
                reader = csv.DictReader(file)
                data = [row for row in reader]
        except FileNotFoundError:
            data = []
        return data

    def save_data(self):
        """
        Сохраняет данные в файл CSV.
        """

        with open(self.file_path, mode='w+', newline='') as file:
            fieldnames = ['Дата', 'Категория', 'Сумма', 'Описание']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for row in self.data:
                writer.writerow(row)

    def show_balance(self):
        """
        Выводит информацию о доходах, расходах и общем балансе.
        """

        incomes = sum(float(row['Сумма']) for row in self.data if row['Категория'] == 'Доход')
        expenses = sum(float(row['Сумма']) for row in self.data if row['Категория'] == 'Расход')
        balance = incomes - expenses
        print(f'Доходы: {incomes}\nРасходы: {expenses}\nБаланс: {balance}')

    def add_record(self, record: Record):
        """
        Добавляет запись о финансовой операции.

        Args:
            record (Record): Запись о финансовой операции.
        """

        self.data.append(
            {
                'Дата': record.date,
                'Категория': record.category,
                'Сумма': record.amount,
                'Описание': record.description
            })
        self.save_data()

    def edit_record(self, old_record: Record, new_record: Record):
        """
        Изменяет запись о финансовой операции.

        Args:
            old_record (Record): Существующая запись о финансовой операции.
            new_record (Record): Новая запись о финансовой операции.
        """

        for row in self.data:
            if (
                    (row['Дата'] == old_record.date) and
                    (row['Категория'] == old_record.category) and
                    (float(row['Сумма']) == old_record.amount) and
                    (row['Описание'] == old_record.description)
            ):
                row['Дата'] = new_record.date
                row['Категория'] = new_record.category
                row['Сумма'] = new_record.amount
                row['Описание'] = new_record.description
        self.save_data()

    def search_records(self, date='', category='', amount='', description=''):
        """
        Ищет записи о финансовых операциях по заданным параметрам.

        Args:
            date (str): Дата операции для поиска.
            category (str): Категория операции для поиска.
            amount (str): Сумма операции для поиска.
            description (str): Описание операции для поиска.

        Returns:
            List[Dict[str, Any]]: Список словарей, содержащих найденные записи о финансовых операциях.
        """

        results = []
        for row in self.data:
            if (
                (date == '' or row['Дата'] == date) and
                (category == '' or row['Категория'] == category) and
                (amount == '' or row['Сумма'] == amount) and
                (description == '' or row['Описание'] == description)
            ):
                results.append(row)
        return results
