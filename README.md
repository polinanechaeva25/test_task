# Проект Connect Stripe

Connect Stripe - проект, в котором реализовано общение со Stripe и создание платёжных форм для товаров.

## Запуск
1. Клонируйте репозиторий с GitHub
2. Создайте виртуальное окружение
3. Установите зависисмости `pip install -r requirements.txt`
4. Запустите сервер командой `python3 manage.py runserver`

## Модель

В проекте создана модель Item для описания продукта. Поля модели: имя, описание, цена продукта.

## Доступные urls
* По default проект разворачивается на порту 8000. Чтобы открыть стартовую страницу вводим адрес:
`http://127.0.0.1:8000/item/`
  * По указаному адресу доступна таблица с товарами типа:

    ID | Name | Description | Price 
    :--|:----:|:-----------:|------:
    1 | Телефон | Мобильный телефон | 600.99
* При клике по идентефикатору товара, происходит редирект на страницу с отдыльным описанием товара
и кнопкой для покупки товара: `http://127.0.0.1:8000/item/1`[^1]
* При нажатии на кнопку "Buy" происходит обращение к url `http://127.0.0.1:8000/buy/1`[^1].
Данный адрес хранит в себе данные о сессии. Обращаясь к нему, мы извлекаем id сессии и перенаправляемся на API Stripe.
[^1]: В данном случае 1, указанная в url адресе, - Id выбранного товара.
* Встроенная Django Admin доступна по адресу: `http://127.0.0.1:8000/admin/`
  * Для создания суперпользователя используйте команду `python3 manage.py createsuperuser`
  * Авторизируясь, как суперпользователь, есть возможность просматривать и создавать объекты существующих моделей. 

## Создание тестовых продуктов
+ Для создания нужного количества продуктов модели Item воспользуйтесь командой: `python3 manage.py create_items <number>`
,где `<number>` - колчество тестовых элементов, которое вы хотели бы создать. 
+ При выполнении этой команды 
так же создается суперпользователь с именем `admin` и паролем `adminadmin`. 
