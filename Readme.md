# Проект "Финансовый менеджер"

## Описание
Простое приложение для управления финансами, позволяющее добавлять, редактировать, искать записи и отображать баланс.

## Установка
* Клонируйте репозиторий на свой компьютер:

`git clone https://github.com/your_username/finance-manager.git`

* Перейдите в директорию проекта:
`cd finance-manager`

* Зависимости устанавливать не надо!

## Использование

* Запустите приложение:
`python main.py`

Следуйте инструкциям в меню для выполнения различных действий, таких как добавление записей, редактирование, поиск и просмотр баланса.

Для выхода из приложения выберите соответствующий пункт в меню или нажмите Ctrl + C.

## Структура проекта
* **main.py**: Главный файл приложения, содержащий интерфейс пользователя.
* **classes.py**: Модуль, содержащий классы Record (для хранения записей) и FinanceManager (для управления данными).
* **finance_records.csv**: Файл для хранения данных о финансовых записях.

## Тестирование
Чтобы запустить тесты, выполните следующую команду:
`python test.py`