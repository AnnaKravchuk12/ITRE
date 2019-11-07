# Lab_3: Вступ до моніторингу.

* :heavy_check_mark: середовище з інстальованим Python / pip / pipenv;
* :heavy_check_mark: будь-який WEB-браузер;

## What to do.

1. Створила папку з назвою лаб. роботи. Ініціалізувала середовище pipenv. Інсталювала необхідні пакети `pipenv --python 3.7` `python install django`

2. Створила заготовку django-template командою `pipenv run django-admin startproject beautiful_project`. Винесла файли на рівень вище `mv beautiful_project/beautiful_project/* beautiful_project/`. `mv beautiful_project/manage.py ./`

3. Запустила сервер та переконалась, що все працює: ![](./photo/server-work.png) ![](./photo/browser.png)

4. Створила коміт з базовим темплейтом. Файл `db.sqlite3` виключила з коміту шляхом додавання його назви до файлу `.gitignore`.
