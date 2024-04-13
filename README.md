# Сервис для создания коротких ссылок на основе Flask
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
### Возможности сервиса:
- генерация коротких ссылок и связь их с исходными длинными ссылками,
- переадресация на исходный адрес при обращении к коротким ссылкам.

### Технологии проекта
* Python
* Flask - отдельный фреймворк для работы с веб сайтами. 

### Для работы проекта в .env необходимо указать следующие переменные

```
FLASK_APP=yacut
FLASK_ENV=

DATABASE_URI=
SECRET_KEY=
```

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/VladErm91/yacut.git

cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Запуск сервиса 

```
flask run
```

Автор: [VladErm91](https://github.com/VladErm91)
