import requests
import json
import logging
import time

logging.basicConfig(
    filename="server.log",
    filemode='a',
    level=logging.INFO,
    format='{levelname} {asctime} {name} : {message}',
    style='{'
)
log = logging.getLogger(__name__)


def main(url):
    try:
        r = requests.get(url)
    except Exception as err:
        logging.error("Вибачте, але в програмі виникла помилка:\n%s\n", err)
        print("Виникла помилка:\n", err, "\n\n")
    else:
        try:
            data = json.loads(r.content)
        except Exception as err:
            logging.warning("Неможливо отримати JSON-дані!\n%s\n", err)
            print("Неможливо отримати JSON-дані\n", err, "\n\n")
        else:
            print("Server працює!\n")
            logging.info("Сервер доступний. Час на сервері: %s", data['date'])
            logging.info("Запитувана сторінка: : %s", data['current_page'])
            logging.info("Відповідь сервера місти наступні поля:")
            for key in data.keys():
                logging.info("Ключ: %s, Значення: %s", key, data[key])


if __name__ == '__main__':
    while True:
        main("http://localhost:8000/health")
        time.sleep(60)

