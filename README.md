# GazQRcode
Python скрипт, который генерирует QR-коды из данных в XML-файле(если в директории несколько xml-файлов, скрипт возьмет последний добавленный или обновленный файл)


## Инструкция по использованию GazQRcode


### Установка:

Linux (с установленным Git):

1. Клонируйте репозиторий Git:

`git clone https://github.com/botrott7/GazQRcode.git


2. Перейдите в директорию проекта:

`cd GazQRcode`


3. Создайте виртуальное окружение Python:

`python3 -m venv venv`


4. Активируйте виртуальное окружение:

`source venv/bin/activate`


5. Установите библиотеки из файла requirements.txt:

`pip install -r requirements.txt`


6. Запустите скрипт main.py:

`python main.py`


Использование:

* Создадутся директории: qr_imgs и xml_files.
* Поместите файл с форматом xlsx в директорию xml_files.
* !таблица должна содержать поля
* ![img.png](img/img.png)
* запустите скрипт `python main.py`
* результат в директории qr_imgs
