
<h2>Автотесты на API проекта «Битва покемонов»</h2>

> **Статус проекта:**
> Проект закрытый для POST запросов, но GET можно выполнять без токена: https://pokemonbattle.ru/
> 
> 🟢 Поддерживается (активный) 

## Описание проекта и задачи
Автоматизировать часть проверок регресса с помощью Pytest и Requests

## Тест-кейсы, которые автоматизировали
* Создание покемона `POST /pokemons`
* Смена имени покемона `PUT /pokemons`
* Поймать покемона в покебол `POST /trainers/add_pokeball`
* Проверить ответ метода `GET /trainers`

Ожидаемый ответ: 
* response `status code` = 200
* в ответе в `json` приходит корректное поле `trainer_name`
* в ответе приходит корректное поле id в json

## Детали реализации

1. Автотесты написаны с применением PyTest
2. Используется библиотека Requests
3. Параметризированные тесты с использованием декоратора

![image](https://raw.githubusercontent.com/QA-SirFourALot/python_autotests/main/Tests.png)

## Локальный запуск тестов (из терминала)
1. Скачать проект
2. Перейти через терминал в директорию проекта
3. Выполнить команду:
3. Создаём виртуальное окружение внутри папки проекта.
Команды для Windows:

Если вы указали путь до python.exe

``` markdown
PS> python -m venv venv
```
Если вы не указывали путь до python.exe

``` markdown
PS> C:\Users\Name\AppData\Local\Programs\Python\Python310\python -m venv venv
```
Теперь, когда вы создали виртуальное окружение, необходимо запустить скрипт активации

``` markdown
PS> venv\Scripts\activate (venv) PS>
```

4. Устанавливаем библиотеки

``` markdown
(venv) PS> python -m pip install requests
```

``` markdown
(venv) PS> python -m pip install pytest
```

Запускаем
``` markdown
pytest tests/test_pokemons.py
```

5. Ожидаемый результат: получим отчет о прохождении тестов.


## Автор

Клим Истомин ([@SirFouralot](https://t.me/SirFouralot))

