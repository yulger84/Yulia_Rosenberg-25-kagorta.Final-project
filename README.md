# Автоматизация тестирования проверяется, что по треку заказа можно получить данные о заказе.
Описание проекта

Этот проект представляет собой автоматизацию тестирования, что по треку заказа можно получить данные о заказе.
Тесты реализованы в соответствии с подготовленным чек-листом и выполняются с использованием Python и библиотеки pytest.
1. Выполнить запрос на создание заказа.
2. Сохранить номер трека заказа.
3. Выполнить запрос на получения заказа по треку заказа.
4. Проверить, что код ответа равен 200.

- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполняется командой pytest
# Структура проекта
config.py: Конфигурационный файл. Содержит настройки окружения, такие как базовый URL API

data.py: Файл с тестовыми данными. Включает заранее подготовленные позитивные и негативные значения для проверки корректности работы поля "name".

test_create_order.py: Модуль для выполнения стандартных API-запросов. Содержит функции для создания заказа, получения трека, и проверка получения заказа по номеру трека.

# Подготовка к запуску

- Выполнить запрос на создание нового заказа. Сохранить значение трека из ответа. Это необходимо для выполнения последующих запросов.
Получить данные о заказа по номеру трека:
- Выполнить запрос на получение данных о заказе по номеру трека. Убедиться, что код ответа равен 200

