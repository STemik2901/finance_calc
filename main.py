from classes import Record, FinanceManager
import os


# Меню пользователя
def main():
    """
    Основная функция для работы с программой управления финансами.

    Функция отображает главное меню и предоставляет пользователю выбор действий.

    При выборе действий пользователь может добавить новую запись о финансовой операции,
    изменить существующую запись, выполнить поиск по записям, отобразить баланс или выйти из программы.

    Программа будет повторяться до выбора пользователем действия "Выйти".

    Raises:
        ValueError: Если пользователь вводит некорректный выбор действия.

    """

    manager = FinanceManager("finance_records.csv")

    while True:
        print("Меню:")
        print("1. Добавить запись")
        print("2. Изменить запись")
        print("3. Поиск записей")
        print("4. Показать баланс")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            os.system('cls')

            date = input("Введите дату (YYYY-MM-DD): ")
            category = input("Введите категорию (Доход или Расход): ").capitalize()
            amount = float(input("Введите сумму: "))
            description = input("Введите описание: ")

            os.system('cls')
            try:
                record = Record(date, category, amount, description)
                manager.add_record(record)
                print('Запись успешно добавлена!', '\n')
            except Exception as e:
                print('Ошибка!', e, '\n')
                main()

        elif choice == '2':
            os.system('cls')

            data = manager.search_records()

            if not data:
                os.system('cls')
                print('Создайте хотя бы одну запись!', '\n')
                main()

            print("Выберите запись для редактирования:")
            for i, row in enumerate(data):
                print(f"{i + 1}. {row}")

            choice = int(input("Введите номер записи для редактирования: ")) - 1
            if 0 <= choice < len(data):
                os.system('cls')

                selected_record = data[choice]
                print("Выбранная запись:", selected_record)
                print("Выберите поля для редактирования:")
                print("1. Дата")
                print("2. Категория")
                print("3. Сумма")
                print("4. Описание")
                fields_to_edit = input("Введите номера полей через пробел: ").split()
                new_record = Record(
                    selected_record['Дата'],
                    selected_record['Категория'],
                    float(selected_record['Сумма']),
                    selected_record['Описание']
                )
                for field in fields_to_edit:
                    if field == '1':
                        new_record.date = input("Введите новую дату: ")
                    elif field == '2':
                        new_record.category = input("Введите новую категорию: ").capitalize()
                    elif field == '3':
                        new_record.amount = float(input("Введите новую сумму: "))
                    elif field == '4':
                        new_record.description = input("Введите новое описание: ")

                os.system('cls')
                try:
                    Record.validate_record(
                        new_record.date,
                        new_record.category,
                        new_record.amount,
                        new_record.description
                    )
                except Exception as e:
                    print('Ошибка!', e, '\n')
                    main()

                manager.edit_record(Record(
                    selected_record['Дата'],
                    selected_record['Категория'],
                    float(selected_record['Сумма']),
                    selected_record['Описание']), new_record)
                print("Запись успешно изменена!", '\n')
            else:
                print("Неверный номер записи!", '\n')
                main()

        elif choice == '3':
            os.system('cls')

            date = input("Введите дату записи для поиска (если не требуется, оставьте пустым): ")
            category = input("Введите категорию записи для поиска (если не требуется, оставьте пустым): ").capitalize()
            amount = input("Введите сумму записи для поиска (если не требуется, оставьте пустым): ")
            description = input("Введите описание записи для поиска (если не требуется, оставьте пустым): ")
            results = manager.search_records(date, category, amount, description)

            os.system('cls')
            if results:
                print("Результаты поиска:")
                for row in results:
                    print(row)
            else:
                print("Записи не найдены!")

            print()
            main()

        elif choice == '4':
            os.system('cls')
            manager.show_balance()

            print()
            main()

        elif choice == '5':
            print("Выход из программы")
            exit(52)

        else:
            os.system('cls')
            print("Неверный ввод. Пожалуйста, выберите действие из списка")

            print()
            main()


if __name__ == "__main__":
    os.system('cls')
    main()
