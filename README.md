# Сервис для создания коротких ссылок на основе Flask
### Учебный проект Яндекс Практикум

## Возможности сервиса:
- генерация коротких ссылок и связь их с исходными длинными ссылками,
- переадресация на исходный адрес при обращении к коротким ссылкам.

## Технологии проекта
* Python
* Flask - отдельный фреймворк для работы с веб сайтами. 

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
## Запуск парсера
```
flask run
```

Автор: [VladErm91](https://github.com/VladErm91)